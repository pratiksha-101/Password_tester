import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, classification_report
import joblib

df = pd.read_csv("features_rockyou.csv")
label_mapping = {"weak": 0, "medium":1, "strong":2}
df["strength"]=df["strength"].map(label_mapping)
X = df.drop(columns=["strength"])
y = df["strength"]



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Model Accracy:", accuracy_score(y_test, y_pred))
print("\nClassification report :\n", classification_report(y_test, y_pred))

joblib.dump(model, "password_strength_model.pkl")
print("\n☑️ Model training complete ! saved as 'password_strength_model.pkl' ")
