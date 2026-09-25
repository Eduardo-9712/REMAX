"""Genera data/inmuebles.json: levantamiento piloto SOLO con RE/MAX Venezuela y MercadoLibre.

Cada inmueble tiene el enlace directo a su publicación (no a una página de búsqueda).
Cuando el buscador no mostró el precio, `precio` queda en None y el estatus en
`por_verificar`: el precio se completa al abrir la publicación.
Solo se anotan habitaciones, baños y m² que la publicación dice explícitamente.
`verificado=False` hasta que alguien confirme los datos en la página del anuncio.
"""
import json, pathlib

HOY = "2026-09-25"
REG = []
RMX = "https://www.remax.com.ve/inmuebles/"


def add(id, zona, tipo, subtipo, sector, titulo, precio, url, *, op="venta", m2c=None, m2t=None,
        hab=None, banos=None, pto=None, specs=None, cal=(3, 3, 3, 3, 3), nota="", estatus=None):
    fuente = "RE/MAX Venezuela" if "remax.com.ve" in url else "MercadoLibre"
    codigo = url.rstrip("/").split("-")[-1] if fuente.startswith("RE/MAX") else url.split("/")[-1].split("-")[0] + "-" + url.split("/")[-1].split("-")[1]
    if estatus is None:
        # Nada se marca Disponible hasta confirmarlo en la publicación.
        estatus = "por_verificar"
    u, e, r, l, d = cal
    REG.append(dict(
        id=id, zona=zona, tipo=tipo, subtipo=subtipo, operacion=op, sector=sector, titulo=titulo,
        precio=precio, m2c=m2c, m2t=m2t, hab=hab, banos=banos, puestos=pto, specs=specs or {},
        descripcion="", fuentes=[dict(nombre=fuente, codigo=codigo, url=url)],
        cal=dict(ubicacion=u, estado=e, rentabilidad=r, liquidez=l, documentacion=d),
        nota=nota, estatus=estatus, fecha_detectada=HOY, ultima_verificacion=HOY,
        historial=[dict(fecha=HOY, evento="Detectado en levantamiento piloto (RE/MAX y MercadoLibre)",
                        precio=precio, estatus=estatus)],
        agente="", contacto="", favorito=False,
        verificado=False))


FALTA = "Falta el precio: ábrelo y complétalo en la ficha."

# ───────────────────────────── GUATIRE ─────────────────────────────
Z = "guatire"
add("GTR-001", Z, "residencial", "Apartamento", "Las Rosas (Conj. El Mirador)", "Apartamento PB de 3 habitaciones, Conj. Res. El Mirador",
    29000, RMX + "apartamento/venta/apartamento-en-venta-las-rosas-mirador-guatire-326701",
    m2c=63, hab=3, banos=1, pto=1, specs={"piso": "Planta baja"}, cal=(3, 3, 4, 4, 3),
    nota="$460/m². Tres habitaciones en 63 m², ideal para alquilar a una familia. Precio de entrada con buena liquidez.")
add("GTR-002", Z, "residencial", "Apartamento", "Las Acacias", "Apartamento piso 3, Conj. Res. Las Acacias",
    None, RMX + "apartamento/venta/venta-de-apartamento-piso-3-conj-resid-las-acacias-guatire-edo-miranda-262038",
    m2c=62, hab=2, banos=2, pto=1, specs={"piso": "3", "extras": "Cocina empotrada con granito, balcón"}, nota=FALTA)
add("GTR-003", Z, "residencial", "Apartamento", "Frutas Condominio", "Apartamento en Frutas Condominio",
    None, RMX + "apartamento/venta/apartamento-en-venta-guatire-frutas-condominio-318522", cal=(4, 3, 3, 3, 3), nota=FALTA)
add("GTR-004", Z, "residencial", "Apartamento", "Plaza Oro", "Apartamento en Plaza Oro",
    None, RMX + "apartamento/venta/venta-de-apartamento-plaza-oro-guatire-293243", cal=(4, 3, 3, 3, 3), nota=FALTA)
add("GTR-005", Z, "residencial", "Casa", "Castillejo (Urb. Castejón)", "Casa de 13 habitaciones y 10 baños, Urb. Castejón",
    75000, RMX + "casa-o-townhouse/venta/casa-en-venta-urbanizacion-castejon-guatire-316583",
    hab=13, banos=10, pto=3, specs={"vigilancia": "Privada 24/7", "estacionamiento": "Techado, 3 vehículos"},
    cal=(4, 3, 5, 2, 3), nota="$5.800 por habitación: sirve para alquilar por habitaciones, como residencia estudiantil o posada. Pocos compradores por el tamaño. Falta el m².")
add("GTR-006", Z, "residencial", "Casa", "El Marqués (Canaima II)", "Casa de 2 habitaciones en Parque Residencial Canaima II",
    55000, RMX + "casa-o-townhouse/venta/venta-de-casa-en-canaima-ii-sector-el-marques-guatire-328433",
    m2c=77, m2t=193, hab=2, banos=1, specs={"antiguedad": "14 años", "estado_obra": "Cocina al 70%, baño auxiliar en obra"},
    cal=(3, 2, 2, 3, 3), nota="$714/m² construido, caro para una casa con acabados pendientes. El valor está en los 193 m² de terreno para ampliarla.")
add("GTR-007", Z, "residencial", "Casa", "La Sabana (Canaima II)", "Casa en obra gris con adelanto, Canaima II",
    None, RMX + "casa-o-townhouse/venta/venta-casa-obra-gris-con-adelanto-canaima-ii-la-sabana-guatire-venezuela-309727",
    m2c=167, specs={"estado_obra": "Obra gris con adelanto, piso elevado, cableado 220V", "estacionamiento": "Techado"},
    cal=(3, 2, 3, 3, 3), nota=FALTA + " Si sale por debajo de ~$200/m², es buena para terminar y revender.")
add("GTR-008", Z, "residencial", "Casa multifamiliar", "Valle Arriba (Ginebra)", "Casa de 3 niveles con 3 anexos para alquilar, Ginebra",
    80000, RMX + "casa-o-townhouse/venta/casa-en-venta-ginebra-en-valle-arriba-guatire-326594",
    m2c=480, hab=7, banos=7, specs={"niveles": "3", "anexo": "3 anexos con entrada independiente", "agua": "Constante + tanque de 2.000 L",
                                     "extras": "Terraza techada con parrillera"},
    cal=(4, 4, 5, 3, 3), nota="$167/m² y 3 anexos que generan renta desde el primer día. De las mejores opciones para un inversionista de renta en Guatire.")
add("GTR-009", Z, "residencial", "Townhouse", "Valle Arriba (San Antonio)", "Townhouse de 5 habitaciones, Conj. Res. San Antonio",
    46000, RMX + "casa-o-townhouse/venta/casa-en-venta-en-urbanizacion-san-antonio-valle-arriba-323380",
    hab=5, banos=5, cal=(4, 3, 4, 4, 3), nota="$9.200 por habitación en Valle Arriba, buen precio. Falta el m².")
add("GTR-010", Z, "residencial", "Apartamento", "Valle Arriba (Las Bonitas II)", "Apartamento piso 2, Conj. Res. Las Bonitas II",
    None, RMX + "apartamento/venta/venta-apartamento-piso-2-urb-valle-arriba-conj-resid-las-bonitas-ii-guatire-252320",
    specs={"piso": "2"}, nota=FALTA)
add("GTR-011", Z, "residencial", "Casa", "Villas de Buenaventura", "Casa en Villas de Buenaventura",
    None, RMX + "casa-o-townhouse/venta/casa-en-venta-en-villas-de-buenaventura-guarenas-276138",
    cal=(5, 3, 2, 3, 3), nota=FALTA + " El anuncio dice Guarenas, pero Villas de Buenaventura está en Guatire.")
add("GTR-012", Z, "residencial", "Apartamento", "El Marqués", "Apartamento remodelado de 3 habitaciones, El Marqués",
    None, "https://apartamento.mercadolibre.com.ve/MLV-733171698-apartamento-en-venta-el-marques-guatire-_JM",
    m2c=62.51, hab=3, banos=1, pto=1, specs={"piso": "1", "estado_obra": "Cocina y baño remodelados", "agua": "Constante",
                                                "extras": "2 split + 1 aire de ventana, gas directo, portón eléctrico"},
    cal=(3, 4, 4, 4, 3), nota=FALTA)
add("GTR-013", Z, "residencial", "Apartamento", "Buena Vista (El Ingenio)", "Apartamento de 2 habitaciones, Buena Vista",
    None, "https://apartamento.mercadolibre.com.ve/MLV-730369349-invalmhouse-inmobiliaria-apartamento-en-venta-buena-vista-sector-buena-vista-guatire-_JM",
    m2c=36, hab=2, banos=1, pto=1, cal=(3, 3, 4, 4, 3), nota=FALTA + " Pequeño (36 m²), de alquiler fácil.")
add("GTR-014", Z, "residencial", "Apartamento", "Castillejo (Plaza Oro)", "Apartamento remodelado con piscina, Plaza Oro",
    None, "https://casa.mercadolibre.com.ve/MLV-729888333-guatire-castillejo-en-venta-apto-full-remodelado-todo-nuevo-con-piscina-vigilancia-privada-24-horas-plaza-oro-guatire-plaza-cerca-de-transporte-publico-y-otras-comodidades-_JM",
    m2c=73, hab=2, banos=2, pto=2, specs={"estado_obra": "Remodelado completo", "vigilancia": "Privada 24h",
                                           "areas_comunes": "Piscina, parque infantil, salón de fiestas"},
    cal=(4, 5, 4, 4, 3), nota=FALTA)
add("GTR-015", Z, "residencial", "Apartamento", "Valle Grande", "Apartamento con aire central, Valle Grande",
    None, "https://apartamento.mercadolibre.com.ve/MLV-716677964-venta-apt-guatire-urbvalle-grande-inf-msfdavarela-04241045413-_JM",
    m2c=64, hab=2, banos=2, specs={"extras": "Cocina equipada, aire acondicionado central"}, nota=FALTA)
add("GTR-016", Z, "residencial", "Apartamento", "Castillejo (Guatire Plaza III)", "Apartamento en Guatire Plaza III, Edif. Gamma",
    None, "https://apartamento.mercadolibre.com.ve/MLV-783459176-apartamento-en-venta-conj-residencial-guatire-plaza-iii-edif-gamma-_JM",
    cal=(4, 3, 3, 3, 3), nota=FALTA)
add("GTR-017", Z, "residencial", "Apartamento", "San Pedro (Terrazas Altos de San Pedro)", "Apartamento en Terrazas Altos de San Pedro",
    None, "https://apartamento.mercadolibre.com.ve/MLV-827398382-apartamento-en-terrazas-altos-de-san-pedro-guatire-luis-infante-24-20838-_JM",
    nota=FALTA)
add("GTR-018", Z, "residencial", "Casa", "El Encantado (Av. Intercomunal)", "Casa ampliada a 180 m² en conjunto con piscina, El Encantado",
    None, "https://casa.mercadolibre.com.ve/MLV-707028051-casa-en-venta-el-encantado-guatire-guarenas-_JM",
    m2c=180, hab=4, banos=3, specs={"agua": "Tanque subterráneo con bomba", "vigilancia": "24h con cámaras", "areas_comunes": "Piscina",
                                     "extras": "Ampliada de 90 a 180 m², 4 habitaciones + 1 estudio"},
    cal=(3, 4, 4, 3, 3), nota=FALTA)
add("GTR-019", Z, "residencial", "Casa", "Casco central (Calle 9 de Diciembre)", "Casa sobre terreno de 400 m², Calle 9 de Diciembre",
    90000, "https://casa.mercadolibre.com.ve/MLV-820636178-casa-en-venta-400m-calle-9-de-diciembre-guatire-_JM",
    m2t=400, banos=2, specs={"frente_fondo": "8,60 × 39,44 m", "estacionamiento": "Sí"}, cal=(4, 2, 3, 3, 3),
    nota="Confirmar el m²: el anuncio dice 400 m², pero 8,60 × 39,44 m da 339 m². $225/m² de terreno en pleno centro. El valor está en el lote para un desarrollo comercial. Hay otra publicación del mismo lote como terreno (MLV-816339772).")
add("GTR-020", Z, "residencial", "Casa", "Las Rosas (Los Pinos)", "Casa remodelada en Parque Residencial Los Pinos",
    None, "https://casa.mercadolibre.com.ve/MLV-729553331-se-vende-hermosa-casa-en-la-urbanizacion-los-pinos-guatire-_JM",
    m2c=82, m2t=73, hab=3, banos=2, pto=1, specs={"niveles": "2 + ático", "vigilancia": "24h", "areas_comunes": "Piscina"},
    cal=(3, 5, 4, 4, 3), nota=FALTA)
add("GTR-021", Z, "residencial", "Casa", "Valle Arriba (Ginebra)", "Casa de 2 niveles con 4 puestos, Conj. Res. Ginebra",
    None, "https://casa.mercadolibre.com.ve/MLV-729590025-invalmhouse-inmobiliaria-casa-en-venta-conjunto-residencial-ginebra-valle-arriba-guatire-estado-miranda-_JM",
    m2c=174, hab=7, pto=4, specs={"niveles": "2", "extras": "Patio interno"}, cal=(4, 3, 4, 3, 3), nota=FALTA)
add("GTR-022", Z, "residencial", "Townhouse", "El Refugio", "Townhouse de 2 niveles con piscina, Conj. Res. El Refugio",
    None, "https://casa.mercadolibre.com.ve/MLV-831373482-venta-de-townhouse-conj-resid-el-refugio-frente-a-corpoelec-guatire-_JM",
    hab=4, banos=3, pto=2, specs={"niveles": "2", "vigilancia": "Privada 24h", "areas_comunes": "Piscina, salón de fiestas"},
    cal=(3, 4, 3, 4, 3), nota=FALTA)
add("GTR-023", Z, "residencial", "Casa", "La Rosa (Colinas de Guatire)", "Casa en Urb. La Rosa, Colinas de Guatire",
    None, "https://casa.mercadolibre.com.ve/MLV-905928642-casa-en-venta-urb-la-rosa-colinas-de-guatire-yh-_JM", nota=FALTA)
add("GTR-024", Z, "terreno", "Urbano", "El Ingenio (Las Margaritas)", "Parcela plana en Urb. Las Margaritas, El Ingenio",
    None, RMX + "terreno-y-parcela/venta/venta-de-terreno-urb-las-margaritas-el-ingenio-guatire-309793",
    specs={"topografia": "Plana, lista para construir"}, cal=(4, 3, 3, 3, 3), nota=FALTA + " Confirmar el m² en la publicación.")
add("GTR-025", Z, "galpon", "Complejo de galpones", "Guatire", "Complejo de 6 galpones industriales (≈6.250 m²)",
    2800000, "https://inmueble.mercadolibre.com.ve/MLV-915562570-24-27672-importante-complejo-de-galpones-industriales-ubicado-en-guatire-_JM",
    m2c=6250, specs={"divisible": "6 galpones: 600, 1.750, 1.800, 1.500, 300 y 300 m²"}, cal=(4, 3, 4, 2, 3),
    nota="$448/m². Se puede alquilar por galpón. Hay una segunda publicación del mismo inmueble (MLV-968371698).")
add("GTR-026", Z, "galpon", "Galpón", "Calle Ramón Alfonso Blanco", "Galpón de 800 m² con caseta de vigilancia",
    None, "https://inmueble.mercadolibre.com.ve/MLV-819438588-en-venta-galpon-guatire-800mts2-_JM",
    m2t=800, specs={"electricidad": "Trifásica", "vigilancia": "Caseta y muro perimetral", "edificacion": "Parcialmente techado"},
    cal=(3, 3, 3, 3, 3), nota=FALTA)
add("GTR-027", Z, "local", "Local comercial", "Casco central (Calle 9 de Diciembre)", "Local de ~150 m² en obra gris, Calle 9 de Diciembre",
    None, RMX + "local-comercial/venta/en-venta-local-en-la-calle-9-de-diciembre-de-guatire-305412",
    m2c=150, specs={"ubicacion": "Pie de calle, cerca de la avenida principal", "estado_obra": "Obra gris con adelantos"},
    cal=(4, 2, 4, 3, 3), nota=FALTA)
add("GTR-028", Z, "local", "Local comercial", "Buenaventura (C.C. Buenaventura)", "Local de 144 m² en alquiler, C.C. Buenaventura",
    None, RMX + "local-comercial/alquiler/local-comercial-en-alquiler-en-el-cc-buenaventura-309808", op="alquiler",
    m2c=144, specs={"ubicacion": "Centro comercial, Av. Intercomunal"}, nota=FALTA)
add("GTR-029", Z, "local", "Local comercial", "Las Barrancas (Edif. Compro)", "Local de 28 m² + terraza de 20 m² en alquiler, Edif. Compro",
    300, RMX + "local-comercial/alquiler/alquiler-de-local-68-mtrs2-mezz-m8-edif-compro-sector-las-barrancas-guatire-edo-miranda-321695",
    op="alquiler", m2c=28, specs={"nivel": "Mezzanina M8", "extras": "Terraza de 20 m²"},
    nota="Referencia: ~$11/m² al mes en la Carretera Nacional.")

# ───────────────────────────── GUARENAS ─────────────────────────────
Z = "guarenas"
add("GRN-001", Z, "residencial", "Apartamento", "Los Naranjos", "Apartamento de 4 habitaciones, Los Naranjos",
    35000, RMX + "apartamento/venta/apartamento-en-guarenas-los-naranjos-323240",
    m2c=76, hab=4, banos=1, cal=(3, 3, 4, 4, 3), nota="$461/m². Cuatro habitaciones por $35k: bueno para alquilar por habitaciones.")
add("GRN-002", Z, "residencial", "Apartamento", "Terrazas del Este", "Apartamento amoblado de 55 m², Terrazas del Este",
    37500, RMX + "apartamento/venta/apartamento-en-venta-en-terrazas-del-este-guarenas-55-m-amoblado-341692",
    m2c=55, hab=2, banos=1, pto=2, specs={"piso": "3", "amoblado": "Sí, listo para mudarse",
                                          "areas_comunes": "Gas directo, polideportivo, vigilancia privada"},
    cal=(3, 4, 4, 4, 3), nota="$682/m², caro por m² porque incluye muebles. En el mismo conjunto hay apartamentos de 75 m² por ~$20-21k.")
add("GRN-003", Z, "residencial", "Apartamento", "Terrazas del Este", "Apartamento en Terrazas del Este",
    None, RMX + "apartamento/venta/terrazas-del-este-335634", nota=FALTA + " En el conjunto se publican de 74-77 m² entre $20.000 y $40.000.")
add("GRN-004", Z, "residencial", "Apartamento", "Ciudad Casarapa", "Apartamento en Ciudad Casarapa",
    None, RMX + "apartamento/venta/apartamento-en-venta-ciudad-casarapa-guarenas-320442", nota=FALTA)
add("GRN-005", Z, "residencial", "Apartamento", "Nueva Casarapa (El Trapiche)", "Apartamento en Nueva Casarapa, El Trapiche",
    None, "https://apartamento.mercadolibre.com.ve/MLV-739178125-apartamento-venta-nueva-casarapa-el-trapiche-guarenas-mls-23-21855-_JM",
    nota=FALTA + " En la zona se publican de 74-83 m² entre $14.500 y $29.000.")
add("GRN-006", Z, "residencial", "Apartamento", "Nueva Casarapa (El Trapiche)", "Apartamento en Nueva Casarapa, El Trapiche",
    None, "https://apartamento.mercadolibre.com.ve/MLV-714314441-apartamento-en-nueva-casarapa-el-trapiche-_JM", nota=FALTA)
add("GRN-007", Z, "residencial", "Apartamento", "Guarenas (cerca del Forum)", "Apartamento cerca del Forum",
    None, "https://apartamento.mercadolibre.com.ve/MLV-841865630-venta-de-apartamento-en-guarenas-cerca-del-forum-_JM", nota=FALTA)
add("GRN-008", Z, "residencial", "Apartamento", "La Vaquera", "Apartamento en conjunto cerrado con piscina, La Vaquera",
    None, "https://apartamento.mercadolibre.com.ve/MLV-831979096-apartamento-venta-la-vaquera-guarenas-ar-mls-24-743-_JM",
    pto=2, specs={"vigilancia": "24h", "areas_comunes": "Piscina, caminerías"}, cal=(3, 4, 3, 3, 3), nota=FALTA)
add("GRN-009", Z, "residencial", "Apartamento", "Oropeza Castillo", "Apartamento en Oropeza Castillo",
    None, "https://apartamento.mercadolibre.com.ve/MLV-718519991-apartamento-en-venta-guarenas-oropeza-castillo-_JM", nota=FALTA)
add("GRN-010", Z, "residencial", "Apartamento", "Terrazas de Vicente Emilio Sojo", "Apartamento en Terrazas de Vicente Emilio Sojo",
    None, "https://apartamento.mercadolibre.com.ve/MLV-724825858-apartamento-en-venta-terrazas-de-vicente-emilio-sojo-guarenas-_JM", nota=FALTA)
add("GRN-011", Z, "residencial", "Apartamento", "El Calvario", "Apartamento de 3 habitaciones, El Calvario",
    None, "https://apartamento.mercadolibre.com.ve/MLV-826783512-se-vende-un-apartamento-en-guarenas-el-calvario-_JM",
    hab=3, banos=2, pto=1, nota=FALTA)
add("GRN-012", Z, "residencial", "Apartamento", "Alto Grande (Loma Linda)", "Apartamento en Urb. Alto Grande, Loma Linda",
    None, "https://apartamento.mercadolibre.com.ve/MLV-730228174-invalmhouse-inmobiliaria-apartamento-en-venta-urbanizacion-alto-grande-sector-loma-linda-carretera-nacional-guarenas-guatire-_JM",
    nota=FALTA)
add("GRN-013", Z, "galpon", "Galpón industrial", "Zona Industrial del Este (Carretera vieja Petare-Guarenas)", "Galpón industrial en la Carretera vieja Petare-Guarenas",
    None, RMX + "local-industrial-y-galpon/venta/galpon-industrial-carretera-vieja-petare-311552",
    specs={"zona": "Zona Industrial del Este"}, cal=(4, 3, 3, 3, 3), nota=FALTA + " También se ofrece en alquiler (GRN-014).")
add("GRN-014", Z, "galpon", "Galpón industrial", "Zona Industrial del Este (Carretera vieja Petare-Guarenas)", "Galpón industrial en alquiler",
    None, RMX + "local-industrial-y-galpon/alquiler/galpon-industrial-carretera-vieja-petare-311555", op="alquiler", nota=FALTA)
add("GRN-015", Z, "galpon", "Galpón", "Loma Linda", "Galpón en alquiler, Sector Loma Linda",
    None, "https://inmueble.mercadolibre.com.ve/MLV-776606532-galpon-en-alquiler-sector-loma-linda-guarenas-mls-24-2888-_JM", op="alquiler", nota=FALTA)

# ─────────────────────────── COSTA MIRANDINA ───────────────────────────
Z = "costa"
add("CST-001", Z, "residencial", "Apartamento", "Higuerote (Jardín Higuerote)", "Apartamento con acceso privado a la playa, Jardín Higuerote",
    None, RMX + "apartamento/venta/apartamento-en-venta-jardin-higuerote-municipio-brion-300288",
    hab=2, banos=2, pto=1, specs={"areas_comunes": "Piscinas tipo club, acceso privado a la playa", "vigilancia": "24/7",
                                  "extras": "Aire acondicionado en habitaciones"},
    cal=(5, 4, 5, 4, 3), nota=FALTA + " Playa privada: el producto con más demanda de alquiler vacacional.")
add("CST-002", Z, "local", "Local comercial", "Higuerote (C.C. Cabo Mall)", "Local en el C.C. Cabo Mall",
    None, RMX + "local-comercial/venta/en-venta-local-comercial-centro-comercial-cabo-mall-higuerote-306925",
    specs={"ubicacion": "Centro comercial"}, nota=FALTA)
add("CST-003", Z, "residencial", "Apartamento", "Higuerote (Puerto Encantado)", "Apartamento PB en Residencias AQUA, Puerto Encantado",
    None, RMX + "apartamento/venta/venta-de-apartamento-en-puerto-encantado-res-aqua-higuerote-283733",
    pto=1, specs={"piso": "Planta baja", "vigilancia": "24h, acceso privado", "estado_obra": "Baños, pisos y cocina actualizados"},
    cal=(4, 4, 4, 3, 3), nota=FALTA)
add("CST-004", Z, "residencial", "Penthouse", "Higuerote (Puerto Encantado)", "Penthouse de 211 m², Puerto Encantado",
    None, RMX + "apartamento/venta/venta-de-pent-house-211-mtrs2-puerto-encantado-higuerote-edo-miranda-285188",
    m2c=211, cal=(4, 3, 4, 2, 3), nota=FALTA)
add("CST-005", Z, "residencial", "Apartamento", "Higuerote (Ciudad Balneario · Villas de Fuente Mar)", "Estudio remodelado de 30 m², Villas de Fuente Mar",
    None, RMX + "apartamento/venta/vendo-apartamento-en-conjunto-residencial-villas-de-fuente-mar-en-urbanizacion-ciudad-balneario-higuerote-270103",
    m2c=30, hab=1, banos=1, pto=1, specs={"areas_comunes": "Piscinas, canchas de tenis, bolas criollas, muelle",
                                          "estado_obra": "Remodelado, cocina con granito"},
    cal=(4, 4, 4, 4, 3), nota=FALTA)
add("CST-006", Z, "residencial", "Apartamento dúplex", "Higuerote (Ciudad Balneario · Villas de Fuente Mar)", "Apartamento de playa de 2 niveles equipado, Villas de Fuente Mar",
    None, RMX + "apartamento/venta/venta-apartamento-de-playa-equipado-ii-niveles-resid-villas-de-fuente-mar-higuerote-285163",
    specs={"niveles": "2", "amoblado": "Equipado"}, nota=FALTA)
add("CST-007", Z, "residencial", "Apartamento", "Higuerote (Las Palmeras)", "Apartamento en Las Palmeras",
    None, RMX + "apartamento/venta/apartamento-en-venta-las-palmeras-higuerote-316518", nota=FALTA)
add("CST-008", Z, "residencial", "Apartamento", "Higuerote (Los Gabanes)", "Apartamento en Conj. Res. Los Gabanes",
    None, RMX + "apartamento/venta/apartamento-en-venta-conjunto-residencial-los-gabanes-municipio-brion-higuerote-305081", nota=FALTA)
add("CST-009", Z, "residencial", "Apartamento", "Higuerote (Agua Sal · Caracolitos)", "Apartamento en Edif. Caracolitos, cerca del Club Aguasal",
    None, RMX + "apartamento/venta/venta-de-apartamento-en-aguasal-edificio-caracolitos-higuerote-321850",
    hab=1, banos=2, pto=1, specs={"vigilancia": "Privada 24h", "estado_obra": "Cocina actualizada"}, cal=(4, 4, 4, 3, 3), nota=FALTA)
add("CST-010", Z, "residencial", "Apartamento", "Río Chico (Los Canales)", "Apartamento en Los Canales de Río Chico",
    None, "https://apartamento.mercadolibre.com.ve/MLV-773110963-apartamento-en-venta-los-canales-de-rio-chico-_JM",
    nota=FALTA + " En Los Canales se publican entre $8.000 y $35.000.")

out = pathlib.Path(__file__).resolve().parent.parent / "data" / "inmuebles.json"
out.write_text(json.dumps(REG, ensure_ascii=False, indent=1))
print(len(REG), "inmuebles ->", out)
