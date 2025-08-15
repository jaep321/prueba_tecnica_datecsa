import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def generar_datos_cliente():
    """Genera datos de ejemplo de clientes con edad, ingreso y si realizaron una compra."""
    np.random.seed(42)
    n_muestras = 200
    
    # Generar edades entre 18 y 70 años
    edades = np.random.randint(18, 71, n_muestras)
    
    # Generar ingresos anuales entre 20k y 150k
    ingresos = np.random.uniform(20000, 150000, n_muestras)
    
    # Crear variable objetivo (1 = compra, 0 = no compra)
    # La probabilidad de compra aumenta con la edad y el ingreso
    prob_compra = 1 / (1 + np.exp(-(0.05 * (edades - 40) + 0.00001 * (ingresos - 50000))))
    compras = (prob_compra > np.random.random(n_muestras)).astype(int)
    
    # Crear DataFrame
    datos = pd.DataFrame({
        'Edad': edades,
        'Ingreso': ingresos,
        'Compro': compras
    })
    
    return datos

def entrenar_arbol_decision(X, y):
    """Entrena un modelo de árbol de decisión y devuelve el modelo y las métricas."""
    # Dividir los datos
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Crear y entrenar el modelo
    arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
    arbol.fit(X_entrenamiento, y_entrenamiento)
    
    # Hacer predicciones
    y_pred = arbol.predict(X_prueba)
    
    # Calcular precisión
    precision = accuracy_score(y_prueba, y_pred)
    
    return arbol, precision, X_entrenamiento, y_entrenamiento, X_prueba, y_prueba

def visualizar_arbol(modelo, caracteristicas):
    """Visualiza el árbol de decisión."""
    plt.figure(figsize=(20,10))
    plot_tree(
        modelo,
        feature_names=caracteristicas,
        class_names=['No Compró', 'Compró'],
        filled=True,
        rounded=True,
        proportion=True
    )
    plt.savefig('arbol_decision.png', bbox_inches='tight')
    plt.close()

def predecir_nuevo_cliente(modelo, edad, ingreso):
    """Predice si un nuevo cliente realizará una compra."""
    # Crear un DataFrame con los nombres de las características
    datos_cliente = pd.DataFrame({
        'Edad': [edad],
        'Ingreso': [ingreso]
    })
    prediccion = modelo.predict(datos_cliente)
    return "Comprará" if prediccion[0] == 1 else "No comprará"

def main():
    # Generar y preparar datos
    datos = generar_datos_cliente()
    X = datos[['Edad', 'Ingreso']]
    y = datos['Compro']
    
    # Entrenar modelo
    arbol, precision, X_entrenamiento, y_entrenamiento, X_prueba, y_prueba = entrenar_arbol_decision(X, y)
    
    # Mostrar resultados
    print("\nResultados del Modelo de Árbol de Decisión")
    print("-" * 50)
    print(f"Precisión del modelo: {precision:.4f}")
    
    # Mostrar importancia de características
    print("\nImportancia de las características:")
    for nombre, importancia in zip(X.columns, arbol.feature_importances_):
        print(f"{nombre}: {importancia:.4f}")
    
    # Realizar predicción para nuevos clientes
    print("\nPredicción para nuevos clientes:")
    print(f"- Cliente de 30 años con ingreso de $40,000: {predecir_nuevo_cliente(arbol, 30, 40000)}")
    print(f"- Cliente de 50 años con ingreso de $100,000: {predecir_nuevo_cliente(arbol, 50, 100000)}")
    
    # Visualizar el árbol
    visualizar_arbol(arbol, X.columns)
    print("\nVisualización del árbol guardada como 'arbol_decision.png'")

if __name__ == "__main__":
    main()
