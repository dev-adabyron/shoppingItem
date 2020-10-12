#-*-coding:utf-8-*-
from flask import Flask, request, json
from datetime import datetime
import os

app = Flask(__name__)

commonResponse = {
    'version': '2.0',
    'resultCode': 'OK',
    'output': {}
}

shoppingItems = [
    ['간장', '2020-09-20'],
    ['설탕', '2020-09-27'],
    ['토마토', '2020-10-10'],
]


def getUtteranceParameter () :
    data = request.get_json()
    return data['action']['parameters']

@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/info', methods=['POST'])
def info():
    data = request.get_json()
    print
    data['test']
    response = commonResponse
    response['output']['name'] = 'napier'
    return json.dumps(response)


@app.route('/shoppingItems/createItems', methods=['POST'])
def createItems():

    utteranceParameter = getUtteranceParameter()
    utteranceValue = utteranceParameter['item']['value']

    response = commonResponse

    response['output']['existYn'] = 'N'

    for i in shoppingItems :
        print (type(i[0]))
        print (i[0])
        print (type(utteranceValue))
        print (utteranceValue)
        if i[0] == utteranceValue :
            response['output']['existYn'] = 'Y'
            response['output']['registerDate'] = i[1]

    if response['output']['existYn'] == 'N':
         shoppingItems.append([utteranceValue, datetime.today().strftime('%Y-%m-%d')])
    return json.dumps(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

