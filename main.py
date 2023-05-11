import time
import pyuac
import EmailClassifier as Classifier

def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

class Sentiment:
    def __init__(self, scores):
        self.negative = scores["negative"]
        self.neutral = scores["neutral"]
        self.positive = scores["positive"]
        self.scores = scores

    def __str__(self):
        return f"Negative: {self.negative}, Neutral: {self.neutral}, Positive: {self.positive}"

def get_sentiment(text):
    text = preprocess(text)
    output = Classifier.predict(text)
    scores = {"negative": output[0], "neutral": output[1], "positive": output[2]}
    return Sentiment(scores)

def main():
    pass


# RUN SCRIPT AS ADMIN
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()  # Already an admin here.
