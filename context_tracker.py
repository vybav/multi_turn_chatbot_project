from collections import defaultdict

class ContextTracker:
    def __init__(self):
        self.context = defaultdict(dict)
        
    def get_context(self, user_id, key):
        return self.context.get(user_id, {}).get(key, None)
    
    def update_context(self, user_id, key, value):
        self.context[user_id][key] = value
        
    def reset_context(self, user_id):
        self.context[user_id] = {}
        