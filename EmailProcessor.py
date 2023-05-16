
from email import policy
from email.parser import BytesParser
import glob
from bs4 import BeautifulSoup

class Email:
    def __init__(self, text, emailfrom, date, subject):
        self.text = text
        self.emailfrom = emailfrom
        self.date = date
        self.subject = subject


def loadEmails():
    path = 'emails/'  # set this to "./" if in current directory
    emails = []
    eml_files = glob.glob(path + '*.eml')  # get all .eml files in a list
    for eml_file in eml_files:
        with open(eml_file, 'rb') as fp:  # select a specific email file from the list
            name = fp.name  # Get file name
            msg = BytesParser(policy=policy.default).parse(fp)

        pretext = msg.get_body(preferencelist=('plain'))

        if(pretext is None):
            html = msg.get_body(preferencelist=('html')).get_content()
            soup = BeautifulSoup(html, features="html.parser")

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()  # rip it out

            # get text
            text = soup.get_text()
        else:
            text = pretext.get_content()

        fp.close()
        text = text.split("\n")
        newText = []
        for line in text:
            if (line != ""):
                newText.append(line)
        emails.append(Email('\n'.join(newText), msg.get('From'), msg.get('Date'), msg.get('Subject')))
    return emails
loadEmails()