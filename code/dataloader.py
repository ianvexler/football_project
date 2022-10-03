import json

class dataloader:
    def load_data():
        with open("test.json") as json_file:
            json_data = json.load(json_file)
            print(json_data)

        return json_data        
