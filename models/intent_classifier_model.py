import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class IntentClassifier:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=6)
        
        
    def classify_intent(self, user_input):
        inputs = self.tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
        outputs = self.model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        intent_index = torch.argmax(probs).item()
        confidence = probs[0][intent_index].item()
        return intent_index, confidence