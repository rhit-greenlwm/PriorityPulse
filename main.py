import pyuac
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def main():
    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")

    inputs = tokenizer("We are very happy to show you the 🤗 Transformers library.")
    print(inputs)

    classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    classifier("We are very happy to show you the 🤗 Transformers library.")

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()  # Already an admin here.