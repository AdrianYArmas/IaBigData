from flask import Flask, request, jsonify
import pandas as pd
#import pickle
from utils import creacion_atributos
import json
import xgboost as xgb
import os
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

# Carga del modelo XGBoost desde JSON
modelo = xgb.XGBRegressor()

#modelo.load_model('model.json')
ruta_modelo = os.path.join(os.path.dirname(__file__), 'model.json')
modelo.load_model(ruta_modelo)


atributos = ['dia_semana', 'mes', 'año', 'dia_año', 'trimestre']

# @app.route('/predict', methods=['GET'])
# def predict():
#     fecha = request.args.get('fecha')  # formato YYYY-MM-DD
#     try:
#         fecha_dt = pd.to_datetime(fecha)
#         df = pd.DataFrame(index=[fecha_dt])
#         df = creacion_atributos(df)
#         pred = modelo.predict(df[atributos])[0]
#         return jsonify({"fecha": fecha, "prediccion": round(pred, 2)})
#     except Exception as e:
#         return jsonify({"fecha": fecha, "prediccion": float(round(pred, 2))})

@app.route('/predict_range', methods=['GET'])
def predict_range():
    start_date = request.args.get('start_date')  # YYYY-MM-DD
    end_date = request.args.get('end_date')      # YYYY-MM-DD
    try:
        fechas = pd.date_range(start=start_date, end=end_date)
        resultados = []
        for fecha_dt in fechas:
            df = pd.DataFrame(index=[fecha_dt])
            df = creacion_atributos(df)
            pred = modelo.predict(df[atributos])[0]
            resultados.append({
                "fecha": fecha_dt.strftime('%Y-%m-%d'),
                "prediccion": float(round(pred, 2))
            })
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)