from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

class BillExtractor:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        predictions = outputs.logits.argmax(dim=-1).squeeze().tolist()
        tokens = self.tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze())
        return list(zip(tokens, predictions))

