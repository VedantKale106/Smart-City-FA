from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model/demand_classifier.pkl')
le_from = joblib.load('model/le_from.pkl')
le_to = joblib.load('model/le_to.pkl')
le_day = joblib.load('model/le_day.pkl')
le_time = joblib.load('model/le_time.pkl')
le_event = joblib.load('model/le_event.pkl')
le_demand = joblib.load('model/le_demand.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    suggestion = None
    map_url = ""
    
    selected = {
        'from': '',
        'to': '',
        'day': '',
        'time': '',
        'temp': '',
        'event': ''
    }

    if request.method == 'POST':
        from_stop = request.form['from']
        to_stop = request.form['to']
        day = request.form['day']
        time = request.form['time']
        temp = float(request.form['temp'])
        event = request.form['event']

        selected = {
            'from': from_stop,
            'to': to_stop,
            'day': day,
            'time': time,
            'temp': temp,
            'event': event
        }

        # Predict
        X = pd.DataFrame([[
            le_from.transform([from_stop])[0],
            le_to.transform([to_stop])[0],
            le_day.transform([day])[0],
            le_time.transform([time])[0],
            temp,
            le_event.transform([event])[0]
        ]])

        y_pred = model.predict(X)[0]
        prediction = le_demand.inverse_transform([y_pred])[0]

       

        # Google Maps preview (without API)
        map_url = f"https://www.google.com/maps/dir/{from_stop.replace(' ', '+')}/{to_stop.replace(' ', '+')}"

    return render_template("index.html",
                           places=le_from.classes_, days=le_day.classes_,
                           times=le_time.classes_, events=le_event.classes_,
                           prediction=prediction, map_url=map_url,
                           selected=selected)

if __name__ == '__main__':
    app.run(debug=True)
