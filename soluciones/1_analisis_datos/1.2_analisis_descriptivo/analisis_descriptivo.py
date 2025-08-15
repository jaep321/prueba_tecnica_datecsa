#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1.2 Análisis Descriptivo de Datos

Este script realiza un análisis descriptivo de los datos limpios generados en el ejercicio 1.1.
Incluye:
1. Estadísticas descriptivas básicas
2. Análisis de distribuciones
3. Visualizaciones de los datos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

# Configuración inicial
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
plt.style.use('seaborn-v0_8')  # Usar el estilo más reciente de seaborn
sns.set_palette('pastel')


def cargar_datos(ruta_archivo: str) -> pd.DataFrame:
    """Carga el dataset desde un archivo CSV.
    
    Args:
        ruta_archivo: Ruta al archivo CSV con los datos
        
    Returns:
        DataFrame de pandas con los datos cargados
    """
    try:
        return pd.read_csv(ruta_archivo, parse_dates=['Fecha_de_compra'])
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return pd.DataFrame()


def generar_estadisticas_descriptivas(df: pd.DataFrame) -> None:
    """Genera y muestra estadísticas descriptivas del DataFrame.
    
    Args:
        df: DataFrame con los datos a analizar
    """
    print("\n" + "="*50)
    print("ESTADÍSTICAS DESCRIPTIVAS")
    print("="*50)
    
    # Estadísticas generales
    print("\nResumen estadístico de variables numéricas:")
    print(df.describe())
    
    # Conteo de valores por categoría
    if 'Producto' in df.columns:
        print("\nConteo de compras por producto:")
        print(df['Producto'].value_counts())
    
    # Estadísticas por producto
    if 'Producto' in df.columns and 'Monto_compra' in df.columns:
        print("\nEstadísticas de Monto_compra por Producto:")
        print(df.groupby('Producto')['Monto_compra'].describe())


def generar_visualizaciones(df: pd.DataFrame, ruta_guardado: str) -> None:
    """Genera visualizaciones de los datos.
    
    Args:
        df: DataFrame con los datos a visualizar
        ruta_guardado: Ruta donde se guardarán las imágenes
    """
    print("\nGenerando visualizaciones...")
    
    # Crear directorio de salida si no existe
    Path(ruta_guardado).mkdir(parents=True, exist_ok=True)
    
    # 1. Histograma de montos de compra
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Monto_compra', kde=True, bins=8)
    plt.title('Distribución de Montos de Compra')
    plt.xlabel('Monto de Compra')
    plt.ylabel('Frecuencia')
    plt.savefig(f"{ruta_guardado}/histograma_montos.png")
    plt.close()
    
    # 2. Boxplot de montos por producto
    if 'Producto' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x='Producto', y='Monto_compra')
        plt.title('Distribución de Montos por Producto')
        plt.xlabel('Producto')
        plt.ylabel('Monto de Compra')
        plt.savefig(f"{ruta_guardado}/boxplot_productos.png")
        plt.close()
    
    # 3. Serie de tiempo de compras
    if 'Fecha_de_compra' in df.columns:
        df_fecha = df.set_index('Fecha_de_compra').sort_index()
        plt.figure(figsize=(12, 6))
        df_fecha['Monto_compra'].plot()
        plt.title('Evolución de Montos de Compra en el Tiempo')
        plt.xlabel('Fecha de Compra')
        plt.ylabel('Monto de Compra')
        plt.tight_layout()
        plt.savefig(f"{ruta_guardado}/serie_temporal.png")
        plt.close()
    
    print(f"Visualizaciones guardadas en: {ruta_guardado}")


def analizar_correlaciones(df: pd.DataFrame) -> None:
    """Analiza correlaciones entre variables numéricas.
    
    Args:
        df: DataFrame con los datos a analizar
    """
    print("\n" + "="*50)
    print("ANÁLISIS DE CORRELACIONES")
    print("="*50)
    
    # Convertir variables categóricas a numéricas para correlación
    df_corr = df.copy()
    if 'Producto' in df_corr.columns:
        df_corr['Producto'] = pd.factorize(df_corr['Producto'])[0]
    
    # Calcular y mostrar matriz de correlación
    corr = df_corr.corr(numeric_only=True)
    print("\nMatriz de correlación:")
    print(corr)
    
    # Generar heatmap de correlación
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Mapa de Calor de Correlaciones')
    plt.tight_layout()
    plt.savefig("graficos/correlaciones.png")
    plt.close()


def main():
    """Función principal."""
    # Rutas de archivos
    ruta_datos = "../1.1_limpieza_datos/datos/datos_limpios.csv"
    ruta_graficos = "graficos"
    
    # Cargar datos
    print("Cargando datos limpios...")
    df = cargar_datos(ruta_datos)
    
    if df.empty:
        print("No se pudieron cargar los datos. Verifica la ruta del archivo.")
        return
    
    print(f"\nPrimeras filas del dataset:")
    print(df.head())
    
    # Generar análisis descriptivo
    generar_estadisticas_descriptivas(df)
    
    # Generar visualizaciones
    generar_visualizaciones(df, ruta_graficos)
    
    # Analizar correlaciones
    analizar_correlaciones(df)
    
    print("\n¡Análisis descriptivo completado con éxito!")


if __name__ == "__main__":
    main()
