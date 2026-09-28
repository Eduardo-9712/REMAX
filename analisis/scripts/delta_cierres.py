"""Lee el Excel de productividad de RE/MAX Delta (2024-2025), calcula rebajas y tiempos
de venta, y exporta reservas, ventas, puntas y captaciones a analisis/datos/delta_cierres_2025.json.
Uso: python3 analisis/scripts/delta_cierres.py  (necesita openpyxl)"""
import openpyxl,datetime,statistics as st,collections,json
wb=openpyxl.load_workbook('analisis/datos/originales/delta-productividad-captaciones-2025.xlsx',data_only=True)
def rows(name,hdr_row=3):
    ws=wb[name]; out=[]; mes=None
    for r in ws.iter_rows(min_row=hdr_row+1,values_only=True):
        if isinstance(r[0],str) and r[0].strip() and not r[1]: mes=r[0].strip(); continue
        if r[1]: out.append((mes,r))
    return out
def d(x):
    if isinstance(x,datetime.datetime): return x.date()
    if isinstance(x,str):
        try: return datetime.datetime.strptime(x.strip(),'%d/%m/%Y').date()
        except: return None
def num(x):
    return float(x) if isinstance(x,(int,float)) else None
# Reservas
res=[]
for mes,r in rows('Reservas'):
    res.append(dict(mes=mes,agente=r[1],cod=r[2],tipo=(r[4] or '').strip(),urb=r[5],exclu=r[6],op=r[7],listada=d(r[8]),pini=num(r[9]),freserva=d(r[10]),pfin=num(r[11]),reserva=num(r[12]),obs=r[15]))
ventas=[]
for mes,r in rows('Ventas - Alquileres'):
    ventas.append(dict(mes=mes,agente=r[1],cod=r[2],tipo=(r[4] or '').strip(),urb=r[5],exclu=r[6],op=r[7],fecha=d(r[8]),pfin=num(r[9]),referido=r[10],obs=r[11]))
puntas=[]
for mes,r in rows('Puntas'):
    puntas.append(dict(cod=r[2],tipo=(r[4] or '').strip(),urb=r[5],fecha=d(r[6]),pfin=num(r[7]),comision=num(r[8])))
print("reservas",len(res),"ventas",len(ventas),"puntas",len(puntas))
# descuento
desc=[];dias=[]
for x in res:
    if x['op']=='V' and x['pini'] and x['pfin']:
        p=(x['pfin']-x['pini'])/x['pini']*100; desc.append((p,x))
    if x['listada'] and x['freserva'] and x['freserva']>=x['listada']:
        dias.append(((x['freserva']-x['listada']).days,x))
ps=[p for p,_ in desc]
print(f"Ventas con precio inicial y final: {len(ps)}; mediana {st.median(ps):.1f}%, promedio {st.mean(ps):.1f}%; sin rebaja {sum(1 for p in ps if p>=0)}; min {min(ps):.1f}")
for p,x in sorted(desc,key=lambda t:t[0])[:8]: print(f"  {p:.1f}% {x['tipo']} {x['urb']} {x['pini']}->{x['pfin']}")
ds=[a for a,_ in dias]
print(f"Días hasta reserva: n={len(ds)} mediana {st.median(ds)} prom {st.mean(ds):.0f} min {min(ds)} max {max(ds)}")
bad=[x for x in res if x['listada'] and x['freserva'] and x['freserva']<x['listada']]
print("fechas incoherentes:",[(x['urb'],str(x['listada']),str(x['freserva'])) for x in bad])
# ventas 2025
v=[x for x in ventas if x['op']!='A' and x['pfin'] and x['pfin']>2000]
a=[x for x in ventas if x['op']=='A']
print("ventas 2025:",len(v),"alquileres:",len(a),"total registros:",len(ventas))
print("mediana precio venta:",st.median([x['pfin'] for x in v]), "rango",min(x['pfin'] for x in v),max(x['pfin'] for x in v))
bt=collections.defaultdict(list)
for x in v: bt[x['tipo'].replace('Apartamento ','Apartamento')].append(x['pfin'])
for k,l in bt.items(): print(f"  {k}: {len(l)} ventas, mediana {st.median(l)}")
print("alquileres:",[(x['tipo'],x['urb'],x['pfin']) for x in a])
print("con referido de otra oficina:",sum(1 for x in ventas if x['referido']), "alianzas:",sum(1 for x in ventas if x['obs'] and 'lianza' in str(x['obs'])))
print("raros ventas <2000 V:",[(x['tipo'],x['urb'],x['pfin'],x['op']) for x in ventas if x['op']!='A' and x['pfin'] and x['pfin']<=2000])
# comisiones
for x in puntas:
    if x['pfin'] and x['comision'] and x['pfin']>2000:
        pct=x['comision']/x['pfin']*100
        if abs(pct-5)>0.3: print("  comision no 5%:",x['urb'],x['pfin'],x['comision'],f"{pct:.1f}%")
# captaciones 2025
cap=[]
for mes,r in rows('Captaciones Año 2025'):
    cap.append(dict(mes=mes,tipo=(r[4] or '').strip(),urb=r[5],exclu=r[6],op=r[7],p=num(r[10])))
print("captaciones 2025:",len(cap),"exclusivas:",sum(1 for c in cap if c['exclu']=='S'),"venta:",sum(1 for c in cap if c['op']=='V'),"alquiler:",sum(1 for c in cap if c['op']=='A'))
print(collections.Counter(c['tipo'] for c in cap).most_common())
cap24=rows('Captaciones Año 2024'); print("captaciones 2024:",len(cap24))
json.dump(dict(reservas=res,ventas=ventas,puntas=puntas,captaciones_2025=cap),open('analisis/datos/delta_cierres_2025.json','w'),default=str,ensure_ascii=False,indent=1)
