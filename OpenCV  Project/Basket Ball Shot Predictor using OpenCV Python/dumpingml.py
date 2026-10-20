import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("synthetic_shot_dataset.csv")

X = df[["A", "B", "C", "landing_x", "landing_y"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

print("Accuracy:", clf.score(X_test, y_test))

# Save model
pickle.dump(clf, open("shot_classifier.pkl", "wb"))


