"""Genera data/inmuebles.json con el levantamiento piloto (25-09-2026).

Cada inmueble lleva: datos comunes, `specs` (características propias del tipo),
`cal` (calificaciones 1-5 del analista) y `nota` (análisis escrito).
El puntaje final 0-100 lo calcula la aplicación, porque el componente de
precio/m² depende de los demás inmuebles comparables.
"""
import json, pathlib

HOY = "2026-09-25"
RAH = "https://rentahouse.com.ve/"
REG = []


def add(id, zona, tipo, subtipo, sector, titulo, precio, *, op="venta", m2c=None, m2t=None,
        hab=None, banos=None, pto=None, specs=None, fuente="Rent-A-House", codigo="", url="",
        cal=(3, 3, 3, 3, 3), nota="", desc="", estatus=None):
    u, e, r, l, d = cal
    if estatus is None:
        # Códigos RAH 25-/26- son publicaciones recientes; lo demás se confirma primero.
        estatus = "disponible" if codigo.startswith(("VE 25", "VE 26")) else "por_verificar"
    REG.append(dict(
        id=id, zona=zona, tipo=tipo, subtipo=subtipo, operacion=op, sector=sector,
        titulo=titulo, precio=precio, m2c=m2c, m2t=m2t, hab=hab, banos=banos, puestos=pto,
        specs=specs or {}, descripcion=desc, fuentes=[dict(nombre=fuente, codigo=codigo, url=url)],
        cal=dict(ubicacion=u, estado=e, rentabilidad=r, liquidez=l, documentacion=d),
        nota=nota, estatus=estatus, fecha_detectada=HOY, ultima_verificacion=HOY,
        historial=[dict(fecha=HOY, evento="Detectado en levantamiento piloto",
                        precio=precio, estatus=estatus)],
        agente="", contacto="", favorito=False,
    ))


ML_GUA = "https://listado.mercadolibre.com.ve/inmuebles/casas/venta/miranda/guatire/casas-baratas-en-guatire-estado-miranda"
RMX_GUA = "https://www.remax.com.ve/inmuebles/apartamento/venta?ubi=Guatire%2C+Zamora%2C+Miranda%2C+VEN"

# ───────────────────────────── GUATIRE ─────────────────────────────
Z = "guatire"
add("GTR-001", Z, "residencial", "Apartamento", "Frutas Condominio", "Apartamento 1 nivel en Frutas Condominio",
    90000, codigo="VE 25-1180", url=RAH + "apartamento_en_venta_en_guatire_en_frutas-condominio_rah-25-1180.html",
    cal=(4, 4, 3, 3, 3), nota="Precio alto para Guatire. Hace falta el m² para compararlo; urbanización cerrada de buena demanda.")
add("GTR-002", Z, "residencial", "Apartamento", "El Ingenio (Parque Habitad)", "Apartamento en obra gris, Parque Habitad El Ingenio",
    25000, m2c=68, hab=2, banos=1, specs={"estado_obra": "Obra gris"}, codigo="VE 21-18466",
    url=RAH + "apartamento_en_venta_en_guatire_en_parque-habitad-el-ingenio_rah-21-18466.html",
    cal=(4, 2, 4, 4, 3), nota="Entrada barata a El Ingenio (~$368/m²). Obra gris: sumar ~$8-12k de acabados. Bueno para comprar, terminar y alquilar o revender. Publicación de 2021: confirmar si sigue vigente.")
add("GTR-003", Z, "residencial", "Apartamento", "San Pedro", "Apartamento en Sector San Pedro",
    40000, codigo="VE 22-23025", url=RAH + "apartamento_en_venta_en_guatire_en_sector-san-pedro_rah-22-23025.html",
    cal=(3, 3, 3, 3, 3), nota="Faltan m² y distribución. Publicación de 2022: confirmar vigencia.")
add("GTR-004", Z, "residencial", "Townhouse", "Terrazas del Ingenio", "Townhouse dúplex en Terrazas del Ingenio",
    50000, m2c=100, m2t=100, hab=3, banos=3, specs={"niveles": "2"}, codigo="VE 24-15888",
    url=RAH + "townhouse_en_venta_en_guatire_en_terrazas-del-ingenio_rah-24-15888.html",
    cal=(4, 3, 3, 4, 3), nota="$500/m² en un townhouse con terreno propio. Producto muy buscado por familias; se vende rápido.")
add("GTR-005", Z, "residencial", "Casa", "Araira", "Casa de 2 niveles con anexo independiente, Araira",
    37000, m2c=500, hab=5, banos=5, pto=3, specs={"niveles": "2", "anexo": "Apartamento independiente con cocina"},
    codigo="VE 24-21415", url=RAH + "casa_en_venta_en_guatire_en_araira_rah-24-21415.html",
    cal=(2, 3, 4, 2, 3), nota="Solo $74/m² construido, muy por debajo del mercado. El anexo se puede alquilar aparte. Araira es periférica y de menor liquidez; revisar vía de acceso y servicios.")
add("GTR-006", Z, "residencial", "Casa", "Villas de Buenaventura", "Casa de 1 nivel amoblada, Villas de Buenaventura",
    115000, m2c=280, m2t=282, hab=3, banos=4, pto=3, specs={"niveles": "1", "amoblado": "Sí"}, codigo="VE 22-13663",
    url=RAH + "casa_en_venta_en_guatire_en_villas-de-buenaventura_rah-22-13663.html",
    cal=(5, 4, 2, 3, 3), nota="Producto premium de Guatire (~$411/m²). Para uso propio o plusvalía; poca rentabilidad por alquiler a este precio.")
add("GTR-007", Z, "residencial", "Casa", "El Ingenio", "Casa de 4 habitaciones en El Ingenio",
    43000, m2c=320, m2t=120, hab=4, banos=4, codigo="VE 21-8127",
    url=RAH + "casa_en_venta_en_guatire_en_el-ingenio-1_rah-21-8127.html",
    cal=(4, 3, 4, 4, 3), nota="$134/m² construido en El Ingenio es muy bajo. Por el tamaño se puede alquilar por habitaciones o por niveles. Publicación de 2021: confirmar vigencia y precio.")
add("GTR-008", Z, "residencial", "Casa", "Valle Arriba", "Casa de 3 niveles en urbanización cerrada, Valle Arriba",
    65000, specs={"niveles": "3", "agua": "5 pozos en la urbanización", "vigilancia": "Portones eléctricos"},
    codigo="VE 23-133", url=RAH + "casa_en_venta_en_guatire_en_valle-arriba_rah-23-133.html",
    cal=(4, 3, 3, 3, 3), nota="Punto fuerte: agua garantizada con 5 pozos. Faltan m² para compararla.")
add("GTR-009", Z, "residencial", "Casa", "Villas de Buenaventura", "Casa de varios niveles, Villas de Buenaventura",
    110000, specs={"niveles": "Varios"}, codigo="VE 22-14195",
    url=RAH + "casa_en_venta_en_guatire_en_villas-de-buenaventura_rah-22-14195.html",
    cal=(5, 3, 2, 3, 3), nota="Referencia de precio en Buenaventura. Faltan m².")
add("GTR-010", Z, "residencial", "Apartamento", "Las Rosas (Conj. El Mirador)", "Apartamento 3 habitaciones, Conj. Res. El Mirador",
    29000, m2c=63, hab=3, banos=1, pto=1, fuente="RE/MAX Venezuela", codigo="326701",
    url="https://www.remax.com.ve/inmuebles/apartamento/venta/apartamento-en-venta-las-rosas-mirador-guatire-326701",
    cal=(3, 3, 4, 4, 3), estatus="disponible",
    nota="$460/m². Tres habitaciones en 63 m², ideal para alquiler a familias. Buena liquidez por el precio.")
add("GTR-011", Z, "residencial", "Apartamento", "Castillejo (Jardines de Castillejo)", "Apartamento 2 habitaciones, Jardines de Castillejo",
    64000, m2c=67, hab=2, fuente="RE/MAX Venezuela", url=RMX_GUA,
    cal=(4, 4, 3, 3, 3), nota="~$955/m², de los más caros de la zona. Justificable solo si tiene acabados de lujo y buenas áreas comunes.")
add("GTR-012", Z, "residencial", "Apartamento", "San Pedro (Terrazas de San Pedro)", "Apartamento 2 habitaciones, Terrazas de San Pedro",
    30000, m2c=77, hab=2, fuente="RE/MAX Venezuela", url=RMX_GUA,
    cal=(3, 3, 4, 4, 3), nota="$390/m²: buen precio. En la misma urbanización se alquila en ~$430/mes (ver GTR-022), lo que da ~14-17% bruto anual si se alquila amoblado.")
add("GTR-013", Z, "residencial", "Apartamento", "La Sabana (Parque Residencial)", "Apartamento 3 habitaciones, Parque Residencial La Sabana",
    29000, m2c=95, hab=3, fuente="RE/MAX Venezuela", url=RMX_GUA,
    cal=(3, 3, 4, 4, 3), nota="$305/m², de los m² más baratos en apartamentos de Guatire. Buena opción de renta.")
add("GTR-014", Z, "galpon", "Galpón / Depósito", "Zona Industrial Inproceca", "Galpón divisible en 2 unidades, Inproceca",
    1000000, m2c=2895, banos=6, specs={"vigilancia": "Privada 24h, doble portón", "montacarga": "Sí",
                                          "oficinas": "Oficinas y sala de conferencias", "divisible": "2 galpones independientes"},
    codigo="VE 25-3085", url=RAH + "comercial_en_venta_en_guatire_en_guatire_rah-25-3085.html",
    cal=(4, 4, 4, 2, 3), nota="$345/m². Se puede dividir en dos galpones para alquilarlos por separado. Ticket alto: pocos compradores.")
add("GTR-015", Z, "galpon", "Galpón / Depósito", "Valle Arriba", "Galpón de 3.400 m², Valle Arriba",
    1800000, m2c=3400, banos=7, codigo="VE 26-4992", url=RAH + "comercial_en_venta_en_guatire_en_valle-arriba_rah-26-4992.html",
    cal=(3, 3, 3, 2, 3), nota="$529/m², caro frente a Inproceca y Terrinca. Negociable.")
add("GTR-016", Z, "galpon", "Industrial", "Guatire", "Inmueble industrial de 1.050 m²",
    850000, m2c=1050, banos=3, specs={"estacionamiento": "Techado"}, codigo="VE 25-13840",
    url=RAH + "comercial_en_venta_en_guatire_en_guatire_rah-25-13840.html",
    cal=(3, 3, 2, 2, 3), nota="$810/m²: muy por encima del resto de galpones. Solo tiene sentido si incluye maquinaria o un negocio en marcha.")
add("GTR-017", Z, "galpon", "Galpón", "Zona Industrial Terrinca", "Galpón de 1.259 m², Zona Industrial Terrinca",
    290000, m2c=1259, fuente="RIV Premium", url="https://rivinotinto.com/premiumcumana/detalle.php?id=24102",
    cal=(4, 3, 4, 3, 3), nota="$230/m², el mejor precio por m² de galpones en Guatire. Terrinca tiene buena salida a la autopista.")
add("GTR-018", Z, "terreno", "Industrial", "El Marqués", "Terreno industrial de 5.553 m² junto al Forum Guatire",
    225000, m2t=5553, specs={"zonificacion": "Industrial", "acceso": "Acceso inmediato a la autopista"}, codigo="VE 26-4321",
    url=RAH + "terreno_en_venta_en_guatire_en_el-marques_rah-26-4321.html",
    cal=(5, 3, 4, 4, 3), nota="$41/m² en una zona industrial con acceso a la autopista: muy por debajo del promedio de Guatire (~$97/m²). Oportunidad para desarrollar galpones.")
add("GTR-019", Z, "terreno", "Industrial", "Vega Arriba (Z.I.)", "Lote de 4.030 m², Zona Industrial Vega Arriba",
    445000, m2t=4030, specs={"zonificacion": "Industrial"}, fuente="ZonaVen", url="https://zonaven.com/venta-terrenos/guatire",
    cal=(4, 3, 3, 3, 3), nota="$110/m², en línea con el promedio del mercado.")
add("GTR-020", Z, "local", "Local comercial", "El Ingenio", "Local comercial en El Ingenio",
    35000, codigo="VE 26-17879", url=RAH + "comercial_en_venta_en_guatire_en_el-ingenio_rah-26-17879.html",
    cal=(4, 3, 4, 4, 3), nota="Local de entrada en la zona más poblada de Guatire. Faltan m²; en El Ingenio se alquilan locales en ~$1.500/mes (GTR-023).")
add("GTR-021", Z, "residencial", "Casa", "Villa Heroica", "Casa de 2 plantas, Villa Heroica",
    45000, m2c=200, hab=4, banos=4, specs={"niveles": "2"}, fuente="MercadoLibre", url=ML_GUA,
    cal=(3, 3, 3, 3, 3), nota="$225/m²: precio razonable para una casa de 4 habitaciones.")
add("GTR-022", Z, "residencial", "Apartamento", "San Pedro (Terrazas Altos de San Pedro)", "Apartamento amoblado en alquiler, Terrazas Altos de San Pedro",
    430, op="alquiler", hab=3, banos=2, pto=2, specs={"amoblado": "Sí, con aire acondicionado"}, codigo="VE 26-5133",
    url=RAH + "apartamento_en_alquiler_en_guatire_en_sector-san-pedro_rah-26-5133.html",
    cal=(3, 4, 3, 4, 3), nota="Sirve de referencia de renta en San Pedro: ~$430/mes amoblado con 3 habitaciones.")
add("GTR-023", Z, "local", "Local comercial", "El Ingenio", "Local comercial en alquiler, El Ingenio",
    1500, op="alquiler", codigo="VE 25-864", url=RAH + "comercial_en_alquiler_en_guatire_en_el-ingenio_rah-25-864.html",
    cal=(4, 3, 3, 3, 3), nota="Referencia de renta comercial en El Ingenio.")
add("GTR-024", Z, "terreno", "Comercial", "Guatire (centro)", "Terreno comercial en alquiler, centro de Guatire",
    1500, op="alquiler", specs={"uso": "Depósito, estacionamiento o comercio"}, codigo="VE 26-14751",
    url=RAH + "terreno_en_alquiler_en_guatire_en_guatire_rah-26-14751.html",
    cal=(4, 3, 3, 3, 3), nota="Sirve para estacionamiento o como patio de depósito.")
add("GTR-025", Z, "residencial", "Casa", "El Ingenio (La Muralla)", "Casa semi-amoblada, Urb. La Muralla",
    60000, m2c=150, hab=5, banos=4, specs={"amoblado": "Semi-amoblada"}, fuente="MercadoLibre", url=ML_GUA,
    cal=(4, 3, 3, 3, 3), nota="$400/m², en línea con El Ingenio. Tiene 5 habitaciones.")

# ───────────────────────────── GUARENAS ─────────────────────────────
Z = "guarenas"
ML_NC = "https://listado.mercadolibre.com.ve/inmuebles/apartamentos/venta/miranda/guarenas/nueva-casarapa/"
add("GRN-001", Z, "residencial", "Apartamento dúplex", "Los Girasoles", "Dúplex de 3 niveles con terraza y parrillera, Los Girasoles",
    20000, m2c=96, hab=2, banos=2, specs={"niveles": "3", "terraza": "Techada con parrillera"}, codigo="VE 25-8691",
    url=RAH + "apartamento_en_venta_en_guarenas_en_los-girasoles_rah-25-8691.html",
    cal=(3, 3, 4, 5, 3), nota="$208/m², en el piso del rango ($20k). Muy líquido para compradores primerizos o inversión de renta.")
add("GRN-002", Z, "residencial", "Apartamento", "Ciudad Casarapa", "Apartamento 3 habitaciones, Ciudad Casarapa",
    36000, hab=3, banos=2, codigo="VE 26-14693", url=RAH + "apartamento_en_venta_en_guarenas_en_ciudad-casarapa_rah-26-14693.html",
    cal=(3, 3, 3, 4, 3), nota="Faltan m². Precio medio para Casarapa.")
add("GRN-003", Z, "residencial", "Apartamento", "La Vaquera", "Apartamento en conjunto de baja densidad, La Vaquera",
    48000, hab=3, banos=2, pto=1, codigo="VE 26-19133", url=RAH + "apartamento_en_venta_en_guarenas_en_la-vaquera_rah-26-19133.html",
    cal=(3, 4, 3, 3, 3), nota="Conjunto exclusivo de baja densidad. Faltan m².")
add("GRN-004", Z, "residencial", "Casa", "Guarenas", "Casa de 1 nivel con jardín, 392 m²",
    50000, m2c=392, hab=5, banos=6, specs={"niveles": "1", "jardin": "Privado"}, codigo="VE 24-4024",
    url=RAH + "casa_en_venta_en_guarenas_en_guarenas_rah-24-4024.html",
    cal=(3, 3, 4, 3, 3), nota="$128/m²: mucho metraje por el precio. Se puede alquilar por habitaciones.")
add("GRN-005", Z, "residencial", "Apartamento", "Nueva Casarapa", "Apartamento 3 habitaciones, Nueva Casarapa",
    34000, m2c=74, hab=3, banos=2, fuente="MercadoLibre", url=ML_NC,
    cal=(3, 3, 4, 4, 3), nota="$459/m², en línea con el mercado.")
add("GRN-006", Z, "residencial", "Apartamento", "Nueva Casarapa", "Apartamento 4 habitaciones, 127 m², Nueva Casarapa",
    45000, m2c=127, hab=4, banos=3, fuente="MercadoLibre", url=ML_NC,
    cal=(3, 3, 4, 4, 3), nota="$354/m²: grande y barato por m². Buena opción para familias.")
add("GRN-007", Z, "galpon", "Galpón", "Zona Industrial del Este", "Galpón de 1.800 m² en 2 naves, Z.I. del Este",
    700000, m2c=1800, m2t=2500, specs={"naves": "2 comunicadas"}, fuente="BienesOnline",
    url="https://venezuela.bienesonline.com/buscar-galpon-zona-industrial-guarenas.php",
    cal=(4, 3, 3, 3, 3), nota="$389/m² de galpón.")
add("GRN-008", Z, "galpon", "Galpón / Depósito", "Zona Industrial Cloris", "Complejo industrial de más de 20.000 m²",
    2500000, m2c=20000, codigo="VE 26-14650", url=RAH + "comercial_en_venta_en_guarenas_en_guarenas_rah-26-14650.html",
    cal=(4, 3, 3, 1, 3), nota="$125/m², barato por m² pero es un ticket de $2,5M para muy pocos compradores. Aparece también en otros portales: posiblemente es el mismo inmueble.")
add("GRN-009", Z, "galpon", "Galpón / Depósito", "Los Naranjos", "Galpón en Los Naranjos",
    1770000, codigo="VE 24-20174", url=RAH + "comercial_en_venta_en_guarenas_en_los-naranjos_rah-24-20174.html",
    cal=(3, 3, 3, 2, 3), nota="Faltan m² para compararlo.")
add("GRN-010", Z, "terreno", "Comercial", "Av. Intercomunal Guarenas-Guatire", "Terreno comercial de 27.600 m² en la Intercomunal",
    3500000, m2t=27600, specs={"zonificacion": "Comercial"}, fuente="Tu Casa Nova Inmuebles",
    url="https://tucasanovainmuebles.com/terreno-venta-guarenas-guarenas/4538808",
    cal=(5, 3, 3, 2, 3), nota="$127/m² en el eje comercial más importante entre las dos ciudades. Para un desarrollador.")
add("GRN-011", Z, "local", "Edificio de uso mixto", "Guarenas (zona comercial)", "Edificio de 3 niveles: local + apartamentos + sótano",
    92500, m2c=650, m2t=126, pto=4, specs={"composicion": "Local en PB, apartamentos en niveles 2-3, terraza"}, codigo="VE 23-30863",
    url=RAH + "casa_en_venta_en_guarenas_en_guarenas_rah-23-30863.html",
    cal=(4, 3, 5, 3, 3), nota="$142/m² por un edificio que genera renta en tres partes (local + 2 aptos). Excelente para un inversionista de renta.")
add("GRN-012", Z, "local", "Edificio comercial", "Guarenas (centro)", "Edificio con local, clínica y apartamento en el centro",
    580000, m2c=1150, m2t=300, specs={"composicion": "Local, clínica, apartamento de 3 hab. y terraza"}, codigo="VE 23-33430",
    url=RAH + "casa_en_venta_en_guarenas_en_guarenas_rah-23-33430.html",
    cal=(5, 3, 4, 2, 3), nota="$504/m². Mucho tráfico peatonal y vehicular. Ticket alto.")
add("GRN-013", Z, "local", "Local comercial", "Guarenas", "Local en planta baja de 50 m² con vidriera",
    27000, m2c=50, pto=1, specs={"ubicacion": "Pie de calle", "vidriera": "Amplia"}, fuente="Inmobiliaria.com",
    url="https://venezuela.inmobiliaria.com/guarenas/locales-comerciales+venta/",
    cal=(4, 3, 4, 4, 3), nota="$540/m², a pie de calle y con mucho tráfico. Precio negociable en efectivo.")
add("GRN-014", Z, "local", "Local comercial", "Ruiz Pineda", "Local de 70 m² en alquiler, Ruiz Pineda",
    500, op="alquiler", m2c=70, codigo="VE 26-11653", url=RAH + "comercial_en_alquiler_en_guarenas_en_ruiz-pineda_rah-26-11653.html",
    cal=(3, 3, 3, 3, 3), nota="Referencia: ~$7/m² al mes.")
add("GRN-015", Z, "local", "Local comercial", "Guarenas", "Local comercial en alquiler",
    2700, op="alquiler", codigo="VE 24-22691", url=RAH + "comercial_en_alquiler_en_guarenas_en_guarenas_rah-24-22691.html",
    cal=(3, 3, 3, 3, 3), nota="Faltan m².")
add("GRN-016", Z, "galpon", "Galpón / Depósito", "Guarenas (zona industrial)", "Galpón en alquiler",
    10000, op="alquiler", codigo="VE 26-2870", url=RAH + "comercial_en_alquiler_en_guarenas_en_guarenas_rah-26-2870.html",
    cal=(3, 3, 3, 3, 3), nota="Referencia de renta industrial en Guarenas.")

# ─────────────────────────── COSTA MIRANDINA ───────────────────────────
Z = "costa"
add("CST-001", Z, "residencial", "Townhouse dúplex", "Higuerote (Ciudad Balneario)", "Townhouse vacacional con acceso al canal",
    24000, hab=2, banos=2, pto=1, specs={"vista": "Canales", "extras": "Parrillera, terraza, acceso al canal principal"},
    codigo="VE 23-16966", url=RAH + "townhouse_en_venta_en_higuerote_en_ciudad-balneario-higuerote_rah-23-16966.html",
    cal=(5, 3, 4, 4, 3), nota="Acceso al canal por $24k. Alta demanda de alquiler vacacional por temporadas.")
add("CST-002", Z, "local", "Local comercial", "Higuerote (C.C. Cabo Mall)", "Local de 67 m² en obra gris, Cabo Mall",
    68000, m2c=67, specs={"ubicacion": "Centro comercial", "estado_obra": "Obra gris"}, codigo="VE 23-27068",
    url=RAH + "comercial_en_venta_en_higuerote_en_higuerote_rah-23-27068.html",
    cal=(4, 2, 3, 3, 3), nota="$1.015/m² más acabados. Caro; conviene solo si el centro comercial tiene buena ocupación.")
add("CST-003", Z, "terreno", "Residencial multifamiliar (AR-5)", "Higuerote (Ciudad Balneario)", "Terreno de 1.400 m², AR-5, con proyecto incluido",
    120000, m2t=1400, specs={"zonificacion": "AR-5 multifamiliar", "topografia": "Plana", "proyecto": "Incluido con variables urbanas"},
    codigo="VE 26-17396", url=RAH + "terreno_en_venta_en_higuerote_en_ciudad-balneario-higuerote_rah-26-17396.html",
    cal=(5, 4, 4, 3, 4), nota="$86/m² con un proyecto multifamiliar ya listo: ahorra meses de trámites. Excelente para un desarrollador.")
add("CST-004", Z, "residencial", "Casa de playa", "Higuerote (Ciudad Balneario)", "Villa con muelle en el canal, 2 parcelas de 2.545 m²",
    120000, m2t=2545, hab=4, specs={"muelle": "Sí, en el canal", "anexo": "2 hab. + 1 baño", "extras": "2 cocinas, cuarto de bombas, árboles frutales"},
    codigo="VE 26-8656", url=RAH + "casa_en_venta_en_higuerote_en_ciudad-balneario-higuerote_rah-26-8656.html",
    cal=(5, 3, 4, 3, 3), nota="Solo el terreno de 2.545 m² con muelle vale el precio ($47/m²). Buena para alquiler vacacional o para subdividir.")
add("CST-005", Z, "local", "Local comercial", "Higuerote", "Local comercial en Higuerote",
    101000, codigo="VE 23-27069", url=RAH + "comercial_en_venta_en_higuerote_en_higuerote_rah-23-27069.html",
    cal=(4, 3, 3, 3, 3), nota="Faltan m².")
add("CST-006", Z, "local", "Local comercial", "Higuerote", "Local comercial en Higuerote",
    380000, codigo="VE 26-7204", url=RAH + "comercial_en_venta_en_higuerote_en_higuerote_rah-26-7204.html",
    cal=(4, 3, 3, 2, 3), nota="Ticket alto para la costa. Faltan m².")
add("CST-007", Z, "residencial", "Apartamento", "Higuerote (Agua Sal)", "Apartamento en Agua Sal",
    65000, codigo="VE 26-16221", url=RAH + "apartamento_en_venta_en_higuerote_en_agua-sal_rah-26-16221.html",
    cal=(4, 3, 3, 3, 3), nota="Faltan m².")
add("CST-008", Z, "residencial", "Apartamento", "Río Chico (Los Canales)", "Apartamento con terraza, vista al mar y al golf",
    30000, specs={"vista": "Mar, canales y golf", "areas_comunes": "Piscina, minigolf, parrilleras, churuatas"}, codigo="VE 22-11880",
    url=RAH + "apartamento_en_venta_en_rio-chico_en_los-canales-de-rio-chico_rah-22-11880.html",
    cal=(4, 3, 4, 3, 3), nota="Muy buenas áreas comunes para alquiler de fin de semana.")
add("CST-009", Z, "residencial", "Penthouse", "Río Chico (Los Canales)", "Penthouse renovado con terraza amplia",
    23000, specs={"estado": "Renovado", "extras": "2 aires acondicionados, nevera"}, codigo="VE 23-23931",
    url=RAH + "apartamento_en_venta_en_rio-chico_en_los-canales-de-rio-chico_rah-23-23931.html",
    cal=(4, 4, 4, 4, 3), nota="Penthouse renovado por $23k: entrada barata al mercado vacacional.")
add("CST-010", Z, "residencial", "Penthouse", "Río Chico (Los Canales)", "Penthouse de lujo con terraza panorámica",
    110000, specs={"extras": "Cocina con granito, A/A central", "areas_comunes": "Piscinas, minigolf de 9 hoyos, muelle"},
    codigo="VE 25-22672", url=RAH + "apartamento_en_venta_en_rio-chico_en_los-canales-de-rio-chico_rah-25-22672.html",
    cal=(4, 5, 3, 2, 3), nota="Producto premium de Los Canales. En Río Chico se consigue muy por debajo de este precio: de lujo, pero cara.")
add("CST-011", Z, "residencial", "Apartamento (PB)", "Río Chico (Los Canales)", "Apartamento en planta baja",
    80000, codigo="VE 24-9997", url=RAH + "apartamento_en_venta_en_rio-chico_en_los-canales-de-rio-chico_rah-24-9997.html",
    cal=(4, 3, 3, 3, 3), nota="Faltan m².")
add("CST-012", Z, "residencial", "Apartamento", "Tacarigua de la Laguna", "Apartamento 1 nivel, Tacarigua la Laguna",
    20000, codigo="VE 24-17600", url=RAH + "apartamento_en_venta_en_rio-chico_en_tacarigua-la-laguna_rah-24-17600.html",
    cal=(3, 3, 3, 3, 3), nota="Piso del rango. Faltan m².")
add("CST-013", Z, "terreno", "Lote", "Higuerote (Playa Cristal)", "Lote de terreno en Playa Cristal (MC-15-002)",
    290616, specs={"zonificacion": "Por confirmar"}, fuente="RIV", codigo="MC-15-002",
    url="https://riv.com.ve/lote-terreno-venta-playa-cristal-costa-mirandina/3429000",
    cal=(4, 3, 3, 2, 3), nota="Faltan m² para compararlo.")
add("CST-014", Z, "residencial", "Casa", "Carenero", "Casa de 3 habitaciones en Carenero",
    31000, m2c=104, hab=3, banos=2, fuente="MercadoLibre",
    url="https://listado.mercadolibre.com.ve/inmuebles/casas/casas-en-venta-carenero-higuerote",
    cal=(4, 3, 4, 4, 3), nota="$298/m², cerca de la marina de Carenero. Buen precio.")
add("CST-015", Z, "galpon", "Galpón comercial", "Tacarigua", "Galpón de 2.081 m² con 4 locales y 4 oficinas",
    None, m2c=2081, specs={"edificacion": "2 niveles, 4 locales con baño, 4 oficinas, depósito"}, fuente="Varios (buscador)",
    url="https://casa.mitula.com.ve/tacarigua-mamporal",
    cal=(3, 3, 4, 3, 3), estatus="por_verificar", nota="Precio no publicado. Hay que pedirlo: si se ofrece por debajo de ~$200/m² puede ser una oportunidad.")

out = pathlib.Path(__file__).resolve().parent.parent / "data" / "inmuebles.json"
out.write_text(json.dumps(REG, ensure_ascii=False, indent=1))
print(len(REG), "inmuebles ->", out)
