# Mi agente RAG casero para el challenge de Alura
# Usa TF-IDF + coseno similitud en vez de cosas pesadas como transformers
# Asi no ocupa GPU ni tarda en descargar modelos gigantes

import os
import glob
from pathlib import Path
import numpy as np
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


class RAGAgent:
    """
    Agente RAG simple que lee PDFs de una carpeta y responde preguntas
    basado en el contenido de los documentos.
    """

    def __init__(self, docs_folder=None):
        if docs_folder is None:
            # Buscamos la carpeta docs relativa a donde se ejecute
            actual = Path(__file__).parent.absolute()
            docs_folder = actual.parent / "docs"
        self.docs_folder = Path(docs_folder)
        self.documents = []       # lista de diccionarios con info de cada doc
        self.chunks = []          # fragmentos de texto
        self.chunk_sources = []   # de que documento viene cada fragmento
        self.vectorizer = TfidfVectorizer(
            max_features=5000,
            stop_words=['el', 'la', 'los', 'las', 'de', 'del', 'en', 'un', 'una',
                        'y', 'e', 'o', 'a', 'con', 'por', 'para', 'es', 'se', 'que',
                        'al', 'lo', 'su', 'le', 'ya', 'no', 'ni', 'mas', 'pero',
                        'este', 'esta', 'entre', 'todo', 'tambien', 'como', 'muy',
                        'cada', 'puede', 'tiene', 'ser', 'era', 'son', 'han',
                        'mas', 'sin', 'sobre', 'todo', 'desde', 'hasta', 'esta']
        )
        self.tfidf_matrix = None
        self.cargar_documentos()

    def cargar_documentos(self):
        """Busca y carga todos los PDFs en la carpeta docs"""
        pdf_files = list(self.docs_folder.glob("*.pdf"))
        if not pdf_files:
            print(f"  [!] No se encontraron PDFs en {self.docs_folder}")
            return

        print(f"  [*] Cargando {len(pdf_files)} documentos PDF...")
        for pdf_path in pdf_files:
            try:
                texto = self._leer_pdf(pdf_path)
                self.documents.append({
                    "nombre": pdf_path.name,
                    "ruta": str(pdf_path),
                    "texto": texto
                })
                # Dividir en fragmentos de ~500 palabras cada uno
                fragmentos = self._dividir_en_chunks(texto, chunk_size=500)
                for f in fragmentos:
                    self.chunks.append(f)
                    self.chunk_sources.append(pdf_path.name)
                print(f"    -> {pdf_path.name}: {len(texto)} caracteres, {len(fragmentos)} fragmentos")
            except Exception as e:
                print(f"    [!] Error al leer {pdf_path.name}: {e}")

        # Construir la matriz TF-IDF con todos los fragmentos
        if self.chunks:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.chunks)
            print(f"\n  [OK] Matriz TF-IDF creada con {len(self.chunks)} fragmentos y "
                  f"{self.tfidf_matrix.shape[1]} terminos")

    def _leer_pdf(self, ruta):
        """Extrae texto de un PDF usando pypdf"""
        reader = PdfReader(str(ruta))
        texto = ""
        for pagina in reader.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto += texto_pagina + "\n"
        return texto

    def _dividir_en_chunks(self, texto, chunk_size=500):
        """Divide el texto en fragmentos de tamano aproximado"""
        palabras = texto.split()
        chunks = []
        for i in range(0, len(palabras), chunk_size):
            chunk = " ".join(palabras[i:i + chunk_size])
            if chunk.strip():
                chunks.append(chunk)
        return chunks if chunks else [texto]

    def buscar(self, pregunta, top_k=3):
        """
        Busca los fragmentos mas relevantes para la pregunta.
        Usa TF-IDF + similitud coseno.
        """
        if not self.chunks or self.tfidf_matrix is None:
            return []

        # Vectorizar la pregunta
        pregunta_vec = self.vectorizer.transform([pregunta])

        # Calcular similitud coseno contra todos los fragmentos
        similitudes = cosine_similarity(pregunta_vec, self.tfidf_matrix)[0]

        # Obtener los indices de los mas similares
        indices_top = np.argsort(similitudes)[::-1][:top_k]

        resultados = []
        for idx in indices_top:
            if similitudes[idx] > 0.05:  # solo si tiene al menos 5% de similitud
                resultados.append({
                    "contenido": self.chunks[idx][:500] + "...",  # truncamos pa' mostrar
                    "documento": self.chunk_sources[idx],
                    "similitud": round(float(similitudes[idx]), 4)
                })
        return resultados

    def responder(self, pregunta):
        """
        Genera una respuesta basada en los fragmentos encontrados.
        Como no uso LLM, hago un resumen simple de lo que encontre.
        """
        resultados = self.buscar(pregunta, top_k=3)
        if not resultados:
            return {
                "respuesta": "Lo siento, no encontre informacion sobre eso en mis documentos. Pregunta sobre: reembolsos, devoluciones, afiliados, envios, metodos de pago, garantias, etc.",
                "fuentes": []
            }

        # Armamos la respuesta con los fragmentos relevantes
        fuentes_vistas = set()
        respuesta = ""
        for r in resultados:
            if r["documento"] not in fuentes_vistas:
                fuente_legible = r["documento"].replace("_", " ").replace(".pdf", "")
                respuesta += f"\n📄 {fuente_legible}:\n{r['contenido']}\n"
                fuentes_vistas.add(r["documento"])

        return {
            "respuesta": respuesta.strip(),
            "fuentes": list(fuentes_vistas)
        }

    def listar_documentos(self):
        """Regresa la lista de documentos cargados"""
        return [d["nombre"] for d in self.documents]

    def resumen_documento(self, nombre):
        """Da un resumen corto de un documento especifico"""
        for d in self.documents:
            if d["nombre"] == nombre:
                return d["texto"][:1000] + "..."
        return None


# Si ejecutan esto directo, pruebas rapidas
if __name__ == "__main__":
    print("=== Prueba del Agente RAG ===\n")
    agente = RAGAgent()
    print(f"\nDocumentos cargados: {agente.listar_documentos()}\n")

    preguntas_prueba = [
        "Cual es la politica de reembolso?",
        "Como me hago afiliado y gano comisiones?",
        "Cuanto cuesta el envio?",
        "Que metodos de pago aceptan?",
        "Mi producto tiene garantia?"
    ]

    for p in preguntas_prueba:
        print(f"\n--- Pregunta: {p} ---")
        resp = agente.responder(p)
        print(resp["respuesta"][:400])
        print(f"Fuentes: {resp['fuentes']}")
