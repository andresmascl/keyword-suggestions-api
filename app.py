from typing import Sequence
from flask import Flask, request

# import pandas as pd

from string import printable
from difflib import SequenceMatcher
# from keybert import KeyBERT

import re


app = Flask(__name__)


def printbl(text):
    # deletes double spaces, removes non-printable characters, transform text to upper case
    text = ' '.join(text.split())
    text = "".join(filter(lambda x: x in printable, text))
    text = text.upper()
    return text

@app.route('/')
def home():
    return 'hello world'

@app.route('/suggest', methods=['GET', 'POST'])
def Suggest():
    if request.method == 'GET':
        return({"message": "It's alive! But you must make a POST request to receive suggestions"}), 200
    
    elif request.method == 'POST':
        req_body = request.get_json()
        interview = req_body['interview']
        keywords_array = req_body['keywords']

        # 1st: divide the file into insights
        split_interviews = re.split('/[/]{30,}/', interview)
        insights = {}
        for i in range(0, len(split_interviews)):
            insights[i] = {"insight": split_interviews[i]}

        # 2nd: search for presence of keywords
        for insight in insights:
            suggestions = []
            printable_insight = printbl(insights[insight]['insight'])
            insight_length = len(printable_insight)
            
            for keyword_pair in keywords_array:
                printable_keyword = printbl(list(keyword_pair.values())[0])
                keyword_length = len(printable_keyword)

                if insight_length >= keyword_length:

                    max_similarity = 0
                    for i in range(0, insight_length - keyword_length):
                        print("indices:", keyword_length, insight_length)
                        similarity = SequenceMatcher(None, printable_insight[i: i + keyword_length - 1], printable_keyword).ratio()
                        max_similarity = max(similarity, max_similarity)

                    if max_similarity >= 0.75: suggestions.append(keyword_pair)

            insights[insight]['suggestions'] = suggestions

        return({"insights": insights}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # run our Flask app