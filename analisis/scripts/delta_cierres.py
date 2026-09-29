"""Lee los Excel de productividad de RE/MAX Delta (uno por año), calcula rebajas y tiempos
de venta, y exporta reservas, ventas, puntas y captaciones a analisis/datos/delta_cierres_<año>.json.
Uso: python3 analisis/scripts/delta_cierres.py  (necesita openpyxl)

Las columnas se buscan por su título, porque cambian de un año a otro (en 2026 la hoja de ventas
ya no trae la columna A / V). Si falta, un cierre de menos de USD 3.000 se toma como alquiler."""
import collections
import datetime
import json
import statistics as st
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parents[1]
ARCHIVOS = {
    2025: RAIZ / 'datos/originales/delta-productividad-captaciones-2025.xlsx',
    2026: RAIZ / 'datos/originales/delta-productividad-captaciones-2026.xlsx',
}
TOPE_ALQUILER = 3000  # por debajo de esto, sin columna A / V, es un canon


def fecha(x):
    if isinstance(x, datetime.datetime):
        return x.date()
    if isinstance(x, str):
        try:
            return datetime.datetime.strptime(x.strip(), '%d/%m/%Y').date()
        except ValueError:
            return None


def num(x):
    return float(x) if isinstance(x, (int, float)) else None


def filas(wb, hoja):
    """Devuelve dicts {titulo_columna: valor} con el mes al que pertenece cada fila."""
    ws = wb[hoja]
    todas = list(ws.iter_rows(values_only=True))
    i = next(i for i, r in enumerate(todas) if r and any(str(c).strip() == 'Agente' for c in r if c))
    cab = [str(c).strip() if c else '' for c in todas[i]]
    out, mes = [], None
    for r in todas[i + 1:]:
        if isinstance(r[0], str) and r[0].strip() and not r[1]:
            mes = r[0].strip()
            continue
        if r[1]:
            d = {cab[j]: r[j] for j in range(len(cab)) if cab[j]}
            d['mes'] = mes
            out.append(d)
    return out


def col(d, *nombres):
    for k, v in d.items():
        if any(k.startswith(n) for n in nombres):
            return v


def operacion(d, precio):
    op = col(d, 'A / V')
    if op in ('A', 'V'):
        return op
    return 'A' if precio is not None and precio < TOPE_ALQUILER else 'V'


def procesar(anio, ruta):
    wb = openpyxl.load_workbook(ruta, data_only=True)
    res = []
    for d in filas(wb, 'Reservas'):
        pfin = num(col(d, 'Precio Final'))
        res.append(dict(mes=d['mes'], agente=d['Agente'], cod=d['Código Oficina'],
                        tipo=(d['Tipo de Inmueble'] or '').strip(), urb=d['Urbanización'],
                        exclu=col(d, 'Exclu'), op=operacion(d, pfin), listada=fecha(col(d, 'Fecha Listada')),
                        pini=num(col(d, 'Precio Inicial')), freserva=fecha(col(d, 'Fecha de Reserva')),
                        pfin=pfin, reserva=num(col(d, 'Monto de la Reserva')), obs=col(d, 'Observaciones')))
    ventas = []
    for d in filas(wb, 'Ventas - Alquileres'):
        pfin = num(col(d, 'Precio Final'))
        ventas.append(dict(mes=d['mes'], agente=d['Agente'], cod=d['Código Oficina'],
                           tipo=(d['Tipo de Inmueble'] or '').strip(), urb=d['Urbanización'],
                           op=operacion(d, pfin), fecha=fecha(col(d, 'Fecha de Venta')), pfin=pfin,
                           referido=col(d, 'REFERIDO', 'Referido'), obs=col(d, 'Observaciones')))
    puntas = [dict(cod=d['Código Oficina'], tipo=(d['Tipo de Inmueble'] or '').strip(), urb=d['Urbanización'],
                   fecha=fecha(col(d, 'Fecha de Venta')), pfin=num(col(d, 'Precio Final')),
                   comision=num(col(d, 'Comisión')))
              for d in filas(wb, 'Puntas')]
    cap = [dict(mes=d['mes'], tipo=(d['Tipo de Inmueble'] or '').strip(), urb=d['Urbanización'],
                exclu=col(d, 'Exclu'), op=col(d, 'A / V'), p=num(col(d, 'Precio Inicial')))
           for d in filas(wb, f'Captaciones Año {anio}') if d.get('Tipo de Inmueble') != 'Tipo de Inmueble']

    print(f'\n===== {anio}: reservas {len(res)}, cierres {len(ventas)}, puntas {len(puntas)}, captaciones {len(cap)}')
    desc = [((x['pfin'] - x['pini']) / x['pini'] * 100, x) for x in res
            if x['op'] == 'V' and x['pini'] and x['pfin'] and x['pini'] > TOPE_ALQUILER]
    ps = [p for p, _ in desc]
    if ps:
        print(f'Rebaja (n={len(ps)}): mediana {st.median(ps):.1f} %, promedio {st.mean(ps):.1f} %, '
              f'sin rebaja {sum(p >= 0 for p in ps)}, por encima {sum(p > 0 for p in ps)}')
        for p, x in sorted(desc, key=lambda t: t[0])[:5]:
            print(f"  {p:.1f} % {x['tipo']} {x['urb']} {x['pini']:.0f} -> {x['pfin']:.0f}")
    ds = [(x['freserva'] - x['listada']).days for x in res
          if x['listada'] and x['freserva'] and x['freserva'] >= x['listada']]
    if ds:
        print(f'Días hasta reserva (n={len(ds)}): mediana {st.median(ds)}, promedio {st.mean(ds):.0f}')
    malas = [(x['urb'], str(x['listada']), str(x['freserva'])) for x in res
             if x['listada'] and x['freserva'] and x['freserva'] < x['listada']]
    print('Reserva antes que la captación:', malas)
    v = [x for x in ventas if x['op'] == 'V' and x['pfin']]
    a = [x for x in ventas if x['op'] == 'A']
    print(f'Ventas {len(v)}, alquileres {len(a)}; mediana venta {st.median(x["pfin"] for x in v):.0f}, '
          f'rango {min(x["pfin"] for x in v):.0f}-{max(x["pfin"] for x in v):.0f}, '
          f'monto total {sum(x["pfin"] for x in v):.0f}')
    por_tipo = collections.defaultdict(list)
    for x in v:
        por_tipo[x['tipo'].title()].append(x['pfin'])
    for k, l in sorted(por_tipo.items(), key=lambda t: -len(t[1])):
        print(f'  {k}: {len(l)}, mediana {st.median(l):.0f}')
    print('Alianzas:', sum(1 for x in ventas if x['obs'] and 'lianza' in str(x['obs'])))
    fuera = [(x['urb'], str(x['fecha'])) for x in ventas if x['fecha'] and x['fecha'].year != anio]
    print('Fecha de cierre de otro año:', fuera)
    print(f"Captaciones: exclusivas {sum(c['exclu'] == 'S' for c in cap)}, venta {sum(c['op'] == 'V' for c in cap)}, "
          f"alquiler {sum(c['op'] == 'A' for c in cap)}")
    print(collections.Counter(c['tipo'].title() for c in cap).most_common(12))
    salida = RAIZ / f'datos/delta_cierres_{anio}.json'
    json.dump(dict(reservas=res, ventas=ventas, puntas=puntas, **{f'captaciones_{anio}': cap}),
              open(salida, 'w'), default=str, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    for anio, ruta in ARCHIVOS.items():
        procesar(anio, ruta)
