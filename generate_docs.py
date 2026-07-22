# Script pa' generar los PDFs de documentacion de BimBam Buy
# Lo hice usando fpdf2 porque es mas facil que andar instalando cosas raras

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "BimBam Buy - Documentacion Oficial", 0, 1, "C")
        self.line(10, 18, 200, 18)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Pagina {self.page_no()}/{{nb}}", 0, 0, "C")

    def titulo(self, txt):
        self.set_font("Arial", "B", 16)
        self.cell(0, 12, txt, 0, 1, "L")
        self.ln(2)

    def subtitulo(self, txt):
        self.set_font("Arial", "B", 13)
        self.cell(0, 10, txt, 0, 1, "L")
        self.ln(1)

    def parrafo(self, txt):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 6, txt)
        self.ln(2)

    def item_lista(self, txt):
        self.set_font("Arial", "", 11)
        self.cell(5)
        self.multi_cell(0, 6, f"- {txt}")
        self.ln(1)


# ============================================================
# Documento 1: Politica de Reembolsos y Devoluciones
# ============================================================
def gen_reembolsos():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.titulo("Politica de Reembolsos y Devoluciones")
    pdf.parrafo("Fecha de actualizacion: Julio 2026")
    pdf.parrafo("En BimBam Buy queremos que compres con confianza. Si algo no sale como esperabas, revisa nuestra politica de devoluciones.")
    pdf.subtitulo("1. Plazo para devoluciones")
    pdf.parrafo("Tienes hasta 30 dias calendario desde la recepcion del producto para solicitar una devolucion. El producto debe estar en su empaque original y sin uso.")
    pdf.subtitulo("2. Condiciones de la devolucion")
    pdf.item_lista("El producto debe estar sin usar y en las mismas condiciones en que lo recibiste.")
    pdf.item_lista("Debe incluir todos los accesorios, manuales y empaque original.")
    pdf.item_lista("Productos en oferta o liquidacion pueden tener condiciones especiales.")
    pdf.item_lista("Los productos digitales (codigos, software) no tienen devolucion una vez activados.")
    pdf.subtitulo("3. Proceso de devolucion")
    pdf.parrafo("Paso 1: Ingresa a 'Mis Pedidos' en BimBam Buy y selecciona el producto que deseas devolver.")
    pdf.parrafo("Paso 2: Elige el motivo de devolucion y sube fotos si es necesario.")
    pdf.parrafo("Paso 3: Genera la guia de devolucion. El costo de envio de retorno es gratuito para devoluciones por defecto de fabrica.")
    pdf.parrafo("Paso 4: Entrega el paquete en la agencia indicada. Una vez recibido, procesaremos tu reembolso en 5-7 dias habiles.")
    pdf.subtitulo("4. Tiempos de reembolso")
    pdf.item_lista("Tarjeta de credito/debito: 5-10 dias habiles.")
    pdf.item_lista("Transferencia bancaria: 3-5 dias habiles.")
    pdf.item_lista("Billetera digital BimBam: 24-48 horas.")
    pdf.subtitulo("5. Excepciones")
    pdf.parrafo("No aplica devolucion en: alimentos perecederos, productos de higiene personal, software descargable, tarjetas de regalo y productos hechos a medida.")
    pdf.output("docs/Politica_de_Reembolsos_y_Devoluciones_de_BimBam_Buy.pdf")
    print("[OK] Politica de Reembolsos generado")


# ============================================================
# Documento 2: Programa de Afiliados
# ============================================================
def gen_afiliados():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.titulo("Programa de Afiliados de BimBam Buy")
    pdf.parrafo("Version 2.1 - Vigente desde Junio 2026")
    pdf.parrafo("Convierte tu trafico en ingresos. El programa de afiliados de BimBam Buy te permite ganar comisiones recomendando nuestros productos.")
    pdf.subtitulo("1. Como funciona")
    pdf.parrafo("Te registras como afiliado, obtienes tu link unico de referidos, compartes productos en tus redes/website, y ganas comision por cada venta generada.")
    pdf.subtitulo("2. Comisiones")
    pdf.item_lista("Comision base: 10% por cada venta realizada a traves de tu link.")
    pdf.item_lista("Bonos por volumen: si generas mas de 50 ventas al mes, la comision sube al 15%.")
    pdf.item_lista("Super afiliados (100+ ventas/mes): 20% de comision.")
    pdf.item_lista("Las comisiones se pagan los dias 15 de cada mes.")
    pdf.subtitulo("3. Requisitos")
    pdf.item_lista("Ser mayor de 18 anos.")
    pdf.item_lista("Tener una cuenta activa en BimBam Buy.")
    pdf.item_lista("Contar con un sitio web, blog o red social con contenido relevante.")
    pdf.item_lista("No usar publicidad engañosa ni spam.")
    pdf.subtitulo("4. Metodo de pago")
    pdf.parrafo("Las comisiones se pagan via transferencia bancaria (a partir de $50 USD) o en billetera BimBam (sin monto minimo).")
    pdf.subtitulo("5. Periodo de cookies")
    pdf.parrafo("Las cookies de afiliado duran 30 dias. Si un cliente compra dentro de ese periodo, el afiliado recibe la comision.")
    pdf.output("docs/Programa_de_Afiliados_de_BimBam_Buy.pdf")
    print("[OK] Programa de Afiliados generado")


# ============================================================
# Documento 3: Guia de Tiempos y Costos de Envio
# ============================================================
def gen_envios():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.titulo("Guia de Tiempos y Costos de Envio de BimBam Buy")
    pdf.parrafo("Actualizacion: Julio 2026")
    pdf.subtitulo("1. Tipos de envio")
    pdf.item_lista("Envio Estandar: 5-7 dias habiles. Costo: $4.99 o gratis en pedidos mayores a $50.")
    pdf.item_lista("Envio Express: 2-3 dias habiles. Costo: $9.99.")
    pdf.item_lista("Envio Same Day (CDMX y area metropolitana): 24 horas. Costo: $14.99.")
    pdf.subtitulo("2. Cobertura")
    pdf.parrafo("Realizamos envios a toda la Republica Mexicana. Zonas extendidas (rurales) pueden tener un plazo adicional de 1-2 dias.")
    pdf.subtitulo("3. Costos por peso")
    pdf.parrafo("Hasta 1 kg: $4.99 | 1-3 kg: $7.99 | 3-5 kg: $11.99 | 5-10 kg: $15.99 | +10 kg: consultar.")
    pdf.subtitulo("4. Seguimiento")
    pdf.parrafo("Todos los envios incluyen numero de rastreo. Recibiras un correo con el link de seguimiento una vez que el paquete sea despachado.")
    pdf.subtitulo("5. Envios internacionales")
    pdf.parrafo("Por el momento solo realizamos envios dentro de Mexico. Proximamente expandiremos a USA y LATAM.")
    pdf.output("docs/Guia_de_Tiempos_y_Costos_de_Envio_de_BimBam_Buy.pdf")
    print("[OK] Guia de Envios generado")


# ============================================================
# Documento 4: FAQ sobre Metodos de Pago
# ============================================================
def gen_faq_pago():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.titulo("Preguntas Frecuentes sobre Metodos de Pago de BimBam Buy")
    pdf.parrafo("FAQ actualizada - Julio 2026")
    pdf.subtitulo("1. Que metodos de pago aceptan?")
    pdf.parrafo("Aceptamos tarjetas de credito y debito (Visa, Mastercard, American Express), transferencia bancaria SPEI, OXXO, PayPal, y nuestra billetera digital BimBam.")
    pdf.subtitulo("2. Es seguro pagar en BimBam Buy?")
    pdf.parrafo("Si. Usamos cifrado SSL de 256 bits y contamos con certificacion PCI DSS. Tus datos financieros nunca son almacenados en nuestros servidores.")
    pdf.subtitulo("3. Puedo pagar a meses sin intereses?")
    pdf.parrafo("Si. Ofrecemos 3, 6, 9 y 12 meses sin intereses con tarjetas participantes. Consulta la lista completa en nuestro sitio.")
    pdf.subtitulo("4. Como funciona la billetera BimBam?")
    pdf.parrafo("Puedes depositar saldo a tu billetera BimBam y usarlo para compras. Ademas, recibiras 5% de bonus en cada recarga mayor a $200.")
    pdf.subtitulo("5. Que hago si mi pago fue rechazado?")
    pdf.parrafo("Verifica que tus datos sean correctos, que tu tarjeta tenga saldo disponible y que no tengas bloqueos con tu banco. Si el problema persiste, contacta a soporte.")
    pdf.subtitulo("6. El pago con OXXO tiene algun costo extra?")
    pdf.parrafo("No, el pago en OXXO es sin costo adicional. Solo debes realizar el deposito dentro de las 24 horas posteriores a tu pedido.")
    pdf.output("docs/Preguntas_Frecuentes_sobre_Metodos_de_Pago_de_BimBam_Buy.pdf")
    print("[OK] FAQ Metodos de Pago generado")


# ============================================================
# Documento 5: Manual de Garantia de Productos
# ============================================================
def gen_garantia():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.titulo("Manual de Garantia de Productos de BimBam Buy")
    pdf.parrafo("Vigente a partir de Enero 2026")
    pdf.subtitulo("1. Cobertura de garantia")
    pdf.parrafo("Todos los productos electronicos vendidos por BimBam Buy cuentan con 1 ano de garantia directa. Productos de otras categorias tienen 90 dias.")
    pdf.subtitulo("2. Que cubre la garantia?")
    pdf.item_lista("Defectos de fabrica.")
    pdf.item_lista("Fallas de funcionamiento no atribuibles al usuario.")
    pdf.item_lista("Partes y componentes defectuosos.")
    pdf.subtitulo("3. Que NO cubre?")
    pdf.item_lista("Danos por mal uso o accidentes.")
    pdf.item_lista("Desgaste normal del producto.")
    pdf.item_lista("Modificaciones no autorizadas.")
    pdf.item_lista("Productos sin empaque original o con numero de serie alterado.")
    pdf.subtitulo("4. Proceso de garantia")
    pdf.parrafo("Contacta a soporte via nuestro chat o correo. Te pediremos tu numero de pedido y evidencia del defecto. En 48 horas te daremos una solucion (reemplazo, reparacion o reembolso).")
    pdf.subtitulo("5. Garantia extendida")
    pdf.parrafo("Ofrecemos planes de garantia extendida hasta 3 anos para electronicos seleccionados. El costo varia segun el producto.")
    pdf.output("docs/Manual_de_Garantia_de_Productos_de_BimBam_Buy.pdf")
    print("[OK] Manual de Garantia generado")


if __name__ == "__main__":
    gen_reembolsos()
    gen_afiliados()
    gen_envios()
    gen_faq_pago()
    gen_garantia()
    print("\n[Todos los PDFs de BimBam Buy fueron generados correctamente!]")
