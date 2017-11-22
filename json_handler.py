from __future__ import print_function
import json

response = """{
    'ok': 1.0, 
    'result': [
        {
            'total': 142250.0, 
            '_id': 'BC'
        }, 
        {
            'total': 210.88999999999996,
             '_id': 'USD'
        }, 

        {
            'total': 1065600.0, 
            '_id': 'TK'
        }
        ]
}"""

# JSON requires double-quotes, not single-quotes.
response = response.replace("'", '"')
response = json.loads(response)
print(response)
for doc in response['result']:
    print(doc['_id'], doc['total'])
