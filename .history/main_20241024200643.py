
import pandas as pd
from flask import Flask, render_template, request
import joblib
import pandas as pd

# Inicializa la aplicación Flask
app = Flask(__name__)

# Cargar el modelo
modelo = joblib.load('models/modelo_fraude.pkl')

# Ruta principal para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para predecir el fraude
@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener los valores enviados desde el formulario
    step = request.form.get('step', 0)
    amount = request.form.get('amount', 0)
    type_TRANSFER = request.form.get('type_TRANSFER', 0)
    type_CASH_OUT = request.form.get('type_CASH_OUT', 0)
    
    # Asignar valores por defecto a las columnas que faltan
    type_CASH_IN = request.form.get('type_CASH_IN', 0)
    type_DEBIT = request.form.get('type_DEBIT', 0)
    type_PAYMENT = request.form.get('type_PAYMENT', 0)
    type2_CC = request.form.get('type2_CC', 0)
    type2_CM = request.form.get('type2_CM', 0)

    # Crear un DataFrame con los datos ingresados y rellenar columnas faltantes
    nueva_transaccion = pd.DataFrame({
        'step': [float(step)],
        'amount': [float(amount)],
        'type_CASH_IN': [int(type_CASH_IN)],
        'type_CASH_OUT': [int(type_CASH_OUT)],
        'type_DEBIT': [int(type_DEBIT)],
        'type_PAYMENT': [int(type_PAYMENT)],
        'type_TRANSFER': [int(type_TRANSFER)],
        'type2_CC': [int(type2_CC)],
        'type2_CM': [int(type2_CM)]
    })
    
    resultado = "La transacción ha sido recibida, pero aún no se ha aplicado un modelo."

    # Pasar los datos del formulario a la página resultado.html
    return render_template('resultado.html', 
                           resultado=resultado, 
                           step=step, 
                           amount=amount, 
                           type_CASH_IN=type_CASH_IN, 
                           type_CASH_OUT=type_CASH_OUT,
                           type_DEBIT=type_DEBIT,
                           type_PAYMENT=type_PAYMENT,
                           type_TRANSFER=type_TRANSFER,
                           type2_CC=type2_CC,
                           type2_CM=type2_CM)
    
    
    """ 
    # Realizar la predicción
    prediccion = modelo.predict(nueva_transaccion)

    # Mostrar el resultado
    if prediccion[0] == 1:
        resultado = "La transacción es fraudulenta"
    else:
        resultado = "La transacción no es fraudulenta"
    
    return render_template('resultado.html', resultado=resultado)
    """
    
    
if __name__ == '__main__':
    app.run(debug=True)
