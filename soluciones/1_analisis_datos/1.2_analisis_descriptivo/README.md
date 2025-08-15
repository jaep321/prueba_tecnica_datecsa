# 1.2 Análisis Descriptivo de Datos

## Descripción
Este directorio contiene el análisis descriptivo de los datos limpios generados en el ejercicio 1.1. El análisis incluye estadísticas descriptivas, visualizaciones y análisis de correlaciones para comprender mejor los patrones en los datos de ventas.

## Estructura
- `analisis_descriptivo.py`: Script principal que realiza el análisis
- `graficos/`: Directorio que contiene las visualizaciones generadas
  - `histograma_montos.png`: Distribución de los montos de compra
  - `boxplot_productos.png`: Comparación de montos por producto
  - `serie_temporal.png`: Evolución de las compras en el tiempo
  - `correlaciones.png`: Mapa de calor de correlaciones
- `README.md`: Este archivo con la documentación

## Requisitos
- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- python-dateutil

## Instalación
1. Asegúrate de tener instalado Python 3.8 o superior
2. Instala las dependencias necesarias:
   ```bash
   pip install pandas numpy matplotlib seaborn python-dateutil
   ```

## Uso
1. Asegúrate de que el archivo de datos limpios exista en la ruta `../1.1_limpieza_datos/datos/datos_limpios.csv`
2. Ejecuta el script de análisis:
   ```bash
   python analisis_descriptivo.py
   ```
3. Los resultados se mostrarán en la consola y las visualizaciones se guardarán en el directorio `graficos/`

## Análisis Realizado

### 1. Estadísticas Descriptivas
- Resumen estadístico de variables numéricas
- Conteo de compras por producto
- Estadísticas de montos de compra por producto

### 2. Visualizaciones
- **Histograma de montos de compra**: Muestra la distribución de los montos de compra
- **Boxplot por producto**: Compara la distribución de montos entre diferentes productos
- **Serie temporal**: Muestra la evolución de las compras a lo largo del tiempo
- **Mapa de calor de correlaciones**: Muestra las correlaciones entre variables numéricas

### 3. Análisis de Correlaciones
- Matriz de correlación entre variables numéricas
- Identificación de relaciones lineales entre variables

## Resultados Esperados
Al ejecutar el script, se generará un informe en la consola con las estadísticas descriptivas y se crearán las siguientes visualizaciones en el directorio `graficos/`:

### Estadísticas Clave de Ventas
- **Promedio de ventas**: 99.42
- **Mediana de ventas**: 95.85
- **Desviación estándar**: 28.14

### Visualizaciones Generadas
1. `histograma_montos.png`: Distribución de los montos de compra
2. `boxplot_productos.png`: Comparación de montos por categoría de producto
3. `serie_temporal.png`: Evolución temporal de las compras
4. `correlaciones.png`: Mapa de calor de correlaciones entre variables

### Análisis por Producto
- **Producto A**:
  - Promedio: 98.53
  - Desviación estándar: 15.07
  - Cantidad: 7 compras
  
- **Producto B**:
  - Promedio: 105.32
  - Desviación estándar: 13.81
  - Cantidad: 4 compras
  
- **Producto C**:
  - Promedio: 96.53
  - Desviación estándar: 45.91
  - Cantidad: 6 compras

## Notas Adicionales
- El script asume que los datos de entrada están en formato CSV con las columnas: ID_cliente, Nombre, Fecha_de_compra, Monto_compra y Producto.
- Las fechas deben estar en un formato reconocible por pandas.
- Los valores faltantes deben ser manejados previamente en la etapa de limpieza de datos.
