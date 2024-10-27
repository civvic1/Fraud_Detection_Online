from flask import Flask, render_template, request
import joblib
import pandas as pd
import random

app = Flask(__name__)
modelo = joblib.load('models/modelo_fraude.pkl')


# Función para convertir período del día en un valor de step
def convertir_periodo_a_step(periodo_dia):
    if periodo_dia == 'Mañana':
        return random.choice([1, 2])
    elif periodo_dia == 'Mediodía':
        return random.choice([3, 4])
    elif periodo_dia == 'Tarde':
        return random.choice([5, 6])
    elif periodo_dia == 'Noche':
        return random.choice([7, 8])
    elif periodo_dia == 'Madrugada':
        return random.choice([9, 10])
    
    

#comentario de caca prueba


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener el período del día seleccionado en el formulario
    periodo_dia = request.form.get('periodo_dia')
    step = convertir_periodo_a_step(periodo_dia)  # Convertir período a valor de step

    # Obtener otros valores del formulario
    amount = request.form.get('amount', 0)
    type_CASH_IN = request.form.get('type_CASH_IN', 0)
    type_CASH_OUT = request.form.get('type_CASH_OUT', 0)
    type_DEBIT = request.form.get('type_DEBIT', 0)
    type_PAYMENT = request.form.get('type_PAYMENT', 0)
    type_TRANSFER = request.form.get('type_TRANSFER', 0)
    type2_CC = request.form.get('type2_CC', 0)
    type2_CM = request.form.get('type2_CM', 0)

    # Crear DataFrame con la transacción de ejemplo
    nueva_transaccion = pd.DataFrame({
        'step': [step],
        'amount': [float(amount)],
        'type_CASH_IN': [int(type_CASH_IN)],
        'type_CASH_OUT': [int(type_CASH_OUT)],
        'type_DEBIT': [int(type_DEBIT)],
        'type_PAYMENT': [int(type_PAYMENT)],
        'type_TRANSFER': [int(type_TRANSFER)],
        'type2_CC': [int(type2_CC)],
        'type2_CM': [int(type2_CM)]
    })

    # Realizar la predicción
    prediccion = modelo.predict(nueva_transaccion)
    resultado = "Fraude" if prediccion[0] == 1 else "No Fraude"

    return render_template('resultado.html', resultado=resultado, periodo_dia=periodo_dia, amount=amount)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
#prueba