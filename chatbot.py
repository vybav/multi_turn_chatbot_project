from context_tracker import ContextTracker
from hybrid_intent_resolver import HybridIntentResolver

def handle_user_query(user_input, user_id, context_tracker):
    
    # Check if there is previous context for the user
    previous_intent = context_tracker.get_context(user_id, "intent")
    
    if previous_intent == "CheckAccountBalance" and "account" in user_input:
        return "Your account balance is $50000000."
    elif previous_intent == "CheckRewardsBalance" and "rewards" in user_input:
        return "Your rewards balance is 1234 reward points."
    else:
        
        #Resolve the intent using HybridIntentResolver
        intent_resolver_hybrid = HybridIntentResolver()
        resolved_intent, score = intent_resolver_hybrid.resolve_intent(user_input)
        context_tracker.update_context(user_id, "intent", resolved_intent)
        
        responses = {
            "CheckAccountBalance": "Your account balance is $50000000.",
            "CheckRewardsBalance": "Your rewards balance is 1234 reward points.",
            "UpdateEmail": "Please provide the new email address.",
            "UpdatePhoneNumber": "Please provide the new phone number.",
            "UpdateAddress": "Please provide the new address."
        }
        
        response = responses.get(resolved_intent, "I’m not sure how to help with that.")
        
    return response


def multi_turn_chatbot():

    user_id = "user123" # Unique identifier for the user
    context_tracker = ContextTracker()
    
    print("Bot: Hi! How can I help you today? Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye. Have a Nice Day!")
            break
        
        response = handle_user_query(user_input, user_id, context_tracker)
        print("Bot:", response)

if __name__ == "__main__":
    multi_turn_chatbot()