import re 
import pandas as pd 

def extract_features(password):
    return [ 
        len(password),
        bool(re.search(r"\d",password)),
        bool(re.search(r"[A-Z]",password)),
        bool(re.search(r"[a-z]",password)),
        bool(re.search(r"[^a-zA-Z0-9]",password)),
    ]
df = pd.read_csv("labeled_rockyou.csv")
X = df["password"].apply(extract_features).tolist()
X = pd.DataFrame(X, columns=["length","has_digit","has_upper","has_lower","has_special"])

X["strength"] = df["strength"]
X.to_csv("features_rockyou.csv", index=False)
print ("feature extraction complete !")
