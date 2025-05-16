import cv2
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from datetime import datetime


# Loading the BLIP model and processor
MODEL_PATH = "blip_model"

try:
    print("Trying to load model from local path...")
    processor = BlipProcessor.from_pretrained(MODEL_PATH)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_PATH)
    print("Model loaded from local folder.")
except:
    print("Model not found locally, downloading from Hugging Face...")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    print(" Saving model locally for future use...")
    processor.save_pretrained(MODEL_PATH)
    model.save_pretrained(MODEL_PATH)
    print("Model saved to local folder 'blip_model'.")

cap=cv2.VideoCapture(0)  # Using 0 for the default camera

log_file = open("activity_log.txt","a") 

def log_activity(text):
    timestamp = datetime.now().isoformat()
    log_file.write(f"{timestamp} - {text}\n")
    log_file.flush()  # Ensure the log is written immediately
    print(f"{timestamp} - {text}")  # Print to console for real-time feedback

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (384, 384))
    from PIL import Image
    image = Image.fromarray(cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB))

    input=processor(image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**input)
    description = processor.decode(out[0], skip_special_tokens=True)
    print(repr(description))

    cv2.putText(frame, repr(description), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("LookupAi Feed", frame)
    log_activity(description)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
log_file.close()