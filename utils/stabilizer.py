import time
class SentenceBuilder:
    def __init__(self):
        self.sentence=""
        self.last_letter=""
        self.letter_count=0
        self.last_time=time.time()
        
    def update(self,letters,confidence):
        if letters==self.last_letter and confidence>0.95:
            self.letter_count+=1
        else:
            self.letter_count=1
        
        if self.letter_count>15:
            self.sentence+=letters
            self.last_time=time.time()
            self.letter_count=0
        self.last_letter=letters
        return self.sentence
    
    def should_send(self,delay=3):
        return time.time()-self.last_time>delay and self.sentence !=""
    def clear(self):
        self.sentence=""


# if __name__=="__main__":
#     kk=SentenceBuilder()
#     for i in ["w","y","u","i","o","k","p","r","w"]:
#         u= kk.update(i,96)
#         print(u)
#     print("it good")