#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aplicación principal para el cuestionario técnico.

Este módulo proporciona la interfaz principal para interactuar con el cuestionario
técnico del proceso de selección para Consultor Líder Analítica.
"""

import os
import sys
from typing import Dict, List, Optional, Tuple
import json
from pathlib import Path

# Constantes
CATEGORIAS = {
    "1": "Análisis de Datos",
    "2": "Creación de Modelos Predictivos",
    "3": "Estrategia y Liderazgo en Analítica",
    "4": "Visualización de Datos",
    "5": "Caso Práctico"
}

def mostrar_bienvenida() -> None:
    """Muestra un mensaje de bienvenida al usuario."""
    print("\n" + "=" * 60)
    print("CUESTIONARIO TÉCNICO - CONSULTOR LÍDER ANALÍTICA".center(60))
    print("=" * 60)
    print("\nBienvenido al sistema de evaluación técnica.\n")

def mostrar_menu_categorias() -> str:
    """Muestra el menú de categorías y devuelve la opción seleccionada."""
    print("\n" + "-" * 60)
    print("CATEGORÍAS DEL CUESTIONARIO".center(60))
    print("-" * 60)
    
    for key, value in CATEGORIAS.items():
        print(f"{key}. {value}")
    print("0. Salir")
    
    while True:
        opcion = input("\nSeleccione una categoría (0-5): ").strip()
        if opcion in ["0", "1", "2", "3", "4", "5"]:
            return opcion
        print("Opción no válida. Por favor, intente de nuevo.")

def mostrar_subcategorias(categoria: str) -> str:
    """Muestra las subcategorías de una categoría y devuelve la opción seleccionada."""
    subcategorias = {
        "1": [
            "1.1 Limpieza y preparación de datos",
            "1.2 Análisis descriptivo de datos"
        ],
        "2": [
            "2.1 Regresión lineal",
            "2.2 Clasificación con árbol de decisión"
        ],
        "3": [
            "3.1 Definición de una estrategia de analítica",
            "3.2 Gestión de Stakeholders en un proyecto de analítica"
        ],
        "4": [
            "4.1 Creación de un dashboard"
        ],
        "5": [
            "5.1 Caso práctico (por desarrollar)"
        ]
    }
    
    print(f"\n{'-' * 60}")
    print(f"{CATEGORIAS[categoria].upper()}".center(60))
    print("-" * 60)
    
    for sub in subcategorias[categoria]:
        print(sub)
    print("0. Volver al menú anterior")
    
    while True:
        opcion = input("\nSeleccione una opción (ej: 1.1) o 0 para volver: ").strip()
        if opcion == "0" or any(opcion == sub.split()[0] for sub in subcategorias[categoria]):
            return opcion
        print("Opción no válida. Por favor, intente de nuevo.")

def cargar_preguntas() -> Dict[str, Dict]:
    """
    Carga las preguntas organizadas por categorías.
    
    Returns:
        Diccionario con las preguntas organizadas por categorías.
    """
    return {
        # Análisis de Datos
        "1.1": {
            "enunciado": "Limpieza y preparación de datos",
            "descripcion": "Tienes un conjunto de datos con las siguientes columnas:\n"
                        "- ID_cliente\n"
                        "- Nombre\n"
                        "- Fecha_de_compra\n"
                        "- Monto_compra\n"
                        "- Producto\n\n"
                        "Al analizar el dataset, detectas valores nulos, duplicados y algunos registros donde el formato de las fechas no es consistente.",
            "instrucciones": [
                "Describe el proceso que seguirías para limpiar estos datos utilizando Python o R.",
                "Implementa una función en el lenguaje de tu preferencia que realice las siguientes acciones:",
                "  - Eliminar duplicados",
                "  - Corregir el formato de la columna de fecha",
                "  - Eliminar los registros con valores nulos en Monto_compra"
            ]
        },
        "1.2": {
            "enunciado": "Análisis descriptivo de datos",
            "descripcion": "Tienes los siguientes datos de ventas:\n"
                        "Ventas_por_mes: [200, 150, 180, 220, 210, 190, 230, 220, 240, 230, 210, 250]",
            "instrucciones": [
                "Calcula el promedio, la mediana y la desviación estándar de las ventas.",
                "Realiza una visualización en la que compares las ventas mensuales con el promedio general."
            ]
        },
        
        # Creación de Modelos Predictivos
        "2.1": {
            "enunciado": "Regresión lineal",
            "descripcion": "Tienes un dataset con las siguientes columnas:\n"
                        "- Horas_estudio\n"
                        "- Notas_examen\n\n"
                        "El objetivo es predecir las notas del examen en función de las horas de estudio.",
            "instrucciones": [
                "Entrena un modelo de regresión lineal para predecir las Notas_examen en función de las Horas_estudio.",
                "Muestra el coeficiente de determinación R² del modelo.",
                "Realiza una predicción para un estudiante que ha estudiado 5 horas.",
                "Explica cómo interpretas los resultados del modelo."
            ]
        },
        "2.2": {
            "enunciado": "Clasificación con árbol de decisión",
            "descripcion": "Dispones de un dataset de clientes con las siguientes columnas:\n"
                        "- Edad\n"
                        "- Ingresos\n"
                        "- Compra_realizada (0: No, 1: Sí)\n\n"
                        "El objetivo es predecir si un cliente realizará una compra basado en su edad e ingresos.",
            "instrucciones": [
                "Prepara los datos para el modelo de clasificación.",
                "Entrena un árbol de decisión para predecir si un cliente realizará una compra.",
                "Muestra la importancia de las características (edad e ingresos).",
                "Evalúa el rendimiento del modelo usando métricas apropiadas (exactitud, precisión, recall, F1-score).",
                "Realiza una predicción para un nuevo cliente con 35 años y $50,000 de ingresos."
            ]
        },
        
        # Estrategia y Liderazgo en Analítica
        "3.1": {
            "enunciado": "Definición de una estrategia de analítica",
            "descripcion": "Imagina que trabajas en una empresa que está comenzando su transformación digital y te han pedido definir una estrategia de analítica de datos.",
            "instrucciones": [
                "Describe los pasos clave que seguirías para implementar una estrategia de analítica en una organización que nunca ha trabajado con grandes volúmenes de datos.",
                "¿Qué factores considerarías para priorizar los proyectos de analítica?",
                "¿Cómo medirías el éxito de la implementación de la estrategia?",
                "Menciona al menos tres desafíos comunes en la implementación de una estrategia de analítica y cómo los abordarías."
            ]
        },
        "3.2": {
            "enunciado": "Gestión de Stakeholders en un proyecto de analítica",
            "descripcion": "En un proyecto de analítica, es fundamental gestionar adecuadamente las expectativas y la comunicación con las partes interesadas (stakeholders).",
            "instrucciones": [
                "Explica cómo gestionarías la relación con los stakeholders no técnicos en un proyecto de analítica.",
                "¿Qué estrategias utilizarías para asegurar que los resultados sean comprendidos y aplicados correctamente?",
                "Describe cómo manejarías una situación donde los stakeholders tienen expectativas poco realistas sobre los resultados del análisis.",
                "¿Qué herramientas o técnicas utilizarías para presentar los hallazgos a un público no técnico?"
            ]
        },
        
        # Visualización de Datos
        "4.1": {
            "enunciado": "Creación de un dashboard",
            "descripcion": "Te han pedido crear un dashboard para visualizar los siguientes indicadores de un negocio de retail:\n"
                        "- Ventas totales por región\n"
                        "- Margen de ganancia por producto\n"
                        "- Comparación de ventas mensuales del último año",
            "instrucciones": [
                "Describe cómo estructurarías el dashboard para asegurar que sea claro y útil para los stakeholders.",
                "¿Qué tipo de gráficos utilizarías para cada indicador y por qué?",
                "¿Qué características de usabilidad incluirías para facilitar la interacción con el dashboard?",
                "¿Cómo asegurarías que el dashboard sea accesible para usuarios con diferentes niveles de conocimiento técnico?",
                "Propón un esquema de colores y diseño general para el dashboard."
            ]
        },
        
        # Caso Práctico
        "5.1": {
            "enunciado": "Caso Práctico - Análisis de Datos de Ventas",
            "descripcion": "Una cadena de tiendas minoristas te ha proporcionado un conjunto de datos con información sobre ventas de los últimos 3 años. Los datos incluyen información sobre productos, tiendas, fechas de venta, cantidades y montos.",
            "instrucciones": [
                "Realiza un análisis exploratorio de los datos (EDA) para identificar patrones y tendencias.",
                "Identifica los productos más y menos vendidos, y analiza su comportamiento a lo largo del tiempo.",
                "Propón al menos tres recomendaciones de negocio basadas en los hallazgos del análisis.",
                "Diseña un plan de acción para implementar una de las recomendaciones propuestas.",
                "¿Qué métricas clave (KPIs) sugerirías monitorear para evaluar el éxito de la implementación?"
            ]
        }
    }

def mostrar_pregunta(codigo_pregunta: str) -> None:
    """Muestra una pregunta específica según su código."""
    preguntas = cargar_preguntas()
    
    if codigo_pregunta not in preguntas:
        print("Pregunta no encontrada.")
        return
    
    pregunta = preguntas[codigo_pregunta]
    
    print("\n" + "=" * 80)
    print(f"{pregunta['enunciado']}".center(80))
    print("=" * 80)
    
    print("\n" + "DESCRIPCIÓN".center(80, "-"))
    print(pregunta['descripcion'])
    
    print("\n" + "INSTRUCCIONES".center(80, "-"))
    for i, instruccion in enumerate(pregunta['instrucciones'], 1):
        print(f"{i}. {instruccion}")
    
    print("\n" + "=" * 80 + "\n")

def main():
    """Función principal de la aplicación."""
    mostrar_bienvenida()
    
    while True:
        # Mostrar menú de categorías
        opcion_categoria = mostrar_menu_categorias()
        
        if opcion_categoria == "0":
            print("\n¡Gracias por usar el sistema de evaluación!")
            break
            
        # Mostrar subcategorías
        opcion_subcategoria = mostrar_subcategorias(opcion_categoria)
        
        if opcion_subcategoria == "0":
            continue
            
        # Mostrar la pregunta seleccionada
        mostrar_pregunta(opcion_subcategoria)
        
        # Esperar a que el usuario presione Enter para continuar
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n¡Operación cancelada por el usuario!")
        sys.exit(0)
