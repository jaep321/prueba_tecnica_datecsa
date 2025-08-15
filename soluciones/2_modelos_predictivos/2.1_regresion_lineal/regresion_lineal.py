import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

def generar_datos_ejemplo():
    """Genera datos de ejemplo de horas de estudio vs calificaciones."""
    np.random.seed(42)
    horas_estudio = np.random.uniform(1, 10, 100)
    ruido = np.random.normal(0, 5, 100)
    calificaciones = 30 + 5 * horas_estudio + ruido
    return horas_estudio.reshape(-1, 1), calificaciones

def entrenar_modelo_regresion(X, y):
    """Entrena un modelo de regresión lineal."""
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
    """Predice la calificación para un número dado de horas de estudio."""
    return modelo.predict([[horas_estudio]])[0]

def visualizar_regresion(X, y, modelo, r2):
    """Visualiza los datos y la línea de regresión."""
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

def main():
    # Generar y preparar datos
    X, y = generar_datos_ejemplo()
    
    # Entrenar modelo
    modelo, r2, X_entrenamiento, y_entrenamiento, X_prueba, y_prueba = entrenar_modelo_regresion(X, y)
    
    # Realizar predicción para 5 horas de estudio
    horas_ejemplo = 5
    prediccion = predecir_calificacion(modelo, horas_ejemplo)
    
    # Mostrar resultados
    print(f"\nResultados del Modelo de Regresión Lineal")
    print("-" * 40)
    print(f"Coeficiente (pendiente): {modelo.coef_[0]:.2f}")
    print(f"Intercepto: {modelo.intercept_:.2f}")
    print(f"R² Score: {r2:.4f}")
    print(f"\nPredicción para {horas_ejemplo} horas de estudio: {prediccion:.2f}")
    
    # Visualización
    visualizar_regresion(X, y, modelo, r2)
    print("\nGráfico de regresión guardado como 'regresion_lineal.png'")

if __name__ == "__main__":
    main()
