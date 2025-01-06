from models.intent_classifier_model import IntentClassifier
from models.semantic_embeddings import SemanticSimilarity

class HybridIntentResolver:
    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.semantic_similarity = SemanticSimilarity()
        
    def resolve_intent(self, user_input):
        # First, classify the intent using the intent classifier
        intent_index, classifier_confidence = self.intent_classifier.classify_intent(user_input)
        
        # Second, compute similarity scores using semantic embeddings
        similarity_scores = self.semantic_similarity.compute_similarity(user_input)
        
        # Third, combine the results
        combined_scores = {
            
            intent: (0.5 * classifier_confidence + 0.5 * similarity)
            for intent, similarity in similarity_scores.items()
        }
        
        resolved_intent = max(combined_scores, key=combined_scores.get)
        return resolved_intent, combined_scores[resolved_intent]