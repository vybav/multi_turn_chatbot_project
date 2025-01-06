from sentence_transformers import SentenceTransformer, util
import torch

class SemanticSimilarity:
    def __init__(self):
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.intent_examples = {
            "CheckAccountBalance": ["Check my account balance", "What is my balance?", "Show my account balance"],
            "CheckRewardsBalance": ["Show my rewards balance", "What are my rewards?", "Check rewards balance"],
            "UpdateEmail": ["Change my email address", "Update email", "I want to update my email"],
            "UpdatePhoneNumber": ["Change my phone number", "Update phone number", "I need to update my phone"],
            "UpdateAddress": ["Change my address", "Update my address", "I want to update my location"]
        }
        self.intent_embeddings = {
            intent: self.embedding_model.encode(examples, convert_to_tensor=True)
            for intent, examples in self.intent_examples.items()
        }
        
    def compute_similarity(self, user_input):
        user_embedding = self.embedding_model.encode(user_input, convert_to_tensor=True)
        similarity_scores = {}
        for intent, example_embeddings in self.intent_embeddings.items():
            cosine_scores = util.cos_sim(user_embedding, example_embeddings)
            similarity_scores[intent] = torch.max(cosine_scores).item()
        return similarity_scores
        