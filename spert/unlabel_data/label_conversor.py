import json
import os
class data:
    def __init__(self, origen):
        self.origen = origen
        self.name = os.path.basename(origen).split('.')[0]
        
    def unlabel_data(self):
        f = open(self.origen)
        labeled_data = json.loads(f.read())
        print(self.name)
        for label_d in labeled_data:
            del label_d["entities"]
            del label_d["relations"]
            del label_d["orig_id"]
       
        with open(self.name+"_unlabeled.json", 'w') as outfile:
          json.dump(labeled_data, outfile)
       
       



    
    