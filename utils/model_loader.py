from tensorflow.keras.models import load_model

def loader():
    model=load_model(r"C:\Users\Sajin S\Desktop\vs_code\Gemini_models\chatbot_kj\model\sigh_prediction.h5")
    # print("model loaded successfully")
    return model