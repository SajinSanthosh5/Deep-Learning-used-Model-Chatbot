import cv2
import numpy as np
# from utils.model_loader import loader

classes = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")+ ["del", "nothing", "space"]

def img_processesor(frame):
    img=cv2.resize(frame,(224,224))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_final=img.reshape((1,224,224,3))/255
    return img_final


def output_generator(model,frame):
    img=img_processesor(frame)
    prediction=model.predict(img,verbose=0)
    output=np.argmax(prediction,axis=1)[0]
    confidence=np.max(prediction)
    # print(f"letter:{classes[output]},conf:{confidence}")
    if output>=len(classes):
        return "unkown", confidence
    return classes[output],confidence

# model=loader()
# i=r"C:\Users\Sajin S\Desktop\vs_code\Gemini_models\chatbot_kj\model\oo.jpg"
# img=cv2.imread(i)

# if __name__=="__main__":
#     print(output_generator(model,img))
#     print("model load")