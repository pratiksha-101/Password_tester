import pandas as pd 
rockyou_path = "/usr/share/wordlists/rockyou.txt"

with open(rockyou_path, encoding="latin-1") as f:
    passwords = f.read().splitlines()
    
passwords = list(set(passwords))
passwords = [pwd for pwd in passwords if len(pwd) >= 4]
df = pd.DataFrame(passwords, columns=["passwords"])
df.to_csv("cleaned_rockyou.csv", index=False)
print("cleaned dataset saved as cleaned_rockyou")
