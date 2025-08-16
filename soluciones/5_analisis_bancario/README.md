# Análisis de Marketing Bancario

Este directorio contiene el análisis del conjunto de datos de marketing bancario (bank-full.csv) para predecir si un cliente suscribirá un depósito a plazo fijo.

## 📊 Presentaciones

### 1. Modelado Predictivo
[![Ver presentación](https://img.shields.io/badge/Ver-Presentación-0078D4?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](../../1.%20Modelado%20predictivo%20y%20análisis%20de%20datos%20de%20campañas%20de%20marketing%20bancarias.pdf)

### 2. Estrategia Comercial
[![Ver presentación](https://img.shields.io/badge/Ver-Estrategia-0078D4?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](../../2.%20Estrategia%20Comercial%20para%20Maximizar%20Conversión%20y%20Minimizar%20Costos.pdf)

## Estructura del Proyecto

- `data/`: Contiene los datos originales y procesados
  - `raw/`: Datos originales (bank-full.csv)
  - `processed/`: Datos procesados para el análisis
- `notebooks/`: Cuadernos de Jupyter con el análisis
  - `1_exploracion_datos.ipynb`: Análisis exploratorio de datos
  - `2_modelado_prediccion.ipynb`: Modelado predictivo
- `src/`: Código fuente
  - `data_processing.py`: Funciones para el procesamiento de datos
  - `model.py`: Funciones para el modelado predictivo
  - `visualization.py`: Funciones para visualización de datos
- `results/`: Resultados del análisis
  - `figures/`: Gráficos generados
  - `models/`: Modelos entrenados
  - `reports/`: Informes generados

## Requisitos

- Python 3.8+
- Bibliotecas listadas en `requirements.txt`

## Uso

1. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
2. Ejecutar los cuadernos en orden:
   - `notebooks/1_exploracion_datos.ipynb`
   - `notebooks/2_modelado_prediccion.ipynb`

## Descripción del Conjunto de Datos

El conjunto de datos contiene información de campañas de marketing directo de una institución bancaria. El objetivo es predecir si el cliente suscribirá un depósito a plazo fijo (variable 'y').

### Variables

- **Variables de entrada:**
  - `age`: Edad
  - `job`: Tipo de trabajo
  - `marital`: Estado civil
  - `education`: Nivel de educación
  - `default`: ¿Tiene crédito en mora?
  - `balance`: Saldo promedio anual en euros
  - `housing`: ¿Tiene préstamo de vivienda?
  - `loan`: ¿Tiene préstamo personal?
  - `contact`: Medio de contacto
  - `day`: Día del mes del último contacto
  - `month`: Mes del último contacto
  - `duration`: Duración del último contacto en segundos
  - `campaign`: Número de contactos realizados durante esta campaña
  - `pdays`: Número de días que pasaron desde que el cliente fue contactado por última vez
  - `previous`: Número de contactos realizados antes de esta campaña
  - `poutcome`: Resultado de la campaña de marketing anterior

- **Variable objetivo:**
  - `y`: ¿El cliente suscribió un depósito a plazo fijo? (binario: 'si' o 'no')
