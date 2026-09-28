"""Extrae las propiedades publicadas en RE/MAX Venezuela para Guatire, Guarenas y
las Costas Mirandinas.

Cómo funciona: el buscador público de remax.com.ve no devuelve resultados a
consultas automáticas, pero la página de cada oficina (remax.com.ve/<oficina>)
trae sus propiedades en un JSON dentro del HTML. El script recorre todas las
oficinas, todas sus páginas, y se queda con las propiedades de nuestras zonas.

Respeta el "Crawl-delay: 1" de robots.txt (1 segundo entre peticiones).

Uso:
    python3 analisis/scripts/remax_scraper.py
Genera:
    analisis/datos/remax_<AAAA-MM-DD>.json
"""

import datetime
import html
import json
import pathlib
import re
import sys
import time
import urllib.request

BASE = "https://www.remax.com.ve"
PAUSA = 1.0  # segundos entre peticiones (robots.txt: Crawl-delay: 1)
NO_OFICINAS = {"blog", "contacto", "inmuebles", "quienes-somos", "nuestros-agentes",
               "nuestras-oficinas", "ser-agente-remax", "adquirir-franquicia-remax",
               "solicitar-inmueble", "ofrecer-inmueble", "privacy-policy", "cookie-policy"}

# Municipios de las Costas Mirandinas (Barlovento costero).
MUNICIPIOS_COSTA = {"brion", "paez", "pedro gual", "andres bello", "buroz"}
LOCALIDADES_COSTA = {"higuerote", "rio chico", "carenero", "tacarigua", "buche",
                     "chirimena", "cupira", "machurucuto", "san jose de barlovento",
                     "mamporal", "el guapo", "tacarigua de la laguna"}

SALIDA = pathlib.Path(__file__).resolve().parents[1] / "datos"


def sin_acentos(texto):
    import unicodedata
    texto = unicodedata.normalize("NFD", texto or "")
    return "".join(c for c in texto if unicodedata.category(c) != "Mn").lower().strip()


def bajar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (analisis-remax-delta)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def oficinas():
    slugs, pagina = set(), 1
    while True:
        html_pag = bajar(f"{BASE}/nuestras-oficinas?page={pagina}")
        nuevas = set(re.findall(r'href="https://www\.remax\.com\.ve/([a-z0-9-]+)"', html_pag)) - NO_OFICINAS
        if not nuevas - slugs:
            break
        slugs |= nuevas
        pagina += 1
        time.sleep(PAUSA)
    return sorted(slugs)


def inmuebles_de(html_pag):
    for props in re.findall(r'data-props="([^"]*)"', html_pag):
        try:
            datos = json.loads(html.unescape(props))
        except ValueError:
            continue
        if isinstance(datos, dict) and isinstance(datos.get("inmuebles"), list):
            return datos["inmuebles"]
    return []


def zona(inm):
    localidad = sin_acentos(inm.get("localidad"))
    municipio = sin_acentos(inm.get("subRegion"))
    if sin_acentos(inm.get("region")) != "miranda":
        return None
    if localidad == "guatire" or municipio == "zamora":
        return "Guatire"
    if localidad == "guarenas" or municipio == "plaza":
        return "Guarenas"
    if localidad in LOCALIDADES_COSTA or municipio in MUNICIPIOS_COSTA:
        return "Costas Mirandinas"
    return None


def numero(texto):
    """'37.000,00 USD $' -> 37000.0 ; devuelve None si no hay número."""
    m = re.search(r"[\d.]+(?:,\d+)?", texto or "")
    if not m:
        return None
    try:
        return float(m.group(0).replace(".", "").replace(",", "."))
    except ValueError:
        return None


def limpiar(inm, oficina, zona_):
    return {
        "codigo": inm.get("codigoInmuebleRemax") or inm.get("idInmueble"),
        "fuente": "RE/MAX Venezuela",
        "oficina": oficina,
        "zona": zona_,
        "localidad": inm.get("localidad"),
        "municipio": inm.get("subRegion"),
        "sector": inm.get("city"),
        "direccion": inm.get("detalleUbicacion"),
        "tipo": inm.get("tipoInmueble"),
        "operacion": inm.get("operacion"),
        "titulo": (inm.get("nombre") or "").strip(),
        "precio_usd": numero(inm.get("precioReferencial")),
        "precio_texto": inm.get("precioReferencial"),
        "m2_construccion": numero(inm.get("areaConstruccion")),
        "m2_terreno": numero(inm.get("areaTerreno")),
        "habitaciones": inm.get("nroHabitaciones"),
        "banos": inm.get("nroBanios"),
        "estacionamientos": inm.get("nroPuestosEstacionamiento"),
        "foto": inm.get("foto"),
        "enlace": inm.get("urlNew") or inm.get("url"),
        "latitud": inm.get("latitud"),
        "longitud": inm.get("longitud"),
    }


def main():
    lista = oficinas()
    print(f"{len(lista)} oficinas", file=sys.stderr)
    encontrados = {}
    for i, oficina in enumerate(lista, 1):
        pagina, vistos = 1, set()
        while True:
            time.sleep(PAUSA)
            try:
                inms = inmuebles_de(bajar(f"{BASE}/{oficina}?page={pagina}"))
            except Exception as e:  # una oficina caída no detiene el resto
                print(f"  {oficina} p{pagina}: {e}", file=sys.stderr)
                break
            ids = {x.get("idInmueble") for x in inms}
            if not inms or ids <= vistos:
                break
            vistos |= ids
            for inm in inms:
                z = zona(inm)
                if z:
                    fila = limpiar(inm, oficina, z)
                    encontrados[fila["codigo"]] = fila
            pagina += 1
        print(f"[{i}/{len(lista)}] {oficina}: {len(vistos)} inmuebles; en zona acumulados {len(encontrados)}",
              file=sys.stderr)

    SALIDA.mkdir(parents=True, exist_ok=True)
    hoy = datetime.date.today().isoformat()
    destino = SALIDA / f"remax_{hoy}.json"
    datos = {"fecha": hoy, "fuente": BASE, "total": len(encontrados),
             "inmuebles": sorted(encontrados.values(), key=lambda x: (x["zona"], x["tipo"] or "", x["precio_usd"] or 0))}
    destino.write_text(json.dumps(datos, ensure_ascii=False, indent=1))
    print(f"Guardado {destino} con {len(encontrados)} inmuebles", file=sys.stderr)


if __name__ == "__main__":
    main()
