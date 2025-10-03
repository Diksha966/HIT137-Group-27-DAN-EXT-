# model_base.py
from abc import ABC, abstractmethod

class ModelHandler(ABC):
    """Abstract base class for AI model handlers.

    Attributes:
        model_id (str): Hugging Face model identifier.
        model (pipeline): Loaded Hugging Face pipeline.
        loaded (bool): Whether the model is loaded.
    """

    def __init__(self, model_id=None):
        # store model id and state
        self.model_id = model_id
        self.model = None
        self.loaded = False

    @abstractmethod
    def load(self):
        """Load model resources (e.g., Hugging Face pipeline)."""
        pass

    @abstractmethod
    def run(self, inp):
        """Run inference and return the result."""
        pass

    def is_loaded(self):
        """Return True if model has been loaded."""
        return self.loaded

    def get_model_id(self):
        """Encapsulation: safe way to access model id."""
        return self._model_id