"""Compara una extracción nueva de RE/MAX con lo que ya está en la base maestra y
prepara las escrituras para la base del artifact.

Reglas:
- Propiedad nueva: se agrega como "por_confirmar".
- Propiedad que sigue publicada: se actualiza "visto_ultima". Si cambió el precio del
  portal se guarda en "cambio_precio"; el precio de la ficha solo se reemplaza si
  todavía está "por_confirmar" (lo confirmado por el equipo no se pisa).
- Propiedad de RE/MAX que ya no aparece: se marca "activo: false" con "salio_en"
  (puede ser un cierre). Las agregadas a mano no se tocan.
- Se escribe un resumen en la colección "extracciones" (doc = fecha).

Uso:
    python3 analisis/scripts/actualizar_base.py \
        --actual <carpeta exportada de la colección inmuebles> \
        --nuevo analisis/datos/remax_<fecha>.json \
        --salida <carpeta de trabajo>
Genera en <salida>: docs/*.json (un archivo por escritura), lote_1.json, lote_2.json…
(listas de escrituras de hasta 50 para ArtifactData "batch") y resumen.json.
"""

import argparse
import json
import pathlib

LOTE = 50


def cargar_actual(carpeta):
    docs = {}
    for f in pathlib.Path(carpeta).rglob("*.json"):
        d = json.loads(f.read_text())
        if isinstance(d, dict) and "data" in d and isinstance(d["data"], dict):
            docs[d.get("id") or f.stem] = d["data"]
        else:
            docs[f.stem] = d
    return docs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--actual", required=True)
    ap.add_argument("--nuevo", required=True)
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()

    actual = cargar_actual(a.actual)
    nuevo = json.loads(pathlib.Path(a.nuevo).read_text())
    fecha = nuevo["fecha"]
    salida = pathlib.Path(a.salida)
    (salida / "docs").mkdir(parents=True, exist_ok=True)

    escrituras, nuevas, salieron, cambios, siguen = [], [], [], [], 0

    def escribir(op, doc_id, data, coleccion="inmuebles"):
        ruta = salida / "docs" / f"{coleccion}__{doc_id}.json"
        ruta.write_text(json.dumps(data, ensure_ascii=False))
        escrituras.append({"op": op, "collection": coleccion, "doc_id": doc_id, "file_path": str(ruta.resolve())})

    vistos = set()
    for x in nuevo["inmuebles"]:
        doc_id = f"remax-{x['codigo']}"
        vistos.add(doc_id)
        fila = {k: v for k, v in x.items() if k != "foto"}
        for k in ("m2_construccion", "m2_terreno", "habitaciones", "banos", "estacionamientos"):
            if not fila.get(k):
                fila[k] = None
        previo = actual.get(doc_id)
        if previo is None:
            fila.update(estado="por_confirmar", activo=True, visto_primera=fecha, visto_ultima=fecha, notas="")
            escribir("set", doc_id, fila)
            nuevas.append(doc_id)
            continue
        siguen += 1
        cambio = {"visto_ultima": fecha, "activo": True, "precio_portal": fila["precio_usd"]}
        if previo.get("activo") is False:
            cambio["salio_en"] = {"__delete__": True}
        antes = previo.get("precio_portal", previo.get("precio_usd"))
        if fila["precio_usd"] is not None and antes is not None and fila["precio_usd"] != antes:
            cambio["cambio_precio"] = {"de": antes, "a": fila["precio_usd"], "fecha": fecha}
            cambios.append({"id": doc_id, "de": antes, "a": fila["precio_usd"]})
            if previo.get("estado") != "confirmado":
                cambio["precio_usd"] = fila["precio_usd"]
                cambio["precio_texto"] = fila["precio_texto"]
        escribir("update", doc_id, cambio)

    for doc_id, previo in actual.items():
        if doc_id in vistos or previo.get("manual") or previo.get("fuente") != "RE/MAX Venezuela":
            continue
        if previo.get("activo") is not False:
            escribir("update", doc_id, {"activo": False, "salio_en": fecha})
            salieron.append(doc_id)

    resumen = {"fecha": fecha, "total_extraidas": len(nuevo["inmuebles"]), "siguen": siguen,
               "nuevas": nuevas, "salieron": salieron, "cambios_precio": cambios}
    escribir("set", fecha, resumen, coleccion="extracciones")

    for i in range(0, len(escrituras), LOTE):
        (salida / f"lote_{i // LOTE + 1}.json").write_text(json.dumps(escrituras[i:i + LOTE], ensure_ascii=False))
    (salida / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1))
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in resumen.items()}, ensure_ascii=False))
    print(f"{(len(escrituras) + LOTE - 1) // LOTE} lote(s) en {salida}")


if __name__ == "__main__":
    main()
