import pandas   as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

#Load the csv file
df=pd.read_csv("iris.csv")

print(df.head(5))

#select independent and dependent variable

X=df[["Sepal_Length","Sepal_Width","Petal_Length","Petal_Width"]]
y=df[["Class"]]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=50)

#feature scalling
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

#instantiate the model
classifier=RandomForestClassifier()


#Fit the model
classifier.fit(X_train,y_train)

#Make pickle file

pickle.dump(classifier,open("model.pkl","wb"))

