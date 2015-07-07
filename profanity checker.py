import urllib

def read_text():
    quotes=open(r"C:\Python27\textdoc.txt")
    contents=quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("This document could not be checked")

read_text()
