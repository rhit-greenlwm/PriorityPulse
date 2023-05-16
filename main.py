import datetime
import pyuac
import EmailClassifier as Classifier
import EmailProcessor as Loader
from EmailProcessor import Email

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

def get_urgency(email):
    delta = datetime.datetime.now() - datetime.datetime.strptime(email.date[:-6], '%a, %d %b %Y %H:%M:%S')
    return delta.total_seconds() / 60 / 60

class OutputObject:

    def __init__(self, subject, sentfrom, urgency, sentiment):
        self.subject = subject
        self.sentfrom = sentfrom
        self.urgency = urgency
        self.sentiment = sentiment

def main():
    emails = Loader.loadEmails()
    out = []
    for email in emails:
        urg = get_urgency(email)
        sent = get_sentiment(email.text)
        out.append(OutputObject(email.subject, email.emailfrom, urg, sent))
    out.sort(key=lambda x: x.urgency, reverse=True)
    for email in out:
        print(f"Subject: {email.subject}\nFrom: {email.sentfrom}\nUrgency: {email.urgency}\nSentiment: {email.sentiment}\n")
    while True:
        key = input("Press Enter to exit...")
        if key == "":
            break


# RUN SCRIPT AS ADMIN
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()  # Already an admin here.
