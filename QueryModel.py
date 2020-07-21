import json

class QueryModel:
    
    def __init__(self, model_src : str):
        self.model_src = model_src
        self.model = None
        self.__read_model()
    
    def __read_model(self):
        with open(self.model_src) as f:
            model_json = json.loads(f.read())
            self.model = model_json