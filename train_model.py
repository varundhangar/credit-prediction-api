import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,VotingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
import matplotlib.pyplot as plt
import joblib
import copy
from pathlib import Path

data_path = Path(__file__).resolve().parent / "credit_card_clean_1.csv"
df = pd.read_csv(data_path)

df1=copy.deepcopy(df)
df1.replace("Not available", pd.NA, inplace=True)
df1.dropna(inplace=True)
scaler=StandardScaler()

#df1["PAY_1"].fillna("0",inplace=True)

df1.drop(columns=["ID"],inplace=True)

x=df1.drop("default payment next month",axis=1)
y=df1["default payment next month"]


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
lr=LogisticRegression(class_weight="balanced",max_iter=100000)
rf=RandomForestClassifier(n_estimators=100,random_state=42)

model=VotingClassifier(estimators=[('lr',lr),
                                   ('rf',rf)
                                  ],
                       voting='soft')
model.fit(x_train,y_train)
predictt=model.predict(x_test)

print(predictt)

print("cofusion metrix")
cm=confusion_matrix(y_test,predictt)
print(cm)
print("classification_report")
cr=classification_report(y_test,predictt)
print(cr)
print("accuracuuu",accuracy_score(y_test,predictt))


plt.figure(figsize=(6,5))
plt.hist(y,bins=2)
plt.title("identify the feafult creadit person with creteria")
plt.xlabel("Class (0 = No Default, 1 = Default)")
plt.ylabel("count")
plt.show()

joblib.dump(model ,"credit_model.pkl")
joblib.dump(scaler,"scaled.pkl")
print("Model saved successfully!")
print("Scaler saved successfully!")



