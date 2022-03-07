from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd


df = pd.read_csv("training_data.csv")
#df.groupby('nationality')['names'].size().plot(kind= 'bar')
x_feat = df['names']
y_label = df['nationality']

vec = CountVectorizer()
x = vec.fit_transform(x_feat)

x_train, x_test, y_train, y_test = train_test_split(x, y_label, test_size= 0.25, random_state=42)

logit = LogisticRegression()
logit.fit(x_train, y_train)

print(logit.score(x_test, y_test))

sample1 = ["Shawn"]
test1 = vec.transform(sample1).toarray()


print(logit.predict(test1))
