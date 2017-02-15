import json
from controllers import apiController as api
from const import PATHS


def parse(messageDAO):
	commandList = messageDAO.content.split()
	key = commandList[0]
	commandTree = json.loads(open(PATHS.PROCESS_JSON_PATH, encoding='utf-8').read())
	if key in commandTree.keys():
		processorKey = commandTree[key]["processor"]
		del commandTree[key]["processor"]
		subKey = "default" if len(commandList)<2  else commandList[1]
		return processor(processorKey,commandTree[key],subKey,messageDAO)
	else:
		return None

def processor(processorKey, tree, treeKey, messageDAO):
	if treeKey in tree.keys():
		if processorKey == "plain":
			return replaceKeys(tree[treeKey],messageDAO)
		elif processorKey == "api":
		 	return api.process(tree,treeKey) 
		else:
		 	return "undefined"
	else:
		return replaceKeys(tree['default'],messageDAO)

def replaceKeys(response,messageDAO):
    return response\
        .replace("@user@", messageDAO.author.name)\
        .replace("@usermention@", messageDAO.author.mention)
