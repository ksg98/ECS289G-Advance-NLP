from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = FastAPI()

# Load your trained BERT model and tokenizer
model_path = './final_bert_model'
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained(model_path)
model.eval()  # Set model to evaluation mode
if torch.cuda.is_available():
    model.to('cuda')

# Gemma API details
GEMMA_API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b-it"
HEADERS = {"Authorization": "Bearer your_new_face_token_here"}



class ChatRequest(BaseModel):
    prompt: str

def predict_label(text):
    # Tokenize the input text
    inputs = tokenizer(text, padding=True, truncation=True, max_length=128, return_tensors="pt")
    
    # Move the inputs to the same device as the model
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    
    # Get the model's predictions
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Convert the logits to probabilities
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
    # Get the predicted label (0 or 1)
    predicted_label = torch.argmax(probabilities, dim=1).item()
    
    # Convert the label to the corresponding category
    return 'jailbreak' if predicted_label == 1 else 'not jailbreak'

def query_gemma_api(prompt: str):
    response = requests.post(GEMMA_API_URL, headers=HEADERS, json={"inputs": prompt})
    return response.json()

@app.post("/chat")
def chat(request: ChatRequest):
    # Use the predict_label function to determine if the prompt is a jailbreak attempt
    predicted_category = predict_label(request.prompt)
    
    if predicted_category == 'jailbreak':
        raise HTTPException(status_code=400, detail="Jailbreak prompt detected.")
    
    # Forward to Gemma API if not a jailbreak prompt
    response = query_gemma_api(request.prompt)
    return response
# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
