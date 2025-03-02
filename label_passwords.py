import pandas as pd 
import re 

df = pd.read_csv("cleaned_rockyou.csv")

df.rename(columns={"passwords": "password"}, inplace=True)

df= df.dropna(subset=["password"])
df["password"] = df["password"].astype(str)


def classify_password(password):
    length = len(password)
    
    if length <= 6 or password.isalpha() or password.isdigit():
       return "weak"
       
    if 7 <= length <= 10 and re.search(r"\d", password) and re.search(r"[a-zA-Z]",password):
       return "medium"
       
    if length > 10 and re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"[^a-zA-Z0-9]", password):
       return "strong"
     
    return "medium"
   
df["strength"] = df["password"].apply(classify_password)
df.to_csv("labeled_rockyou.csv", index=False)

print("password labeling complete! saved as labeled_rockyou.csv")
