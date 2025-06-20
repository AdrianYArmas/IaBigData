# -*- coding: utf-8 -*-
"""Analisis_Predictivo_Churnv2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F-JH3MllWLgI9tz9omceLJkO8rOHrt9s

# Análisis Predictivo: Fuga de Clientes en Telecomunicaciones

Este cuaderno tiene como objetivo explorar un caso real de predicción de fuga de clientes usando un árbol de decisión.

## Objetivo
Reflexionar sobre el uso de modelos predictivos y prescriptivos para tomar decisiones empresariales.

📌 **Nota:** No es necesario programar. Simplemente ejecuta las celdas y reflexiona sobre las preguntas propuestas.
"""

# Cargar librerías
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Cargar datos desde GitHub
url = "https://raw.githubusercontent.com/taruntiwarihp/dataSets/master/telecom_churn.csv"
df = pd.read_csv(url)
df.head()

"""## ¿Qué representan estos datos?
- Cada fila representa un cliente.
- Las columnas muestran información sobre su uso de servicios, gastos y si se dio de baja (`Churn`).

### 💬 Reflexión:
¿Qué variables crees que podrían influir más en que un cliente se dé de baja?

### Respuesta:
Las variables que considero que más afectan son las siguientes; Customer service calls, ya que define un descontento debido al alto número de interacciones suele reflejar insatisfacción o problemas no resueltos; international plan, quienes tienen este extra pagan más y, si no lo utilizan, pueden sentirse frustrados por el coste adicional; Total day minutes  y cargos asociados Total day charge. ya que un uso muy elevado puede derivar en facturas inesperadamente altas; Voice mail plan, la ausencia de este servicio básico, o el tenerlo y no usarlo, puede señalar que el cliente no percibe valor; Total eve minutes, Total night minutes, patrones de uso desequilibrados pueden indicar insatisfacción con la tarifa diurna o falta de flexibilidad en los planes
"""

# Preprocesamiento mínimo (automático)
df.drop(["State", "Area code", "Phone"], axis=1, inplace=True, errors='ignore')
df["Churn"] = df["Churn"].astype(int)
df = pd.get_dummies(df, drop_first=True)

X = df.drop("Churn", axis=1)
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamiento y predicción con árbol de decisión
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

"""### 💬 Reflexión:

#### 💬 Pregunta:
- ¿El modelo predice bien los clientes que se dan de baja?

#### Respuesta:
El modelo predice bastante bien, ya que cuenta con una alta precisión pese a tener un punto negativo del que hablaré en la siguiente pregunta.


#### 💬 Pregunta:
- ¿Qué errores comete? ¿Qué consecuencias tendría para la empresa?

#### Respuesta:
Los identifica muy bien, ya que tiene una alta precisión y recall, pero en la clase 1 el 33 % de los clientes que finalmente abandonan no son detectados por el modelo lo que puede derivar en falsos positivos o falsos negativvos, y destinar recursos a casos innecesarios y no destinarlo a casos que lo requieren.


#### 💬 Pregunta:
- ¿Preferirías minimizar los falsos positivos o los falsos negativos?

#### Respuesta:
En un contexto de retención de clientes, es generalmente más costoso perder un cliente valioso que ofrecer un descuento o atención extra a quien no lo necesita.
Por tanto, priorizaría reducir los falsos negativos, es decir, incrementar el recall de la clase 1 incluso a costa de aumentar ligeramente los falsos positivos podría ser una estrategia a seguir o al menos a plantear.

## De la predicción a la acción: Análisis prescriptivo

Supón que detectas que clientes con muchas llamadas al servicio de atención tienden a darse de baja.

### 💬 Reflexión
#### 💬 Pregunta:
- ¿Qué acción podrías recomendar a la empresa?

#### Respuesta:
Para reducir la fuga de clientes, es importante actuar con anticipación. Yo propondría activar alertas cuando un cliente llama varias veces en poco tiempo, permitiendo que un agente especializado lo contacte y resuelva su problema de manera prioritaria, antes de que se agrave. Además, enviar encuestas rápidas después de cada interacción ayuda a medir la satisfacción y detectar puntos débiles. Por último, contar con agentes capacitados en retención permite ofrecer soluciones efectivas —como descuentos o cambios de plan— justo cuando el cliente más lo necesita, además de tener en cuenta que estos descuentos podrían ser dentro de un varemo investigado con los datos del cliente y procesados con un modelo.


#### 💬 Pregunta:
- ¿Cómo podrías personalizar la oferta o el servicio?

#### Respuesta:
Para mejorar la retención, es clave personalizar la experiencia del cliente. Por ejemplo, si alguien utiliza muchas llamadas durante el día, se le podría ofrecer un plan con más minutos o tarifa plana por un tiempo de prueba. También es útil brindar atención prioritaria a clientes que han tenido muchos problemas, con una línea directa y agentes capacitados para resolver rápidamente. Y para fortalecer la lealtad, se pueden otorgar puntos cada vez que un cliente cierre una incidencia con éxito, los cuales luego se canjeen por beneficios como datos extra o puntos de canje de la compañía. Para esto es prioritario un análisis del perfil del usuario, que hoy en día sería más sencillo hacerlo a través de la inteligencia artificial e ia.




Este tipo de análisis ayuda a mejorar la toma de decisiones estratégicas con base en los datos.
"""