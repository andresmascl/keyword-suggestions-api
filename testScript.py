import requests
import json

# please note: the text passed in here must have formated double quotes if it 
# contains them.  Example: " thix text is \"the\" expert interview"
query = {
    "interview": """
        >>Supervised learning is the machine learning task of learning a function that
        maps an input to an output based on example input-output pairs. It infers a
        function from labeled training data consisting of a set of training examples.<<
        >>In supervised learning, each example is a pair consisting of an input object
        (typically a vector) and a desired output value (also called the supervisory signal). 
        A supervised learning algorithm analyzes the training data and produces an inferred function, 
        which can be used for mapping new examples. An optimal scenario will allow for the 
        algorithm to correctly determine the class labels for unseen instances. This requires 
        the learning algorithm to generalize from the training data to unseen situations in a 
        'reasonable' way (see inductive bias).<<
    """,
    "keywords": [{"reasonable":"paralapapiricoipi"}, {"paralapapiricoipi": "unseen"}]
    }

data = json.dumps(query, ensure_ascii=False).encode("utf8")

headers = {'content-type': 'application/json'}

endpoint = "http://127.0.0.1:5000/suggest"
#endpoint = "https://insight-tagging.azurewebsites.net/suggest"

response = requests.post(endpoint, data=data, headers=headers)

print(response.text)