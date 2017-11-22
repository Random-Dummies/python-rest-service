from __future__ import print_function
import json
def getScores(payload):
    scoreDict = {"skill":0,"exp":0,"Crev":0,"CErev":0,"NeoApi":0}
    # JSON requires double-quotes, not single-quotes.
    payload = json.loads(payload)
    print(payload)
    for doc in payload['payload']:
        scoreDict[doc['type']] = doc['score']
        print(doc['score'], doc['type'])
    scoreList = []
    scoreList.append(scoreDict["skill"])
    scoreList.append(scoreDict["exp"])
    scoreList.append(scoreDict["Crev"])
    scoreList.append(scoreDict["CErev"])
    scoreList.append(scoreDict["NeoApi"])
    return scoreList

