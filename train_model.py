import pandas as pd
import random
import os
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, f1_score

# Models
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier



df = pd.read_csv('pcmctransit.csv')

# Label Encoding
le_from = LabelEncoder()
le_to = LabelEncoder()
le_day = LabelEncoder()
le_time = LabelEncoder()
le_event = LabelEncoder()
le_demand = LabelEncoder()

df['from'] = le_from.fit_transform(df['from'])
df['to'] = le_to.fit_transform(df['to'])
df['day'] = le_day.fit_transform(df['day'])
df['time'] = le_time.fit_transform(df['time'])
df['event'] = le_event.fit_transform(df['event'])
df['demand'] = le_demand.fit_transform(df['demand'])

# Features & Labels
X = df[['from', 'to', 'day', 'time', 'temp', 'event']]
y = df['demand']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models to try
models = {
    "RandomForest": RandomForestClassifier(),
    "DecisionTree": DecisionTreeClassifier(),
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "KNeighbors": KNeighborsClassifier(),
    "GradientBoosting": GradientBoostingClassifier()
}

# Compare models
results = []
best_model = None
best_score = 0

print("🔍 Model Evaluation:\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(f"📌 {name} Accuracy: {acc:.4f}, F1-score: {f1:.4f}")
    print(classification_report(y_test, y_pred, target_names=le_demand.classes_))
    print("-" * 50)

    results.append((name, acc, f1))

    if f1 > best_score:
        best_score = f1
        best_model = model
        best_model_name = name

# Save best model and encoders
os.makedirs("model", exist_ok=True)
joblib.dump(best_model, 'model/demand_classifier.pkl')
joblib.dump(le_from, 'model/le_from.pkl')
joblib.dump(le_to, 'model/le_to.pkl')
joblib.dump(le_day, 'model/le_day.pkl')
joblib.dump(le_time, 'model/le_time.pkl')
joblib.dump(le_event, 'model/le_event.pkl')
joblib.dump(le_demand, 'model/le_demand.pkl')

# Show Summary
print("\n✅ Best Model:", best_model_name)
print("📊 Summary Table:")
print(f"{'Model':<20}{'Accuracy':<10}{'F1-score'}")
for r in results:
    print(f"{r[0]:<20}{r[1]:<10.4f}{r[2]:.4f}")
