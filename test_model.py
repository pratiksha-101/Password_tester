import re 
import joblib
import pandas as pd 
 
model = joblib.load("password_strength_model.pkl")
def extract_features(password):
    return [
         len(password),
         bool(re.search(r"\d",password)),
         bool(re.search(r"[A-Z]",password)),
         bool(re.search(r"[a-z]",password)),
         bool(re.search(r"[a-zA-Z0-9]",password)),
    ]

feature_columns = ["length","has_digit","has_upper","has_lower","has_special"]
label_map = {0:"weak", 1:"medium", 2:"strong", "weak":"Weak", "medium":"Medium", "strong":"Strong"}

while True:
    password = input("Enter a password to test (or type 'exit' to quit) : ")
    if password.lower() == "exit":
         break
         
    features = extract_features(password)
    print(f"extracted feature:{features}")
         
    features_df = pd.DataFrame([features],columns=feature_columns)
    prediction = model.predict(features_df)[0]
    
    print(f"model prediction (raw output):{prediction}")
    if prediction in label_map:
          print(f"\npredicted Strength:{label_map[prediction]}\n")
    else:
          print(f"\nError model returned an unknown value !\n")
          
