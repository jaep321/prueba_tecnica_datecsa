#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solución para el ejercicio 1.1: Limpieza y preparación de datos

Este script realiza las siguientes operaciones de limpieza en un dataset:
1. Elimina duplicados
2. Corrige el formato de fechas
3. Maneja valores nulos en la columna Monto_compra
"""

import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
import warnings

# Configuración inicial
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)


def cargar_datos(ruta_archivo: str) -> pd.DataFrame:
    """Carga el dataset desde un archivo CSV.
    
    Args:
        ruta_archivo: Ruta al archivo CSV con los datos
        
    Returns:
        DataFrame de pandas con los datos cargados
    """
    try:
        return pd.read_csv(ruta_archivo, encoding='utf-8')
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return pd.DataFrame()


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """Realiza la limpieza del DataFrame.
    
    Args:
        df: DataFrame con los datos a limpiar
        
    Returns:
        DataFrame con los datos limpios
    """
    # Hacer una copia para no modificar el original
    df_limpio = df.copy()
    
    # 1. Eliminar duplicados
    duplicados = df_limpio.duplicated().sum()
    if duplicados > 0:
        print(f"Se encontraron {duplicados} registros duplicados. Eliminando...")
        df_limpio = df_limpio.drop_duplicates()
    
    # 2. Corregir formato de fechas por fila
    if 'Fecha_de_compra' in df_limpio.columns:
        print("\nConvirtiendo formato de fechas...")
        
        formatos_fecha = [
            '%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', 
            '%Y/%m/%d', '%d-%m-%Y', '%m-%d-%Y'
        ]
        
        def convertir_fecha(valor):
            if pd.isna(valor):
                return pd.NaT
            for fmt in formatos_fecha:
                try:
                    return datetime.strptime(str(valor), fmt)
                except:
                    continue
            return pd.NaT  # Si ninguno funciona
        
        df_limpio['Fecha_de_compra'] = df_limpio['Fecha_de_compra'].apply(convertir_fecha)
    
    # 3. Manejar valores nulos en Monto_compra
    if 'Monto_compra' in df_limpio.columns:
        nulos = df_limpio['Monto_compra'].isna().sum()
        if nulos > 0:
            print(f"\nSe encontraron {nulos} valores nulos en 'Monto_compra'. Eliminando registros...")
            df_limpio = df_limpio.dropna(subset=['Monto_compra'])
    
    return df_limpio


def validar_datos(df: pd.DataFrame) -> None:
    """Realiza validaciones sobre los datos limpios.
    
    Args:
        df: DataFrame con los datos a validar
    """
    print("\n" + "="*50)
    print("VALIDACIÓN DE DATOS")
    print("="*50)
    
    # Verificar duplicados
    duplicados = df.duplicated().sum()
    print(f"\nRegistros duplicados: {duplicados}")
    
    # Verificar nulos por columna
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    
    # Verificar tipos de datos
    print("\nTipos de datos:")
    print(df.dtypes)
    
    # Estadísticas descriptivas
    if 'Monto_compra' in df.columns:
        print("\nEstadísticas de Monto_compra:")
        print(df['Monto_compra'].describe())


def generar_datos_ejemplo() -> pd.DataFrame:
    """Genera un dataset de ejemplo para pruebas."""
    np.random.seed(42)
    
    # Crear datos de ejemplo
    data = {
        'ID_cliente': list(range(1, 11)) * 2,  # Convertir a lista antes de multiplicar
        'Nombre': [f'Cliente {i}' for i in range(1, 11)] * 2,
        'Fecha_de_compra': [
            '2023-01-15', '2023/02/20', '15-03-2023', '04/30/2023', '2023-05-10',
            '2023-06-25', '07/15/2023', '2023-08-20', '2023-09-05', '2023-10-12',
            '2023-01-15', '2023/02/20', '15-03-2023', '04/30/2023', '2023-05-10',
            '2023-06-25', '07/15/2023', '2023-08-20', '2023-09-05', '2023-10-12'
        ],
        'Monto_compra': np.random.normal(100, 30, 20).round(2).tolist(),
        'Producto': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'] * 2
    }
    
    # Convertir a DataFrame
    df = pd.DataFrame(data)
    
    # Agregar algunos valores nulos
    for _ in range(3):
        idx = np.random.randint(0, len(df))
        df.loc[idx, 'Monto_compra'] = np.nan
    
    return df


def main():
    """Función principal."""
    # Crear directorio de datos si no existe
    directorio_datos = Path('datos')
    directorio_datos.mkdir(exist_ok=True)
    
    # Ruta del archivo de datos
    ruta_datos = directorio_datos / 'datos_ventas.csv'
    
    # Generar y guardar datos de ejemplo si no existen
    if not ruta_datos.exists():
        print("Generando datos de ejemplo...")
        df = generar_datos_ejemplo()
        df.to_csv(ruta_datos, index=False, encoding='utf-8')
    else:
        print("Cargando datos existentes...")
        df = cargar_datos(ruta_datos)
    
    print("\nDatos originales:")
    print(df.head())
    
    # Limpiar datos
    print("\n" + "="*50)
    print("PROCESANDO DATOS")
    print("="*50)
    df_limpio = limpiar_datos(df)
    
    # Mostrar datos limpios
    print("\nDatos después de la limpieza:")
    print(df_limpio.head())
    
    # Validar datos
    validar_datos(df_limpio)
    
    # Guardar datos limpios
    ruta_salida = directorio_datos / 'datos_limpios.csv'
    df_limpio.to_csv(ruta_salida, index=False, encoding='utf-8')
    print(f"\nDatos limpios guardados en: {ruta_salida}")


if __name__ == "__main__":
    main()
