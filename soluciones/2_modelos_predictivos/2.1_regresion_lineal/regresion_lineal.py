import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from tabulate import tabulate

def generar_datos_ejemplo():
    np.random.seed(42)
    horas_estudio = np.random.uniform(1, 10, 100)
    ruido = np.random.normal(0, 5, 100)
    calificaciones = 30 + 5 * horas_estudio + ruido
    return horas_estudio.reshape(-1, 1), calificaciones

def entrenar_modelo_regresion(X, y):
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    modelo = LinearRegression()
    modelo.fit(X_entrenamiento, y_entrenamiento)
    
    # Evaluación
    y_pred = modelo.predict(X_prueba)
    r2 = r2_score(y_prueba, y_pred)
    
    return modelo, r2, X_entrenamiento, y_entrenamiento, X_prueba, y_prueba

def predecir_calificacion(modelo, horas_estudio):
    return modelo.predict([[horas_estudio]])[0]

def visualizar_regresion(X, y, modelo, r2):
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', label='Datos reales')
    
    # Línea de regresión
    x_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_pred = modelo.predict(x_range)
    plt.plot(x_range, y_pred, color='red', label=f'Regresión Lineal (R² = {r2:.3f})')
    
    plt.title('Horas de Estudio vs Calificaciones')
    plt.xlabel('Horas de Estudio')
    plt.ylabel('Calificación')
    plt.legend()
    plt.grid(True)
    plt.savefig('regresion_lineal.png')
    plt.close()

def mostrar_tabla_predicciones(modelo, max_horas=10):
    horas = list(range(1, max_horas + 1))
    # Predecir calificaciones para cada hora
    predicciones = [predecir_calificacion(modelo, h) for h in horas]
    
    # Crear tabla
    tabla = []
    for h, p in zip(horas, predicciones):
        tabla.append([f"{h} hora{'s' if h > 1 else ''}", f"{p:.2f}"])
    
    # Mostrar tabla
    print("\nPredicciones para las primeras horas de estudio:")
    print(tabulate(tabla, headers=["Horas de Estudio", "Calificación Predicha"], tablefmt="grid"))

def main():
    # Generar y preparar datos
    X, y = generar_datos_ejemplo()
    
    # Entrenar modelo
    modelo, r2, X_entrenamiento, y_entrenamiento, X_prueba, y_prueba = entrenar_modelo_regresion(X, y)
    
    # Mostrar resultados
    print(f"\nResultados del Modelo de Regresión Lineal")
    print("-" * 40)
    print(f"Coeficiente (pendiente): {modelo.coef_[0]:.2f}")
    print(f"Intercepto: {modelo.intercept_:.2f}")
    print(f"R² Score: {r2:.4f}")
    
    # Mostrar tabla de predicciones
    mostrar_tabla_predicciones(modelo)
    
    # Realizar predicción para 5 horas de estudio
    horas_ejemplo = 5
    prediccion = predecir_calificacion(modelo, horas_ejemplo)
    print(f"\nPredicción para {horas_ejemplo} horas de estudio: {prediccion:.2f}")
    
    # Visualización
    visualizar_regresion(X, y, modelo, r2)
    print("\nGráfico de regresión guardado como 'regresion_lineal.png'")

if __name__ == "__main__":
    main()
