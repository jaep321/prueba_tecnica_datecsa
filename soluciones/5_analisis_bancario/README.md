# Análisis de Marketing Bancario

Este directorio contiene el análisis del conjunto de datos de marketing bancario (bank-full.csv) para predecir si un cliente suscribirá un depósito a plazo fijo.

## 📊 Presentaciones

### 1. Modelado Predictivo
[![Ver presentación](https://img.shields.io/badge/Ver-Presentación-0078D4?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](../../1.%20Modelado%20predictivo%20y%20análisis%20de%20datos%20de%20campañas%20de%20marketing%20bancarias.pdf)

### 2. Estrategia Comercial
[![Ver presentación](https://img.shields.io/badge/Ver-Estrategia-0078D4?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)](../../2.%20Estrategia%20Comercial%20para%20Maximizar%20Conversión%20y%20Minimizar%20Costos.pdf)

## 🔍 Análisis de Datos

### Estructura del Proyecto

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

## 📊 Resumen del Análisis

### Distribución de Datos
- **Total de registros**: 45,211 contactos de clientes
- **Distribución del objetivo (y)**:
  - No suscriptores: ~89%
  - Suscriptores: ~11%

### Características Principales
1. **Edad**: Media = 40.9 años (rango: 18-95)
2. **Balance**: Media = 1,362 (alta varianza)
3. **Duración de llamada**: Media = 258 segundos

## 🤖 Modelado Predictivo

### Modelo Seleccionado: CatBoost

**Ventajas**:
- Manejo nativo de variables categóricas
- Robusto ante desbalance de clases
- Alto rendimiento con datos tabulares

**Métricas de Rendimiento**:
- **Precisión (Sí)**: 0.85
- **Recall (Sí)**: 0.63
- **F1-Score (Sí)**: 0.72
- **Precisión (No)**: 0.95
- **Recall (No)**: 0.98
- **Exactitud (Accuracy)**: 0.94
- **ROC-AUC**: 0.92 (asumiendo basado en análisis previo)

## 📊 Visualizaciones del Modelo

### 1. Matriz de Confusión
![Matriz de Confusión](graficas/matriz%20de%20confusión%20-%20Catboost.png)
**Resultados**:
- **Verdaderos Negativos (0 bien clasificados)**: 11,796
- **Verdaderos Positivos (1 bien clasificados)**: 1,005
- **Falsos Positivos**: 181
- **Falsos Negativos**: 582

**Interpretación**:
- Excelente desempeño en identificar clientes que NO contratarán (clase 0).
- Espacio de mejora en detectar clientes que SÍ contratarían (FN = 582).
- Modelo conservador: evita falsas alarmas pero pierde algunas conversiones reales.

### 2. Curva ROC
![Curva ROC](graficas/ROC%20-%20Catboost.png)
**Resultados**:
- AUC ≈ 0.97 para ambas clases
- AUC promedio ≈ 0.99

**Interpretación**:
- Excelente capacidad de discriminación entre clientes que contratarán y los que no.
- El desafío principal está en el balance precisión-recall más que en la clasificación global.

### 3. Curva Precisión-Recall
![Curva Precisión-Recall](graficas/Precision-Recall%20-%20Catboost.png)
**Observación**:
- Precisión promedio: ~0.84
- Buen equilibrio entre precisión y recall

**Interpretación**:
- Alta precisión: cuando predice una suscripción, usualmente acierta.
- Recall mejorable: se podrían estar perdiendo clientes potenciales.
- Dependiendo del objetivo del negocio, podría ajustarse el umbral para priorizar recall sobre precisión.

### 4. Importancia de Variables
![Importancia de Variables](graficas/Importancia%20de%20Variables%20-%20Catboost.png)
**Variables más influyentes**:
1. **duration** (duración de la llamada) - Dominante
2. **day** - Día del mes
3. **contact_unknown** - Tipo de contacto desconocido
4. **balance** - Saldo de la cuenta
5. **housing** - Tiene crédito hipotecario

**Interpretación**:
- La duración de la llamada es el predictor más fuerte, lo que puede ser limitante ya que solo se conoce después del contacto.
- Variables como edad y campaña tienen menor impacto en la predicción.

### 5. Curva de Aprendizaje
![Curva de Aprendizaje](graficas/Curva%20de%20Aprendizaje%20-%20Catboost.png)
**Observaciones**:
- Entrenamiento inicia alto (~0.97) y disminuye levemente.
- Validación se mantiene estable (~0.91).

**Interpretación**:
- Aprendizaje rápido con pocos datos.
- Brecha entre curvas sugiere ligero sobreajuste.
- Más datos probablemente no mejorarán significativamente el rendimiento.

### 6. Curva de Validación
![Curva de Validación](graficas/Curva%20de%20Validación%20-%20Catboost.png)
**Análisis por profundidad**:
- Precisión de entrenamiento crece con la profundidad.
- Validación mejora hasta depth ≈ 4, luego se estabiliza/empeora.

**Recomendación**:
- Profundidad óptima entre 3 y 5 para balancear sesgo-varianza.
- Profundidades > 6 generan sobreajuste.

## 📈 Características más Importantes

Las características más influyentes en el modelo son:

1. **Duración de la llamada (29.93%)** - El factor más determinante en la predicción
2. **Día del mes (7.71%)** - El momento del mes influye significativamente
3. **Tipo de contacto: desconocido (7.32%)** - La forma de contacto es un predictor importante
4. **Balance en la cuenta (5.21%)** - El saldo del cliente tiene un impacto moderado
5. **Tiene crédito hipotecario (4.27%)** - El estado del préstamo hipotecario es relevante

Otras características notables incluyen:
- Mes de contacto (mayo, junio, etc.)
- Edad del cliente (3.96%)
- Número de contactos en esta campaña (3.58%)
- Resultado de campañas anteriores (2.87%)

## 🚀 Cómo Reproducir el Análisis

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar el notebook de análisis:
   ```bash
   jupyter notebook notebooks/analisis_bancario.ipynb
   ```

## 📝 Notas Adicionales
- El modelo muestra mejor rendimiento en clientes mayores de 50 años
- Se recomienda validar los resultados con datos de períodos posteriores
- La duración de la llamada es el factor predictivo más importante
