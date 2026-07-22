# 🛒 BimBam Buy - Agente Inteligente de Atencion al Cliente

> **Challenge Alura ONE - IA para Tech**
>
> Proyecto desarrollado como parte del challenge de Alura ONE, donde construimos un agente de inteligencia artificial capaz de responder preguntas basadas en documentos PDF usando tecnicas de RAG (Retrieval Augmented Generation).

---

## 📋 Descripcion del Proyecto

**BimBam Buy** es un e-commerce multiplataforma enfocado en la experiencia de compra digital agil y segura. Este proyecto implementa un **Agente RAG** que puede leer 5 documentos PDF oficiales de la empresa y responder preguntas de los clientes sobre:

- ✅ **Politica de Reembolsos y Devoluciones**
- ✅ **Programa de Afiliados**
- ✅ **Guia de Tiempos y Costos de Envio**
- ✅ **Preguntas Frecuentes sobre Metodos de Pago**
- ✅ **Manual de Garantia de Productos**

El agente utiliza un enfoque **RAG (Retrieval Augmented Generation)** simple pero efectivo: convierte los PDFs a texto, los fragmenta, y usa **TF-IDF + similitud coseno** para encontrar la informacion mas relevante para cada pregunta.

---

## 🏗️ Arquitectura de la Solucion

```
┌─────────────────────────────────────────────────────────────┐
│                    USUARIO (Browser)                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  Flask Web App (app.py)                      │
│  • Servidor web HTTP                                        │
│  • Rutas: / (chat), /api/preguntar, /api/documentos         │
│  • Templates HTML + CSS + JS                                │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  RAG Agent (rag_agent.py)                    │
│                                                             │
│  ┌──────────────┐    ┌──────────────────┐                   │
│  │ Carga de PDFs │───▶│ Division en      │                   │
│  │ (pypdf)       │    │ fragmentos/chunks│                   │
│  └──────────────┘    └────────┬─────────┘                   │
│                               ▼                             │
│  ┌──────────────────────────────────────────────┐           │
│  │ Vectorizacion TF-IDF (sklearn)               │           │
│  │ • Convierte texto a vectores numericos       │           │
│  │ • Ignora stop words en espanol               │           │
│  └──────────────────┬───────────────────────────┘           │
│                     ▼                                       │
│  ┌──────────────────────────────────────────────┐           │
│  │ Busqueda por Similitud de Coseno             │           │
│  │ • Vectoriza la pregunta del usuario          │           │
│  │ • Compara contra todos los fragmentos        │           │
│  │ • Devuelve los top_k mas relevantes          │           │
│  └──────────────────────────────────────────────┘           │
│                                                             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              Documentos PDF (carpeta docs/)                  │
│                                                             │
│  1. Politica de Reembolsos y Devoluciones                   │
│  2. Programa de Afiliados                                   │
│  3. Guia de Tiempos y Costos de Envio                       │
│  4. FAQ sobre Metodos de Pago                               │
│  5. Manual de Garantia de Productos                         │
└─────────────────────────────────────────────────────────────┘
```

### Flujo de funcionamiento:

1. El usuario escribe una pregunta en la interfaz web
2. La app Flask recibe la pregunta via API REST
3. El RAG Agent vectoriza la pregunta usando TF-IDF
4. Calcula la similitud coseno contra todos los fragmentos de los PDFs
5. Devuelve los fragmentos mas relevantes como respuesta
6. La interfaz muestra la respuesta y las fuentes utilizadas

---

## 💻 Tecnologias y Herramientas Utilizadas

| Tecnologia | Version | Proposito |
|------------|---------|-----------|
| **Python** | 3.14.5 | Lenguaje principal |
| **Flask** | 3.1.3 | Framework web para el servidor |
| **scikit-learn** | 1.9.0 | TF-IDF y similitud coseno |
| **pypdf** | 6.14.2 | Lectura y extraccion de texto de PDFs |
| **fpdf2** | 2.8.7 | Generacion de documentos PDF |
| **NumPy** | 2.5.1 | Operaciones numericas y matrices |
| **HTML/CSS/JS** | - | Frontend de la aplicacion web |
| **Git/GitHub** | - | Control de versiones y repositorio |

---

## 🚀 Como Ejecutar el Proyecto

### Prerrequisitos

- Python 3.10 o superior instalado
- Git instalado (opcional, para clonar)

### Pasos para ejecutar localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/challenge-alura-agente.git
cd challenge-alura-agente

# 2. (Opcional pero recomendado) Crear un entorno virtual
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
# source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Generar los PDFs de documentacion (si no estan en la carpeta docs/)
python generate_docs.py

# 5. Ejecutar la aplicacion
python app/app.py

# 6. Abrir en el navegador
# http://localhost:5000
```

---

## ❓ Ejemplos de Preguntas que el Agente Puede Responder

| Pregunta | Documento relacionado |
|----------|----------------------|
| "Cual es la politica de reembolso?" | Politica de Reembolsos y Devoluciones |
| "Cuantos dias tengo para devolver un producto?" | Politica de Reembolsos y Devoluciones |
| "Como me hago afiliado y cuanto gano?" | Programa de Afiliados |
| "Cuanto cuesta el envio express?" | Guia de Tiempos y Costos de Envio |
| "El envio es gratis a partir de cuanto?" | Guia de Tiempos y Costos de Envio |
| "Que metodos de pago aceptan?" | FAQ sobre Metodos de Pago |
| "Aceptan PayPal?" | FAQ sobre Metodos de Pago |
| "Mi producto tiene garantia?" | Manual de Garantia de Productos |
| "Que cubre la garantia?" | Manual de Garantia de Productos |

---

## 💬 Ejemplos de Respuestas Generadas por el Agente

### Pregunta: "Cual es la politica de reembolso?"

```
📄 Politica de Reembolsos y Devoluciones de BimBam Buy:

En BimBam Buy queremos que compres con confianza. Tienes hasta 30
dias calendario desde la recepcion del producto para solicitar una
devolucion. El producto debe estar en su empaque original y sin uso.

Pasos:
1. Ingresa a 'Mis Pedidos' en BimBam Buy
2. Selecciona el producto a devolver
3. Genera la guia de devolucion
4. Entrega el paquete en la agencia indicada

Reembolso en 5-7 dias habiles.
```

### Pregunta: "Cuanto cuesta el envio?"

```
📄 Guia de Tiempos y Costos de Envio de BimBam Buy:

- Envio Estandar: 5-7 dias habiles. Costo: $4.99
  (GRATIS en pedidos mayores a $50)
- Envio Express: 2-3 dias habiles. Costo: $9.99
- Envio Same Day (CDMX y area metropolitana): 24 horas. Costo: $14.99
```

### Pregunta: "Como me hago afiliado?"

```
📄 Programa de Afiliados de BimBam Buy:

Te registras como afiliado, obtienes tu link unico de referidos,
compartes productos en tus redes/website, y ganas comision por
cada venta generada.

Comisiones:
- Base: 10% por venta
- 50+ ventas/mes: 15%
- 100+ ventas/mes: 20% (Super Afiliados)
```

---

## 📁 Estructura del Repositorio

```
challenge-alura-agente/
├── app/                          # Codigo fuente de la aplicacion
│   ├── __init__.py              # (vacio, marca como paquete)
│   ├── app.py                   # Servidor Flask
│   ├── rag_agent.py             # Agente RAG (TF-IDF + coseno)
│   ├── templates/
│   │   └── index.html           # Interfaz de usuario (chat)
│   └── static/                  # Archivos estaticos (futuro)
├── docs/                        # Documentos PDF de la empresa
│   ├── Politica_de_Reembolsos_y_Devoluciones_de_BimBam_Buy.pdf
│   ├── Programa_de_Afiliados_de_BimBam_Buy.pdf
│   ├── Guia_de_Tiempos_y_Costos_de_Envio_de_BimBam_Buy.pdf
│   ├── Preguntas_Frecuentes_sobre_Metodos_de_Pago_de_BimBam_Buy.pdf
│   └── Manual_de_Garantia_de_Productos_de_BimBam_Buy.pdf
├── data/                        # (vacio, para futuros datasets)
├── tests/                       # (vacio, para pruebas unitarias)
├── generate_docs.py             # Script para generar los PDFs
├── requirements.txt             # Dependencias del proyecto
├── .gitignore                   # Archivos ignorados por Git
└── README.md                    # Este archivo
```

---

## ☁️ Evidencia de Deploy en OCI

> **Nota:** Esta seccion se completa despues del deploy en Oracle Cloud Infrastructure (OCI).

### Instrucciones para deploy en OCI:

1. Crear una instancia de compute en OCI (Ubuntu 22.04+)
2. Conectarse via SSH y clonar el repositorio
3. Instalar Python y las dependencias
4. Ejecutar la aplicacion con Gunicorn para produccion:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 app.app:app
```

5. Configurar el firewall para permitir trafico en el puerto 8080
6. (Opcional) Usar Nginx como proxy reverso

### Link de la aplicacion desplegada:

```
[PENDIENTE - Agregar URL de OCI]
```

### Captura de pantalla:

```
[PENDIENTE - Agregar screenshot de la app funcionando en OCI]
```

---

## 🧠 Como Funciona el RAG Agent (Explicacion Tecnica)

El agente RAG implementado no utiliza modelos de lenguaje grandes (LLMs) como GPT, sino un enfoque clasico pero efectivo:

1. **Extraccion**: `pypdf` extrae el texto de cada PDF
2. **Fragmentacion**: Divide el texto en chunks de ~500 palabras
3. **Vectorizacion**: `TfidfVectorizer` de scikit-learn convierte cada chunk en un vector numerico, ignorando stop words en espanol
4. **Busqueda**: Cuando el usuario hace una pregunta, se vectoriza con el mismo vectorizador y se calcula la similitud coseno contra todos los chunks
5. **Respuesta**: Se devuelven los chunks mas similares (top 3) con un umbral minimo de 5% de similitud

**Ventajas de este enfoque:**
- No requiere GPU ni descargar modelos grandes
- Rapido (respuestas en milisegundos)
- Funciona offline
- Facil de entender y modificar

---

## 🔮 Mejoras Futuras

- [ ] Integrar un LLM local (como Llama 3 o Mistral) para generar respuestas mas naturales
- [ ] Soporte para mas formatos de archivo (CSV, DOCX, TXT)
- [ ] Historial de conversaciones
- [ ] Autenticacion de usuarios
- [ ] Modo oscuro en la interfaz
- [ ] Despliegue automatizado con Docker
- [ ] Mas documentos de BimBam Buy (terminos y condiciones, politicas de privacidad)

---

## 📝 Licencia

Proyecto educativo desarrollado para el **Challenge Alura ONE - IA para Tech**.

---

## 🙌 Agradecimientos

- A **Alura** y **ONE (Oracle Next Education)** por el programa de formacion
- A los instructores por el contenido del curso
- A la comunidad por los recursos compartidos

---

> Desarrollado con ❤️ para el challenge de Alura ONE
