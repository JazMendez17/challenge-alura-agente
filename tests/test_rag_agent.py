# Pruebas unitarias bien basicas pa' ver que el agente funcione
# Se usa el modulo unittest, no pytest

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

import unittest
from rag_agent import RAGAgent


class TestRAGAgent(unittest.TestCase):
    """Pruebas del agente RAG"""

    @classmethod
    def setUpClass(cls):
        """Cargamos el agente una sola vez para todas las pruebas"""
        print("Cargando agente RAG para pruebas...")
        cls.agente = RAGAgent()
        print(f"Documentos cargados: {len(cls.agente.documents)}")

    def test_carga_documentos(self):
        """Verifica que los PDFs se cargaron correctamente"""
        self.assertGreater(len(self.agente.documents), 0, "No se cargaron documentos")
        self.assertGreater(len(self.agente.chunks), 0, "No se crearon fragmentos")

    def test_documentos_esperados(self):
        """Verifica que esten los 5 documentos de BimBam Buy"""
        docs = self.agente.listar_documentos()
        self.assertEqual(len(docs), 5, "Deberian ser 5 documentos")

        esperados = [
            "Politica_de_Reembolsos",
            "Programa_de_Afiliados",
            "Guia_de_Tiempos",
            "Preguntas_Frecuentes",
            "Manual_de_Garantia"
        ]
        for esperado in esperados:
            existe = any(esperado in d for d in docs)
            self.assertTrue(existe, f"Falta documento: {esperado}")

    def test_buscar_reembolso(self):
        """Prueba busqueda sobre reembolsos"""
        resultados = self.agente.buscar("politica de reembolso", top_k=3)
        self.assertGreater(len(resultados), 0, "Deberia encontrar resultados")
        self.assertIn("Reembolsos", resultados[0]["documento"])

    def test_buscar_afiliados(self):
        """Prueba busqueda sobre afiliados"""
        resultados = self.agente.buscar("programa de afiliados comisiones", top_k=3)
        self.assertGreater(len(resultados), 0, "Deberia encontrar resultados")
        self.assertIn("Afiliados", resultados[0]["documento"])

    def test_buscar_envio(self):
        """Prueba busqueda sobre envios"""
        resultados = self.agente.buscar("costo de envio express", top_k=3)
        self.assertGreater(len(resultados), 0, "Deberia encontrar resultados")
        self.assertIn("Envio", resultados[0]["documento"])

    def test_buscar_pago(self):
        """Prueba busqueda sobre metodos de pago"""
        resultados = self.agente.buscar("metodos de pago aceptados", top_k=3)
        self.assertGreater(len(resultados), 0, "Deberia encontrar resultados")
        self.assertIn("Pago", resultados[0]["documento"])

    def test_buscar_garantia(self):
        """Prueba busqueda sobre garantia"""
        resultados = self.agente.buscar("garantia de productos", top_k=3)
        self.assertGreater(len(resultados), 0, "Deberia encontrar resultados")
        self.assertIn("Garantia", resultados[0]["documento"])

    def test_similitud_minima(self):
        """Verifica que los resultados tengan similitud aceptable"""
        resultados = self.agente.buscar("reembolso", top_k=1)
        if resultados:
            self.assertGreater(resultados[0]["similitud"], 0.05,
                             "La similitud deberia ser mayor a 0.05")

    def test_sin_resultados(self):
        """Prueba con una pregunta que no deberia tener match"""
        resultados = self.agente.buscar("receta de pastel de chocolate", top_k=3)
        self.assertEqual(len(resultados), 0, "No deberia encontrar nada")

    def test_responder_devuelve_formato(self):
        """Verifica que responder() devuelva el formato correcto"""
        respuesta = self.agente.responder("devoluciones")
        self.assertIn("respuesta", respuesta)
        self.assertIn("fuentes", respuesta)


if __name__ == "__main__":
    unittest.main(verbosity=2)
