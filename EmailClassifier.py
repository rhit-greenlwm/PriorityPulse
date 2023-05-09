from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
_classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def predict(text):
    return _classifier(text)[0]['label']
