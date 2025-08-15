# Modelo de Regresión Lineal

Este directorio contiene la implementación de un modelo de regresión lineal que predice las calificaciones de los estudiantes en función de las horas de estudio.

## Descripción

El modelo de regresión lineal se utiliza para predecir la calificación que obtendrá un estudiante basándose en la cantidad de horas que ha estudiado. El modelo se entrena con datos de ejemplo y proporciona una predicción junto con métricas de rendimiento.

## Resultados del Modelo

Al ejecutar el script, se obtienen los siguientes resultados:

```
Resultados del Modelo de Regresión Lineal
----------------------------------------
Coeficiente (pendiente): 4.78
Intercepto: 30.94
R² Score: 0.9120

Predicción para 5 horas de estudio: **54.82**

Predicciones para las primeras horas de estudio:
+--------------------+-------------------------+
| Horas de Estudio  | Calificación Predicha  |
+====================+=========================+
| 1 hora            | 35.71                  |
+--------------------+-------------------------+
| 2 horas           | 40.49                  |
+--------------------+-------------------------+
| 3 horas           | 45.27                  |
+--------------------+-------------------------+
| 4 horas           | 50.05                  |
+--------------------+-------------------------+
| 5 horas           | 54.82                  |
+--------------------+-------------------------+
| 6 horas           | 59.60                  |
+--------------------+-------------------------+
| 7 horas           | 64.38                  |
+--------------------+-------------------------+
| 8 horas           | 69.15                  |
+--------------------+-------------------------+
| 9 horas           | 73.93                  |
+--------------------+-------------------------+
| 10 horas          | 78.71                  |
+--------------------+-------------------------+

```

### Interpretación de los Resultados

- **Coeficiente (4.78)**: Por cada hora adicional de estudio, se espera un aumento de aproximadamente 4.78 puntos en la calificación.
- **Intercepto (30.94)**: La calificación esperada cuando no se estudia (0 horas).
- **R² Score (0.912)**: El modelo explica aproximadamente el 91.2% de la variabilidad en las calificaciones, lo que indica un excelente ajuste a los datos.

### Gráfico de Regresión

El archivo `regresion_lineal.png` muestra la relación entre las horas de estudio y las calificaciones, junto con la línea de regresión ajustada.

![Gráfico de Regresión Lineal](regresion_lineal.png)

## Requisitos

- Python 3.6+
- Bibliotecas requeridas (instalables con `pip install -r requirements.txt`):
  - numpy
  - pandas
  - scikit-learn
  - matplotlib
  - tabulate

## Uso

1. Instale las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecute el script:
   ```bash
   python regresion_lineal.py
   ```

3. El script generará:
   - Estadísticas del modelo (coeficiente, intercepto, R²)
   - Tabla de predicciones para las primeras 10 horas
   - Un gráfico de dispersión con la línea de regresión guardado como `regresion_lineal.png`

## Personalización

Para usar sus propios datos, modifique la función `generar_datos_ejemplo()` en el script para cargar su conjunto de datos. Asegúrese de que los datos estén en el formato correcto (horas de estudio como variable independiente, calificaciones como variable dependiente).

## Notas Técnicas

- El modelo utiliza una división 80/20 para entrenamiento y prueba.
- Se utiliza una semilla aleatoria (random_state=42) para garantizar resultados reproducibles.
- La tabla de predicciones muestra cómo aumenta la calificación esperada con cada hora adicional de estudio.
