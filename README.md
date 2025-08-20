# Análisis de Marketing Bancario - Prueba Técnica

Repositorio que contiene el análisis completo de datos de marketing bancario para predecir la suscripción a depósitos a plazo fijo, desarrollado como parte del proceso de selección para el puesto de Consultor Líder Analítica.

## 🎯 Objetivo
Desarrollar un modelo predictivo que identifique a los clientes con mayor probabilidad de suscribir un depósito a plazo fijo, optimizando así las estrategias de marketing del banco.

## 📊 Presentaciones

### 1. Modelado Predictivo
[![Ver presentación](https://img.shields.io/badge/Ver-Presentación-0078D4?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](1.%20Modelado%20predictivo%20y%20análisis%20de%20datos%20de%20campañas%20de%20marketing%20bancarias.pdf)

### 2. Estrategia Comercial
[![Ver presentación](https://img.shields.io/badge/Ver-Estrategia-0078D4?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](2.%20Estrategia%20Comercial%20para%20Maximizar%20Conversión%20y%20Minimizar%20Costos.pdf)

## 🔍 Hallazgos Clave

### 📈 Rendimiento del Modelo
- **Precisión (Sí)**: 85%
- **Recall (Sí)**: 63%
- **F1-Score (Sí)**: 0.72
- **Exactitud (Accuracy)**: 94%
- **ROC-AUC**: 0.92

### 🎯 Características Principales
1. Duración de la llamada (29.93%)
2. Día del mes (7.71%)
3. Tipo de contacto (7.32%)
4. Balance en cuenta (5.21%)
5. Crédito hipotecario (4.27%)

## 🏗️ Estructura del Proyecto

```
prueba tecnica datecsa/
├── soluciones/
│   ├── 1_analisis_datos/           # Análisis exploratorio y limpieza
│   │   ├── 1.1_limpieza_datos/     # Procesamiento inicial de datos
│   │   └── 1.2_analisis_descriptivo/ # Análisis estadístico descriptivo
│   │
│   ├── 2_modelos_predictivos/      # Modelos de machine learning
│   │   ├── 2.1_regresion_lineal/   # Modelo de regresión lineal
│   │   ├── 2.2_arbol_decision/     # Modelo de árbol de decisión
│   │   └── requirements.txt        # Dependencias para modelos
│   │
│   ├── 3_estrategia_liderazgo_analitica/  # Estrategia de implementación
│   ├── 4_visualizacion_datos/      # Dashboards y visualizaciones
│   └── 5_analisis_bancario/        # Análisis integral del caso bancario
│       ├── analisis_bancario.ipynb # Notebook con el análisis completo
│       ├── graficas/               # Visualizaciones generadas
│       └── catboost_info/          # Información del modelo CatBoost
│
├── src/                            # Código fuente principal
│   ├── __init__.py
│   └── main.py
│
├── .gitignore
├── bank-full.csv                   # Dataset principal
├── requirements.txt               # Dependencias del proyecto
└── README.md
```

## 🚀 Requisitos

- Python 3.9+
- Git
- Jupyter Notebook (opcional, para visualizar los notebooks)

## ⚙️ Configuración

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/jaep321/prueba_tecnica_datecsa.git
   cd prueba_tecnica_datecsa
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el análisis**
   ```bash
   jupyter notebook soluciones/5_analisis_bancario/analisis_bancario.ipynb
   ```

## 📊 Visualizaciones

El análisis incluye visualizaciones detalladas que muestran:
- Matriz de confusión
- Curva ROC y Precision-Recall
- Importancia de variables
- Curvas de aprendizaje y validación

## 📝 Notas Adicionales

- Los datos originales se encuentran en `bank-full.csv`
- El análisis detallado está en `soluciones/5_analisis_bancario/`
- Para replicar el entorno exacto, instalar las dependencias del `requirements.txt`

## 📧 Contacto

Para más información, por favor contactar a joralb93@gmail.com.
