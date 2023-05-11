
from email import policy
from email.parser import BytesParser
import glob
class Email:
    def __init__(self, text,date):
        self.text = text
        self.date = date


    def getText(self):
        return self.text
    def getDate(self):
        return self.date
def loadEmails():
    path = 'emails/'  # set this to "./" if in current directory
    emails= []
    eml_files = glob.glob(path + '*.eml')  # get all .eml files in a list
    for eml_file in eml_files:
        with open(eml_file, 'rb') as fp:  # select a specific email file from the list
            name = fp.name  # Get file name
            msg = BytesParser(policy=policy.default).parse(fp)
        text = msg.get_body(preferencelist=('plain')).get_content()
        fp.close()
        text = text.split("\n")
        newText = []
        for line in text:
            if(line != ""):
                newText.append(line)
        emails.append(Email('\n'.join(newText),msg.get('Date')))
    return emails