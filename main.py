import pyuac
import EmailClassifier as Classifier


def main():
    text = []
    while (True):
        t = input("Please enter text to be classified (Enter ` when done): ")
        t += (" ")
        if (t == "` "):
            break
        text.append(t)

    instr = "".join(text)
    print("INPUT STRING: \t" + instr)
    print("Classification: " + Classifier.predict(instr))


# RUN SCRIPT AS ADMIN
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()  # Already an admin here.
