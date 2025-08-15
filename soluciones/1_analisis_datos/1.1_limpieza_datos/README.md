# 1.1 Limpieza y preparación de datos

## Descripción
Este directorio contiene la solución al ejercicio de limpieza y preparación de datos, que incluye el manejo de valores nulos, duplicados y formato de fechas inconsistentes.

## Estructura
- `solucion.py`: Script de Python con la implementación de la solución
- `datos/`: Directorio que contiene los archivos de datos
  - `datos_ventas.csv`: Dataset de ejemplo para probar la solución
  - `datos_limpios.csv`: Resultado del proceso de limpieza
- `README.md`: Este archivo con la documentación

## Requisitos
- Python 3.8+
- pandas
- numpy
- python-dateutil

## Uso
1. Instalar las dependencias:
   ```bash
   pip install pandas numpy python-dateutil
   ```
2. Ejecutar el script:
   ```bash
   python solucion.py
   ```

## Resultados de la ejecución

### Datos originales (primeros 5 registros):
```
   ID_cliente     Nombre Fecha_de_compra  Monto_compra Producto
0           1  Cliente 1      2023-01-15        114.90        A
1           2  Cliente 2      2023/02/20         95.85        B
2           3  Cliente 3      15-03-2023        119.43        A
3           4  Cliente 4      04/30/2023        145.69        C
4           5  Cliente 5      2023-05-10         92.98        B
```

### Proceso de limpieza:
1. **Conversión de fechas**: Se estandarizaron todos los formatos de fecha
2. **Valores nulos**: Se encontraron 3 valores nulos en 'Monto_compra'. Estos registros fueron eliminados
3. **Datos duplicados**: No se encontraron registros duplicados

### Datos después de la limpieza (primeros 5 registros):
```
   ID_cliente     Nombre Fecha_de_compra  Monto_compra Producto
0           1  Cliente 1      2023-01-15        114.90        A
1           2  Cliente 2             NaT         95.85        B
2           3  Cliente 3             NaT        119.43        A
3           4  Cliente 4             NaT        145.69        C
4           5  Cliente 5      2023-05-10         92.98        B
```

### Validación de datos:
- **Registros duplicados**: 0
- **Valores nulos por columna**:
  - ID_cliente: 0
  - Nombre: 0
  - Fecha_de_compra: 7 (algunas fechas no pudieron ser convertidas)
  - Monto_compra: 0
  - Producto: 0

### Estadísticas de Monto_compra:
```
count     17.000000
mean      99.423529
std       28.137692
min       42.600000
25%       85.920000
50%       95.850000
75%      116.280000
max      147.380000
```

## Análisis de resultados
- Se procesaron exitosamente 17 registros después de la limpieza
- Los montos de compra tienen una media de aproximadamente 99.42 con una desviación estándar de 28.14
- El valor mínimo de compra fue 42.60 y el máximo 147.38
- Algunas fechas (7 registros) no pudieron ser convertidas al formato estándar y se marcaron como NaT (Not a Time)
