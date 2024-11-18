# 🚀 Detección de Fraude Financiero 💳🔍

📋 Descripción
Este proyecto implementa un sistema de detección de fraude financiero utilizando algoritmos de Machine Learning para identificar transacciones sospechosas. Desarrollado como parte del @Bootcamp Xperience, fue guiado por los profesores Alejandro Gamarra y Silvia Branco. El sistema se ha desplegado en Google Cloud utilizando Flask, permitiendo análisis en tiempo real y proporcionando predicciones sobre posibles fraudes financieros.

## 🛠️ Tecnologías Utilizadas
- Python 🐍: Lenguaje principal para el desarrollo del modelo y la aplicación.
- Flask 🌐: Framework para crear la interfaz web y el API del modelo.
- Scikit-learn 🤖: Biblioteca para el desarrollo y evaluación de los modelos de Machine Learning.
- Google Cloud Platform ☁️: Servicio de nube utilizado para el despliegue del modelo.
- Pandas y NumPy 📊: Herramientas para manipulación y análisis de datos.
- Matplotlib y Seaborn 📈: Librerías para visualización de datos.
  
## 📦 Estructura del Proyecto
- data/: Contiene el dataset de ejemplo.
- models/: Almacena el modelo entrenado.
- templates/ y static/: Archivos HTML y CSS para la interfaz de usuario.
- app.py: Código principal de la aplicación Flask.
- requirements.txt: Lista de dependencias necesarias para el proyecto.

## ⚙️ Instalación
Sigue estos pasos para ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio
- bash
- Copiar código
- git clone https://github.com/tu_usuario/deteccion_fraude_financiero.git
- cd deteccion_fraude_financiero

### 2. Crear un entorno virtual e instalar dependencias
- bash
- Copiar código
- python -m venv venv
- source venv/bin/activate  # En Windows: venv\Scripts\activate
- pip install -r requirements.txt
  
### 3. Ejecutar la aplicación
- bash
- Copiar código
- python app.py
- Accede a la aplicación en http://localhost:5000.

## 📊 Dataset
El dataset utilizado contiene información sobre transacciones financieras. Algunos campos importantes son:
- step: Tiempo en días desde el inicio del análisis.
- type: Tipo de transacción (e.g., 'TRANSFER', 'CASH_OUT').
- amount: Monto de la transacción.
- oldbalanceOrg: Saldo de la cuenta antes de la transacción.
- newbalanceOrig: Saldo de la cuenta después de la transacción.
- isFraud: Indica si la transacción es fraudulenta (1) o no (0).

## 🧠 Modelos y Métodos
El modelo se entrenó utilizando técnicas de Machine Learning supervisado. Se exploraron varios algoritmos, entre ellos:
- Regresión Logística
- Árboles de Decisión
- Random Forest
Después de la evaluación, se seleccionó el modelo con mejor rendimiento basado en métricas como precisión, recall y f1-score.

## 🚀 Despliegue en Google Cloud
- El proyecto se implementó en Google Cloud Compute Engine, utilizando una máquina virtual configurada con Flask para manejar solicitudes de predicción en tiempo real.
- [ https://fraude2-767384775947.europe-west10.run.app/](https://fraude2-767384775947.europe-west10.run.app/)


## 📈 Resultados
El modelo alcanzó un 98% de precisión en el conjunto de validación, con una tasa baja de falsos positivos, lo que indica una alta capacidad para detectar transacciones fraudulentas sin afectar a las transacciones legítimas.

## 🤝 Colaboradores:
- Víctor (Líder del proyecto)
- Alejandra Cruz
- Mario José Arellano
- Fernanda Cader
- Ignacio
- Nestor Saenz
- Wilfer Alexandre

## Agradecimientos especiales para:
- Alejandro Gamarra instructor del bootcamp
- Silvia Branco especialista de RRHH

