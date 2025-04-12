# Smart City Transit Predictor - My Awesome FA! 🚌 

Yo! 👋 This is my Smart City Final Assessment project. It's all about predicting public transit demand in a smart way.

## What's Inside

Here's the lowdown on what you'll find in this repo:

* `app.py`:  This is where all the Flask magic happens. It's the web app that takes user inputs and spits out predictions. [cite: 56, 57, 58, 59, 60, 61]
* `dataset_generate.py`:  A handy script to generate a synthetic dataset (`pcmctransit.csv`) with realistic transit demand patterns. [cite: 61, 62, 63, 64, 65]
* `pcmctransit.csv`: The dataset used for training the prediction model. It's got info on routes, times, days, temperature, events, and demand levels. [cite: 65]
* `train_model.py`:  The script to train the machine learning model that predicts transit demand.  (You'll find the trained model files in the `model/` directory.)
* `model/`:  This folder contains the trained model (`demand_classifier.pkl`) and the label encoder files (`le_*.pkl`). [cite: 55]
* `templates/`:  Contains the HTML template (`index.html`) for the web interface. [cite: 55, 56, 57, 58, 59, 60, 61]

## How It Works

The main idea is to predict how much demand there will be for public transport based on factors like:

* Where people are going "from" and "to" [cite: 56, 57, 58, 59]
* The day of the week [cite: 56, 57, 58, 59]
* Time of day [cite: 56, 57, 58, 59]
* Temperature [cite: 56, 57, 58, 59]
* Whether there's an event happening [cite: 56, 57, 58, 59]

The `dataset_generate.py` script creates a dataset with some smart rules to make it realistic.  Then, the `train_model.py` script uses this data to train a model.  Finally, the `app.py` uses the trained model to predict demand and show it on a webpage. [cite: 61, 62, 63, 64, 65, 56, 57, 58, 59, 60, 61]

## Cool Features

* **Demand Prediction:** Predicts transit demand levels (Low, Medium, High). [cite: 59, 60]
* **Google Maps Preview:** Shows a quick Google Maps link for the route (just a preview, not a full-on integration). [cite: 60]
* **User-Friendly Web Interface:** You can easily enter the parameters and see the prediction. [cite: 56, 57, 58, 59, 60, 61]

## Get Started

1.  Clone the repo.
2.  Make sure you have Python and Flask installed.
3.  Run `app.py` to start the web app.
4.  Open the web app in your browser and play around with it!

##  Shoutout

Big thanks to my friends who helped or inspired this project! 🙌

---

Hope you like it!  😊
```
