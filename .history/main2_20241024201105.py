from flask import Flask, render_template, request
import joblib
import pandas as pd

# Inicializa la aplicación Flask
app = Flask(__name__)

# Cargar el modelo (si es necesario)
# modelo = joblib.load('modelo_fraude.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    # Recibir los datos del formulario
    step = request.form.get('step', 0)
    amount = request.form.get('amount', 0)
    type_CASH_IN = request.form.get('type_CASH_IN', 0)
    type_CASH_OUT = request.form.get('type_CASH_OUT', 0)
    type_DEBIT = request.form.get('type_DEBIT', 0)
    type_PAYMENT = request.form.get('type_PAYMENT', 0)
    type_TRANSFER = request.form.get('type_TRANSFER', 0)
    type2_CC = request.form.get('type2_CC', 0)
    type2_CM = request.form.get('type2_CM', 0)

    # Crear un DataFrame para pasar al modelo
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

    # Si deseas usar el modelo para predecir
    # prediccion = modelo.predict(nueva_transaccion)
    # resultado = "fraudulenta" si prediccion[0] == 1 else "no fraudulenta"
    
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

if __name__ == '__main__':
    app.run(debug=True)
