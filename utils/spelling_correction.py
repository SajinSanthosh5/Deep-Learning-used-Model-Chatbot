from textblob import TextBlob


from textblob import TextBlob

def speller(text):
    if text.strip() == "":
        return ""
    else:
        blob = TextBlob(text)
        correction = blob.correct()
        return str(correction)  

# if __name__=="__main__":
#     print(speller("helo"))
#     print("okay anu")