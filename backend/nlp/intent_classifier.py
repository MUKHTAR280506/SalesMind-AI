import pickle 

model = pickle.load(open("intent_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

def predict_intent(text):
    x = vectorizer.transform([text])

    intent = model.predict(x)[0]

    return intent