"""Extrae propiedades de Guatire, Guarenas y Costas Mirandinas de otros portales:
Century 21 Venezuela, ZonaVen y BienesOnline. Cada propiedad lleva su enlace exacto.

- Century 21 (century21.com.ve): el listado nacional trae los datos en un JSON dentro
  del HTML (window.REP_LOG_APP_PROPS). Se recorren todas las páginas y se filtra por zona.
  Su robots.txt permite explícitamente a los asistentes de IA.
- ZonaVen (zonaven.com): se toman los enlaces de las páginas por ciudad y tipo y del
  sitemap de avisos; cada aviso trae un JSON-LD (RealEstateListing) con precio, fecha de
  publicación y ubicación.
- BienesOnline (bienesonline.ai): páginas por tipo y ciudad; cada aviso trae JSON-LD con
  precio, metros, ubicación y la inmobiliaria que lo publica.

Pausa de 2 s entre peticiones. Uso:
    python3 analisis/scripts/portales_scraper.py
Genera analisis/datos/portales_<AAAA-MM-DD>.json con el mismo formato que remax_scraper.
"""

import datetime
import html
import json
import pathlib
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

PAUSA = 2.0
SALIDA = pathlib.Path(__file__).resolve().parents[1] / "datos"
UA = {"User-Agent": "Mozilla/5.0 (analisis-remax-delta)"}

MUNICIPIOS_COSTA = {"brion", "paez", "pedro gual", "andres bello", "buroz", "acevedo"}
LOCALIDADES_COSTA = {"higuerote", "rio chico", "carenero", "tacarigua", "tacarigua de brion",
                     "buche", "chirimena", "cupira", "machurucuto", "san jose de barlovento",
                     "mamporal", "el guapo", "tacarigua de la laguna", "puerto encantado", "caucagua"}


def norm(t):
    t = unicodedata.normalize("NFD", str(t or ""))
    return re.sub(r"\s+", " ", "".join(c for c in t if unicodedata.category(c) != "Mn")).lower().strip()


def zona_de(*textos):
    t = " | ".join(norm(x) for x in textos if x)
    if "guatire" in t or "araira" in t or "zamora" in t:
        return "Guatire"
    if "guarenas" in t or "plaza" == t.strip():
        return "Guarenas"
    if any(x in t for x in LOCALIDADES_COSTA | MUNICIPIOS_COSTA):
        return "Costas Mirandinas"
    return None


def bajar(url):
    time.sleep(PAUSA)
    url = urllib.parse.quote(url, safe=":/?=&%#+,;@")  # direcciones con ñ o acentos
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def ld_json(texto):
    for bloque in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', texto, re.S):
        try:
            d = json.loads(bloque)
        except ValueError:
            continue
        nodos = d.get("@graph", [d]) if isinstance(d, dict) else d
        for n in nodos:
            if isinstance(n, dict):
                yield n


def tipo_normal(t):
    t = norm(t)
    if any(x in t for x in ("terreno", "parcela", "lote")):
        return "Terreno y Parcela"
    if any(x in t for x in ("galpon", "industrial", "bodega", "nave")):
        return "Local Industrial y Galpón"
    if "local" in t or "comercial" in t:
        return "Local Comercial"
    if any(x in t for x in ("apartamento", "departamento", "penthouse", "apto")):
        return "Apartamento"
    if any(x in t for x in ("casa", "town", "quinta")):
        return "Casa o TownHouse"
    if "oficina" in t or "consultorio" in t:
        return "Oficina"
    if "edificio" in t:
        return "Edificio"
    if any(x in t for x in ("finca", "hacienda")):
        return "Hacienda y Finca"
    return "Otro"


def fila(**k):
    base = {"codigo": None, "fuente": None, "oficina": None, "zona": None, "localidad": None,
            "municipio": None, "sector": None, "direccion": None, "tipo": None, "operacion": "Venta",
            "titulo": "", "precio_usd": None, "precio_texto": None, "m2_construccion": None,
            "m2_terreno": None, "habitaciones": None, "banos": None, "estacionamientos": None,
            "enlace": None, "latitud": None, "longitud": None, "fecha_publicacion": None}
    base.update(k)
    for c in ("m2_construccion", "m2_terreno", "habitaciones", "banos", "estacionamientos", "precio_usd"):
        try:
            base[c] = float(base[c]) if base[c] not in (None, "", 0, "0") else None
        except (TypeError, ValueError):
            base[c] = None
    return base


# ---------------------------------------------------------------- Century 21
def century21():
    out = []
    for operacion, slug in (("Venta", "operacion_venta"), ("Alquiler", "operacion_alquiler")):
        pagina = 1
        while True:
            url = f"https://www.century21.com.ve/v/resultados/{slug}" + (f"/pagina_{pagina}" if pagina > 1 else "")
            try:
                s = bajar(url)
            except Exception as e:
                print(f"  c21 {url}: {e}", file=sys.stderr)
                break
            i = s.find("window.REP_LOG_APP_PROPS")
            if i < 0:
                break
            j = s.find("data:", i) + 5
            try:
                d, _ = json.JSONDecoder().raw_decode(s[j:].lstrip())
            except ValueError:
                break
            res = d.get("results") or []
            if not res:
                break
            for r in res:
                if norm(r.get("estado")) != "miranda":
                    continue
                z = zona_de(r.get("municipio"), r.get("colonia"), r.get("encabezado"))
                if not z:
                    continue
                if r.get("ocultarPrecioInternet"):
                    precio = None
                else:
                    precio = (r.get("precios") or {}).get("vista", {}).get("precio") or r.get("precio")
                out.append(fila(
                    codigo=f"c21-{r.get('idPropiedadesOS') or r.get('id')}", fuente="Century 21",
                    oficina=r.get("nombreAfiliado"), zona=z, localidad=r.get("municipio"),
                    sector=r.get("colonia"), direccion=", ".join(x for x in (r.get("colonia"), r.get("municipio"), r.get("estado")) if x),
                    tipo=tipo_normal(r.get("tipoPropiedadTrans") or r.get("tipoPropiedad")), operacion=operacion,
                    titulo=(r.get("encabezado") or "").strip(), precio_usd=precio if (r.get("moneda") or "USD") == "USD" else None,
                    precio_texto=r.get("precioFormat"), m2_construccion=r.get("m2C"), m2_terreno=r.get("m2T"),
                    habitaciones=r.get("recamaras"), banos=r.get("banos"), estacionamientos=r.get("estacionamientos"),
                    enlace="https://www.century21.com.ve" + (r.get("urlCorrectaPropiedad") or ""),
                    latitud=r.get("lat"), longitud=r.get("lon"), fecha_publicacion=r.get("fechaAlta")))
            print(f"  c21 {operacion} p{pagina}: {len(res)} avisos; en zona {len(out)}", file=sys.stderr)
            pagina += 1
    return out


# ---------------------------------------------------------------- ZonaVen
ZV_CIUDADES = ["guatire", "guarenas", "higuerote", "rio-chico"]
ZV_TIPOS = ["apartamentos", "casas", "terrenos", "locales", "oficinas", "galpones", "edificios",
            "casas-rusticas", "propiedades"]
ZV_CLAVES = ("guatire", "guarenas", "higuerote", "rio-chico", "carenero", "araira", "tacarigua",
             "barlovento", "brion", "buche", "chirimena", "cupira", "caucagua")


def zonaven():
    enlaces = set()
    for op in ("venta", "alquiler"):
        for t in ZV_TIPOS:
            for c in ZV_CIUDADES:
                try:
                    s = bajar(f"https://zonaven.com/{op}-{t}/{c}")
                except Exception:
                    continue
                for n in ld_json(s):
                    for it in (n.get("itemListElement") or []) if n.get("@type") == "ItemList" else []:
                        if it.get("url"):
                            enlaces.add(it["url"])
    for n in (1, 2):
        try:
            s = bajar(f"https://zonaven.com/sitemap-listings-{n}.xml")
        except Exception:
            continue
        for u in re.findall(r"<loc>([^<]+)</loc>", s):
            if any(k in u.lower() for k in ZV_CLAVES):
                enlaces.add(u)
    print(f"  zonaven: {len(enlaces)} enlaces a revisar", file=sys.stderr)
    out = []
    for u in sorted(enlaces):
        try:
            s = bajar(u)
        except urllib.error.HTTPError:
            continue  # aviso vencido
        except Exception as e:
            print(f"  zonaven {u}: {e}", file=sys.stderr)
            continue
        for n in ld_json(s):
            tipos = n.get("@type")
            tipos = tipos if isinstance(tipos, list) else [tipos]
            if "RealEstateListing" not in tipos:
                continue
            addr = n.get("address") or {}
            if norm(addr.get("addressRegion")) not in ("miranda", ""):
                continue
            z = zona_de(addr.get("addressLocality"), n.get("name"))
            if not z:
                continue
            of = n.get("offers") or {}
            extra = n.get("additionalProperty") or []
            extra = extra if isinstance(extra, list) else [extra]
            props = {norm(p.get("name")): p.get("value") for p in extra if isinstance(p, dict)}
            fs = n.get("floorSize") or {}
            ls = n.get("lotSize") or {}
            forma = [t for t in tipos if t != "RealEstateListing"]
            out.append(fila(
                codigo="zv-" + u.rstrip("/").rsplit("/", 1)[-1], fuente="ZonaVen", zona=z,
                localidad=(addr.get("addressLocality") or "").strip(), direccion=addr.get("streetAddress"),
                tipo=tipo_normal(" ".join(forma) + " " + (n.get("name") or "")),
                operacion="Alquiler" if norm(n.get("category")) == "alquiler" or "/alquiler/" in u else "Venta",
                titulo=(n.get("name") or "").strip(),
                precio_usd=of.get("price") if (of.get("priceCurrency") or "USD") == "USD" else None,
                precio_texto=f"{of.get('price')} {of.get('priceCurrency') or ''}".strip(),
                m2_construccion=fs.get("value") if isinstance(fs, dict) else None,
                m2_terreno=ls.get("value") if isinstance(ls, dict) else props.get("area del terreno"),
                habitaciones=n.get("numberOfRooms") or n.get("numberOfBedrooms"),
                banos=n.get("numberOfBathroomsTotal"), estacionamientos=n.get("numberOfParkingSpaces"),
                enlace=u, fecha_publicacion=(n.get("datePosted") or "")[:10] or None))
            break
    return out


# ---------------------------------------------------------------- BienesOnline
BO_CIUDADES = ["guatire", "guarenas", "higuerote", "rio-chico"]
BO_TIPOS = ["terreno", "casa", "apartamento", "local", "galpon", "oficina", "edificio", "finca"]


def bienesonline():
    enlaces = {}  # enlace -> operación de la página donde apareció
    for op in ("venta", "alquiler"):
        for t in BO_TIPOS:
            for c in BO_CIUDADES:
                pagina = 1
                while pagina <= 20:
                    url = f"https://bienesonline.ai/es/venezuela/{op}/{t}/miranda/{c}" + (f"?page={pagina}" if pagina > 1 else "")
                    try:
                        s = bajar(url)
                    except Exception:
                        break
                    nuevos = set(re.findall(r'href="(https://bienesonline\.ai/es/venezuela/[a-z0-9-]+/propiedad/[^"#?]+)"', s)) - set(enlaces)
                    if not nuevos:
                        break
                    for u in nuevos:
                        enlaces[u] = "Alquiler" if op == "alquiler" else "Venta"
                    if f"page={pagina + 1}" not in s:
                        break
                    pagina += 1
    print(f"  bienesonline: {len(enlaces)} enlaces a revisar", file=sys.stderr)
    out = []
    for u, operacion in sorted(enlaces.items()):
        try:
            s = bajar(u)
        except Exception:
            continue
        lugar, oferta, aviso = {}, {}, {}
        for n in ld_json(s):
            if n.get("@type") == "Place":
                lugar = n
            elif n.get("@type") == "Offer":
                oferta = n
            elif n.get("@type") == "RealEstateListing":
                aviso = n
        addr = lugar.get("address") or {}
        z = zona_de(addr.get("addressLocality"), aviso.get("name"))
        if not z or norm(addr.get("addressRegion")) not in ("miranda", ""):
            continue
        vendedor = oferta.get("seller") or {}
        empresa = (vendedor.get("worksFor") or {}).get("name") if isinstance(vendedor, dict) else None
        nombre = aviso.get("name") or lugar.get("name") or ""
        out.append(fila(
            codigo="bo-" + u.rsplit("/", 1)[-1].split("-", 1)[0], fuente="BienesOnline",
            oficina=(empresa or (vendedor.get("name") if isinstance(vendedor, dict) else None) or "").strip() or None,
            zona=z, localidad=addr.get("addressLocality"), sector=(addr.get("streetAddress") or "").strip() or None,
            tipo=tipo_normal(nombre), operacion=operacion,
            titulo=nombre.strip(), precio_usd=oferta.get("price") if (oferta.get("priceCurrency") or "USD") == "USD" else None,
            precio_texto=f"{oferta.get('price')} {oferta.get('priceCurrency') or ''}".strip(),
            m2_construccion=(lugar.get("floorSize") or {}).get("value"), m2_terreno=(lugar.get("lotSize") or {}).get("value"),
            habitaciones=lugar.get("numberOfBedrooms"), banos=lugar.get("numberOfBathroomsTotal"),
            estacionamientos=lugar.get("numberOfParkingSpaces"), enlace=u))
    return out


# ---------------------------------------------------------------- Inmobiliarias locales
MESES = {m: i for i, m in enumerate(["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
                                     "septiembre", "octubre", "noviembre", "diciembre"], 1)}
NO_AVISO = {"propiedades", "contacto", "historia", "tips", "nuestros-servicios", "estructura-organizativa",
            "canales-de-pago", "wp-json", "feed", "comments", "consulta-tu-inmueble", "nosotros", "servicios"}


def admyser():
    """Inversiones Admyser (admyser.com): inmobiliaria local de Higuerote y Guarenas-Guatire.
    Cada aviso muestra 'NNN mts2 Precio: $X Edo. Miranda , Ciudad Baños: N Habitaciones: N'."""
    enlaces, pagina = set(), 1
    while pagina <= 30:
        url = "https://admyser.com/propiedades/" + (f"page/{pagina}/" if pagina > 1 else "")
        try:
            s = bajar(url)
        except Exception:
            break
        nuevos = {u for u in re.findall(r'href="(https://admyser\.com/([a-z0-9-]+)/)"', s)
                  if u[1] not in NO_AVISO and not u[1].startswith("page")}
        nuevos = {u[0] for u in nuevos} - enlaces
        if not nuevos:
            break
        enlaces |= nuevos
        pagina += 1
    print(f"  admyser: {len(enlaces)} enlaces a revisar", file=sys.stderr)
    out = []
    for u in sorted(enlaces):
        try:
            s = bajar(u)
        except Exception:
            continue
        t = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
        t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)))
        m_precio = re.search(r"Precio:\s*\$?\s*([\d.]+(?:,\d+)?)", t)
        m_ciudad = re.search(r"Edo\.?\s*Miranda\s*,\s*(.+?)\s+(?:Baños|Habitaciones|Estacionamiento|Vigilancia|\(0)", t)
        if not m_precio or not m_ciudad:
            continue
        ciudad = re.sub(r"\s*\d+(?:[.,]\d+)?\s*mts?.*$", "", m_ciudad.group(1)).strip()  # "Higuerote 218 mts2" -> "Higuerote"
        titulo = re.search(r"<title>(.*?)(?:\s*[-–|]\s*Admyser)?</title>", s, re.S)
        titulo = html.unescape(titulo.group(1)).strip() if titulo else u.rstrip("/").rsplit("/", 1)[-1]
        z = zona_de(ciudad, titulo)
        if not z:
            continue
        num = lambda rx: (re.search(rx, t) or [None, None])[1]
        m2 = num(r"(\d+(?:[.,]\d+)?)\s*mts?\.?\s*2")
        fecha = re.search(r"Publicado:\s*(\d{1,2})\s+(\w+),?\s+(\d{4})", t)
        fecha = f"{fecha.group(3)}-{MESES.get(fecha.group(2).lower(), 1):02d}-{int(fecha.group(1)):02d}" if fecha else None
        es_terreno = "terreno" in norm(titulo)
        out.append(fila(
            codigo="adm-" + u.rstrip("/").rsplit("/", 1)[-1], fuente="Admyser", oficina="Inversiones Admyser",
            zona=z, localidad=ciudad, tipo=tipo_normal(titulo),
            operacion="Alquiler" if "alquiler" in norm(titulo) else "Venta", titulo=titulo,
            precio_usd=m_precio.group(1).replace(".", "").replace(",", "."), precio_texto="$" + m_precio.group(1),
            m2_construccion=None if es_terreno else (m2 or "").replace(",", "."),
            m2_terreno=(m2 or "").replace(",", ".") if es_terreno else None,
            habitaciones=num(r"Habitaciones:\s*(\d+)"), banos=num(r"Baños:\s*(\d+)"),
            estacionamientos=num(r"Estacionamiento:\s*(\d+)"), enlace=u, fecha_publicacion=fecha))
    return out


def main():
    todas = {}
    solo = set(sys.argv[1:])  # opcional: nombres de fuentes a correr, p. ej. "Admyser"
    for nombre, fn in (("Century 21", century21), ("ZonaVen", zonaven), ("BienesOnline", bienesonline), ("Admyser", admyser)):
        if solo and nombre not in solo:
            continue
        print(f"== {nombre}", file=sys.stderr)
        try:
            filas = fn()
        except Exception as e:  # un portal caído no detiene los demás
            print(f"  {nombre} falló: {e}", file=sys.stderr)
            filas = []
        for f in filas:
            todas[f["codigo"]] = f
        print(f"  {nombre}: {len(filas)} en zona", file=sys.stderr)
    SALIDA.mkdir(parents=True, exist_ok=True)
    hoy = datetime.date.today().isoformat()
    sufijo = ("_" + "-".join(sorted(norm(x).replace(" ", "") for x in solo))) if solo else ""
    destino = SALIDA / f"portales_{hoy}{sufijo}.json"
    datos = {"fecha": hoy, "fuente": "Century 21, ZonaVen, BienesOnline", "total": len(todas),
             "inmuebles": sorted(todas.values(), key=lambda x: (x["fuente"], x["zona"], x["tipo"] or ""))}
    destino.write_text(json.dumps(datos, ensure_ascii=False, indent=1))
    print(f"Guardado {destino} con {len(todas)} inmuebles", file=sys.stderr)


if __name__ == "__main__":
    main()
