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
plt.style.use('seaborn-v0_8')
sns.set_palette('pastel')


def analizar_ventas_mensuales():
    """Analiza las ventas mensuales según el ejercicio propuesto."""
    print("\n" + "="*50)
    print("ANÁLISIS DE VENTAS MENSUALES")
    print("="*50)
    
    # Datos de ventas mensuales
    ventas_mensuales = [200, 150, 180, 220, 210, 190, 230, 220, 240, 230, 210, 250]
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
             'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    
    # Cálculos estadísticos
    promedio = np.mean(ventas_mensuales)
    mediana = np.median(ventas_mensuales)
    desviacion = np.std(ventas_mensuales, ddof=1)  # Usando ddof=1 para muestra
    
    # Mostrar resultados
    print(f"\nEstadísticas de ventas mensuales:")
    print(f"- Promedio: {promedio:.2f}")
    print(f"- Mediana: {mediana:.2f}")
    print(f"- Desviación estándar: {desviacion:.2f}")
    
    # Crear visualización
    plt.figure(figsize=(12, 6))
    plt.bar(meses, ventas_mensuales, color='skyblue', label='Ventas mensuales')
    plt.axhline(y=promedio, color='red', linestyle='--', 
                label=f'Promedio: {promedio:.2f}')
    plt.title('Ventas Mensuales vs Promedio')
    plt.xlabel('Mes')
    plt.ylabel('Ventas')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Guardar gráfico
    ruta_graficos = "graficos"
    Path(ruta_graficos).mkdir(exist_ok=True)
    plt.savefig(f"{ruta_graficos}/ventas_mensuales.png")
    plt.close()
    
    print(f"\nGráfico guardado en: {ruta_graficos}/ventas_mensuales.png")

def main():
    """Función principal."""
    analizar_ventas_mensuales()

if __name__ == "__main__":
    main()
