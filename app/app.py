# App web Flask para el Challenge Alura - Agente RAG de BimBam Buy
# Esta es mi primera vez haciendo un proyecto asi, perdon si algo esta mal XD

from flask import Flask, render_template, request, jsonify
from rag_agent import RAGAgent
import sys
import os

# Para que encuentre los PDFs desde donde sea que se ejecute
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

# Inicializamos el agente RAG cuando arranca la app
print("=== Iniciando BimBam Buy RAG Agent ===")
try:
    agente = RAGAgent()
    print(f"Documentos cargados: {agente.listar_documentos()}")
except Exception as e:
    print(f"ERROR al cargar el agente: {e}")
    agente = None


@app.route("/")
def index():
    """Pagina principal con el chat"""
    docs = agente.listar_documentos() if agente else []
    return render_template("index.html", documentos=docs)


@app.route("/api/preguntar", methods=["POST"])
def preguntar():
    """
    API endpoint para hacer preguntas al agente.
    Recibe JSON con {"pregunta": "texto de la pregunta"}
    """
    if not agente:
        return jsonify({
            "respuesta": "El agente no esta disponible. Revisa la consola.",
            "fuentes": []
        })

    data = request.get_json()
    pregunta = data.get("pregunta", "").strip()

    if not pregunta:
        return jsonify({
            "respuesta": "Por favor escribe una pregunta.",
            "fuentes": []
        })

    respuesta = agente.responder(pregunta)
    return jsonify(respuesta)


@app.route("/api/documentos", methods=["GET"])
def listar_docs():
    """Endpoint para ver los documentos cargados"""
    if not agente:
        return jsonify({"documentos": []})
    return jsonify({"documentos": agente.listar_documentos()})


@app.route("/api/sugerencias", methods=["GET"])
def sugerencias():
    """Endpoint que regresa preguntas de ejemplo"""
    ejemplos = [
        "Cual es la politica de reembolso?",
        "Como puedo ser afiliado y ganar comisiones?",
        "Cuanto cuesta el envio express?",
        "Que metodos de pago aceptan?",
        "Mi producto tiene garantia?",
        "Cuantos dias tengo para devolver un producto?",
        "Como funciona la billetera BimBam?",
        "Se puede pagar a meses sin intereses?"
    ]
    return jsonify({"sugerencias": ejemplos})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
