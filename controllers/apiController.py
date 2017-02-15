import requests
import json

def process(subtree, key, messageDAO):
    a = traits(messageDAO)
    return a

    options = \
        {"tc1":traits(messageDAO),
         "tc2":relics
        }

    try:
        a = options[subtree[key]]()
    except:
        a = "error"
    
    return a
    
    
def traits(messageDAO):
    n = messageDAO.author.name

    url = 'https://eu.api.battle.net/wow/character/' + "thrall" + "/" + "eliath"

    params = dict(
        fields="items",
        locale="en_GB",
        apikey="rm4g62eungjsvppyupebwsubeafrb6a9"
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.content)
    ilvl = data['items']['averageItemLevel'] 

    if(len(data['items']['mainHand']['relics']) > 0):
        relics = data['items']['mainHand']['relics']
    else:
        relics = data['items']['offHand']['relics']

    completemsg = 'Relics for: **' + n + '** ```'

    for member in relics:
        url = 'https://eu.api.battle.net/wow/item/' + str(member['itemId'])

        params = dict(
            locale="en_GB",
            apikey="rm4g62eungjsvppyupebwsubeafrb6a9"
        )

        resp = requests.get(url=url, params=params)
        data = json.loads(resp.content)
        relicname = data['name']
        completemsg += relicname + "\n"

    return completemsg + "```"

def relics():
    return("asked for relics")