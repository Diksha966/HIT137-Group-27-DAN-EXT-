# model_text.py
from transformers import pipeline
from model_base import ModelHandler
from decorators import simple_timer, Logger

class TextModelHandler(Logger, ModelHandler):
    """Handler for text classification using Hugging Face pipeline.

    Default model: distilbert-base-uncased-finetuned-sst-2-english
    Category: Text Classification
    """

    def __init__(self, model_id="distilbert-base-uncased-finetuned-sst-2-english"):
        super().__init__(model_id=model_id)

    @simple_timer
    def load(self):
        """Load the Hugging Face text classification pipeline."""
        if not self.loaded:
            self.log(f"Loading text model: {self.model_id}")
            self.model = pipeline("text-classification", model=self.model_id)
            self.loaded = True
            self.log("Text model loaded.")

    @simple_timer
    def run(self, text):
        """Run the model on the given text and return its output."""
        if not self.loaded:
            self.load()
        output = self.model(text)  # returns [{'label': 'POSITIVE', 'score': 0.99}]
        return output
