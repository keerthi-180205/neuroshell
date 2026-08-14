import os
import joblib
import numpy as np

class IntentRouter:
    """
    ML Router for NeuroShell.
    Uses a pre-trained Linear SVM (with TF-IDF) to classify user intents.
    This routes deterministic commands (e.g. GET_TIME) directly to tools,
    saving LLM API quota and latency.
    """
    def __init__(self, model_path: str = None, confidence_threshold: float = 0.5):
        # Default path to the intent_model.pkl we are about to copy
        if not model_path:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            model_path = os.path.join(base_dir, "models", "intent_model.pkl")
            
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold
        self.model = None
        
        self._load_model()

    def _load_model(self):
        """Loads the scikit-learn pipeline from the pickle file."""
        if not os.path.exists(self.model_path):
            print(f"[ROUTER] ⚠️ Warning: ML model not found at {self.model_path}")
            print("[ROUTER] ⚠️ Falling back to Gemini for all requests until the model is provided.")
            return
            
        try:
            self.model = joblib.load(self.model_path)
            print(f"[ROUTER] ✅ Successfully loaded ML intent model from {self.model_path}")
        except Exception as e:
            print(f"[ROUTER] ❌ Failed to load ML model: {e}")
            self.model = None

    def route_request(self, user_input: str) -> str:
        """
        Classifies the user input into an intent.
        
        Returns:
            The predicted intent string (e.g., 'GET_TIME', 'UNKNOWN').
        """
        # 1. Fallback if model isn't loaded
        if not self.model:
            return "GENERAL_QUESTION"
            
        # 2. Predict the intent
        try:
            prediction = self.model.predict([user_input])[0]
            
            # 3. Check Confidence (Rejection mechanism for UNKNOWN)
            # LinearSVC outputs a decision_function (distance to hyperplane) instead of raw probabilities.
            decision_scores = self.model.decision_function([user_input])
            max_score = np.max(decision_scores)
            
            # If the model is extremely uncertain, force UNKNOWN
            if max_score < self.confidence_threshold:
                print(f"[ROUTER] Low confidence ({max_score:.2f}). Rejecting prediction '{prediction}' as UNKNOWN.")
                return "UNKNOWN"
                
            return prediction
            
        except Exception as e:
            print(f"[ROUTER] ❌ Inference error: {e}")
            return "GENERAL_QUESTION"
