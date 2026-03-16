import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

data = {
"text":[
"I want a laptop",
"Show gaming laptop",
"laptop under 60000",
"price of laptop",
"buy laptop",
"hello",
"hi",
"good morning"
],
"intent":[
"buy_laptop",
"buy_laptop",
"buy_laptop",
"buy_laptop",
"buy_laptop",
"greeting",
"greeting",
"greeting"
]
}

df = pd.DataFrame(data)
vectorizer = TfidfVectorizer()

x= vectorizer.fit_transform(df["text"])

model = LogisticRegression()

model.fit(x, df["intent"])

pickle.dump(model, open("intent_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))