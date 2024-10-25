from flask import Flask, render_template, request
import joblib
import pandas as pd

# Inicializa la aplicación Flask
app = Flask(__name__)

# Cargar el modelo
modelo = joblib.load('modelo_fraude.pkl')

# Ruta principal para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para predecir el fraude
@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener los valores enviados desde el formulario
    step = request.form['step']
    amount = request.form['amount']
    type_TRANSFER = request.form['type_TRANSFER']
    type_CASH_OUT = request.form['type_CASH_OUT']
    
    # Crear un DataFrame con los datos ingresados
    nueva_transaccion = pd.DataFrame({
        'step': [float(step)],
        'amount': [float(amount)],
        'type_TRANSFER': [int(type_TRANSFER)],
        'type_CASH_OUT': [int(type_CASH_OUT)]
        # Agregar más columnas si es necesario
    })

    # Realizar la predicción
    prediccion = modelo.predict(nueva_transaccion)

    # Mostrar el resultado
    if prediccion[0] == 1:
        resultado = "La transacción es fraudulenta"
    else:
        resultado = "La transacción no es fraudulenta"
    
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
