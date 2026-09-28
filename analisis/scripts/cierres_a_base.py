"""Convierte los cierres de los Excel de RE/MAX Delta en documentos para la colección `cierres`
de la base maestra. Primero hay que correr delta_cierres.py (genera los JSON por año).

Uso: python3 analisis/scripts/cierres_a_base.py
Salida: analisis/datos/cierres_base/lote_<n>.json (lotes de hasta 50 escrituras para ArtifactData).

Reglas:
- La zona sale del nombre de la urbanización, con las palabras clave de ZONA_CLAVE (tomadas de los
  sectores que traen los portales y de CLAUDE.md). Si no calza ninguna, queda "Por confirmar".
- El precio publicado y la fecha de salida al mercado salen de la hoja de Reservas o, si no está
  ahí, de las hojas de Captaciones (2024 a 2026) por el código de oficina.
- Lo que Eduardo corrigió el 29-09-2026 está en CORRECCIONES y CIERRES_EXTRA.
"""
import datetime
import json
import re
import unicodedata
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parents[1]
ANIOS = (2025, 2026)
SALIDA = RAIZ / 'datos/cierres_base'


def norm(s):
    s = unicodedata.normalize('NFD', str(s or '')).encode('ascii', 'ignore').decode()
    return re.sub(r'\s+', ' ', s.lower()).strip()


# Palabra clave en la urbanización -> zona. Se revisa en este orden.
ZONA_CLAVE = [
    ('Otra (Caracas)', ['caracas', 'montalban']),
    ('Costas Mirandinas', ['higuerote', 'rio chico', 'los jobos', 'costanera', 'costa grande', 'marina suites',
                           'fuente mar', 'brion', 'carenero', 'tacarigua']),
    ('Guatire', ['guatire', 'castillejo', 'el ingenio', 'las rosas', 'las rosa,', 'araira', 'valle arriba',
                 'valle grande', 'alto grande', 'el marques', 'la sabana', 'vista dorada', 'buenaventura',
                 'buena ventura', 'frutas condominium', 'las flores', 'el desvio', 'oasis', 'las barrancas',
                 'compro', 'vista place', 'parque habitat', 'muralla arriba', 'las margaritas', 'calle zamora',
                 'villa avila', 'palo alto', 'villa heroica', 'el encantado', 'la trinidad']),
    ('Guarenas', ['guarenas', 'casarapa', 'la vaquera', 'terrazas del este', 'cloris', 'san pedro',
                  'trapichito', 'el torreon']),
]


def zona_de(urb):
    u = norm(urb)
    for zona, claves in ZONA_CLAVE:
        if any(c in u for c in claves):
            return zona
    return 'Por confirmar'


def tipo_base(t):
    t = norm(t)
    if 'galp' in t:
        return 'Local Industrial y Galpón'
    if 'terreno' in t:
        return 'Terreno y Parcela'
    if 'fondo' in t or 'negocio' in t:
        return 'Negocio'
    if 'local' in t or 'quiosco' in t:
        return 'Local Comercial'
    if 'apart' in t or t == 'ph':
        return 'Apartamento'
    if 'casa' in t or t in ('th', 'townhouse', 'villa', 'quinta'):
        return 'Casa o TownHouse'
    if 'oficina' in t or 'consultorio' in t:
        return 'Oficina'
    return 'Otro'


def codigo(c):
    """Normaliza 0156-801 y 0156-0801 al mismo código."""
    if not c or str(c).strip() in ('-', ''):
        return None
    m = re.match(r'(\d+)-(\d+)', str(c).strip())
    return f'{int(m.group(1)):04d}-{int(m.group(2)):04d}' if m else str(c).strip()


# Correcciones confirmadas por Eduardo (29-09-2026)
AGENTE = {'Enrique Castillejo': 'Enrique Oliveri'}
# Cierres de la planilla 2026 que quedaron con año 2025: si está en el Excel de 2026, es de 2026.
FECHA_ANIO_ARCHIVO = True
# Reservas de agosto 2026 que Eduardo confirmó como cerradas (no están en la hoja de ventas).
CIERRES_EXTRA = [
    dict(anio=2026, agente='José Castellanos', cod='0156-0866', tipo='Casa', urb='Castillejo, La Esperanza',
         op='Venta', fecha_cierre=None, fecha_reserva='2026-08-18', precio_cierre=100000,
         notas='Cierre confirmado por Eduardo. La fecha exacta del cierre está por confirmar: se muestra la de reserva.'),
    dict(anio=2026, agente='Enrique Oliveri', cod='0156-0864', tipo='Casa', urb='Castillejo, El Torreón',
         op='Venta', fecha_cierre=None, fecha_reserva='2026-08-12', precio_cierre=65000,
         notas='Alianza con Luis León. Cierre confirmado por Eduardo. La fecha exacta del cierre está por confirmar: se muestra la de reserva.'),
]


# Palabras que no distinguen un inmueble de otro (tipos y nombres de sectores grandes)
GENERICAS = set('''apartamento casa guatire guarenas miranda residencias residencial urbanizacion parcela centro
comercial castillejo casarapa nueva ciudad higuerote brion marques ingenio valle arriba altos parque villa villas
jardin jardines terrazas torres costa local'''.split())


def palabras(urb):
    return {w for w in re.findall(r'[a-z0-9]+', norm(urb)) if len(w) > 3 and w not in GENERICAS}


def parecidas(a, b):
    """Dos urbanizaciones son la misma si comparten alguna palabra significativa. Si una de las dos solo
    tiene palabras genéricas (por ejemplo "C.C. Castillejo"), basta con que compartan cualquier palabra."""
    pa, pb = palabras(a), palabras(b)
    if pa and pb:
        return bool(pa & pb)
    amplias = lambda u: {w for w in re.findall(r'[a-z0-9]+', norm(u)) if len(w) > 3 and w not in ('apartamento', 'casa')}
    return bool(amplias(a) & amplias(b))


def reserva_de(venta, reservas):
    """La reserva de una venta. Los códigos de oficina a veces se repiten entre inmuebles distintos:
    con código, la reserva debe tener el mismo código y una urbanización parecida; sin código, una
    urbanización parecida y el mismo precio final. Si hay varias, la última reserva antes del cierre."""
    c = codigo(venta['cod'])
    if c:
        cand = [r for r in reservas if codigo(r['cod']) == c and parecidas(r['urb'], venta['urb'])]
    else:
        cand = [r for r in reservas if not codigo(r['cod']) and parecidas(r['urb'], venta['urb']) and r['pfin'] == venta['pfin']]
    antes = [r for r in cand if r.get('freserva') and venta['fecha'] and r['freserva'] <= venta['fecha']]
    cand = antes or cand
    return max(cand, key=lambda r: r.get('freserva') or '') if cand else None


def fecha_txt(d):
    return str(d)[:10] if d else None


def cargar(anio):
    return json.load(open(RAIZ / f'datos/delta_cierres_{anio}.json'))


def captaciones():
    """Precio inicial y fecha de captación por código de oficina, de todas las hojas de captaciones."""
    out = {}  # código -> [(urb, precio, fecha)]
    for anio in ANIOS:
        wb = openpyxl.load_workbook(RAIZ / f'datos/originales/delta-productividad-captaciones-{anio}.xlsx', data_only=True)
        for hoja in wb.sheetnames:
            if not hoja.startswith('Captaciones Año'):
                continue
            for r in wb[hoja].iter_rows(values_only=True):
                c = codigo(r[2]) if len(r) > 10 else None
                if c and isinstance(r[10], (int, float)):
                    f = r[8]
                    f = f.date().isoformat() if isinstance(f, datetime.datetime) else None
                    out.setdefault(c, []).append(dict(urb=r[5], precio=float(r[10]), fecha=f))
    return out


def captacion_de(caps, cod, urb):
    cand = [x for x in caps.get(codigo(cod), []) if parecidas(x['urb'], urb)]
    return cand[0] if cand else {}


def construir():
    caps = captaciones()
    docs = []
    for anio in ANIOS:
        d = cargar(anio)
        # Las reservas del año y las del año anterior (una venta de enero puede venir de una reserva de diciembre)
        reservas = d['reservas'] + (cargar(anio - 1)['reservas'] if anio - 1 in ANIOS else [])
        for i, v in enumerate(d['ventas'], 1):
            c = codigo(v['cod'])
            r = reserva_de(v, reservas)
            op = 'Alquiler' if v['op'] == 'A' else 'Venta'
            revisar = []
            fecha = v['fecha']
            if fecha and FECHA_ANIO_ARCHIVO and int(fecha[:4]) != anio:
                fecha = f'{anio}{fecha[4:]}'
                revisar.append(f'En el Excel decía {v["fecha"]}; se corrigió al año {anio}.')
            pcierre = v['pfin']
            if r and r.get('pfin') and pcierre and op == 'Venta':
                if pcierre < 0.2 * r['pfin']:
                    revisar.append(f'En Ventas dice {pcierre:,.0f}, pero se reservó en {r["pfin"]:,.0f}. '
                                   f'Se usa el de la reserva. Por confirmar.')
                    pcierre = r['pfin']
                elif abs(pcierre - r['pfin']) > 1:
                    revisar.append(f'Se reservó en {r["pfin"]:,.0f} y se vendió en {pcierre:,.0f}. Por confirmar.')
            cap = captacion_de(caps, c, v['urb'])
            ppub = (r or {}).get('pini') or cap.get('precio')
            fpub = fecha_txt((r or {}).get('listada')) or cap.get('fecha')
            if fpub and fecha and fpub > fecha:
                revisar.append(f'La fecha de captación ({fpub}) es posterior al cierre. Por confirmar.')
                fpub = None
            if op == 'Alquiler' and ppub and pcierre and ppub > 20 * pcierre:
                ppub = None
            notas = [str(x) for x in (v.get('obs'), (r or {}).get('obs')) if x and str(x).strip()]
            ref = v.get('referido')
            docs.append(dict(
                doc_id=f'delta-{anio}-{i:03d}',
                fecha_cierre=fecha, fecha_reserva=fecha_txt((r or {}).get('freserva')), fecha_publicacion=fpub,
                zona=zona_de(v['urb']), sector=str(v['urb']).strip(), tipo=tipo_base(v['tipo']),
                tipo_original=str(v['tipo']).strip(), operacion=op,
                m2_construccion=None, m2_terreno=None,
                precio_publicado=ppub, precio_cierre=pcierre,
                oficina='RE/MAX Delta', agente=AGENTE.get(v['agente'], v['agente']),
                codigo_oficina=c, alianza_referido=' · '.join(filter(None, [*dict.fromkeys(notas), str(ref) if ref else None])) or None,
                forma_pago=None, revisar=' '.join(revisar) or None,
                fuente=f'Excel de productividad RE/MAX Delta {anio}', estado='por_confirmar', anio=anio,
                notas='', registrado_por='Amigo', registrado_en='2026-09-29'))
    for j, x in enumerate(CIERRES_EXTRA, 1):
        cap = captacion_de(caps, x['cod'], x['urb'])
        docs.append(dict(
            doc_id=f'delta-{x["anio"]}-extra-{j}', fecha_cierre=x['fecha_cierre'], fecha_reserva=x['fecha_reserva'],
            fecha_publicacion=cap.get('fecha'), zona=zona_de(x['urb']), sector=x['urb'], tipo=tipo_base(x['tipo']),
            tipo_original=x['tipo'], operacion=x['op'], m2_construccion=None, m2_terreno=None,
            precio_publicado=cap.get('precio'), precio_cierre=x['precio_cierre'], oficina='RE/MAX Delta',
            agente=x['agente'], codigo_oficina=x['cod'], alianza_referido=None, forma_pago=None,
            revisar='Falta la fecha exacta del cierre.', fuente='Confirmado por Eduardo (reserva en el Excel 2026)',
            estado='por_confirmar', anio=x['anio'], notas=x['notas'], registrado_por='Amigo', registrado_en='2026-09-29'))
    return docs


if __name__ == '__main__':
    docs = construir()
    SALIDA.mkdir(exist_ok=True)
    for f in SALIDA.glob('lote_*.json'):
        f.unlink()
    for n in range(0, len(docs), 50):
        lote = [dict(op='set', collection='cierres', doc_id=x.pop('doc_id'), data=x) for x in docs[n:n + 50]]
        json.dump(lote, open(SALIDA / f'lote_{n // 50 + 1}.json', 'w'), ensure_ascii=False, indent=1)
    print(f'{len(docs)} cierres en {(len(docs) + 49) // 50} lotes')
