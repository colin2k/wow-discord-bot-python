import json
from controllers import piController as pi
from controllers import infoController as info
from const import PATHS


def parse(messageDAO):
	messageList = messageDAO.content.split()
	botKey = messageList[0]
	botTree = json.loads(open(PATHS.PROCESS_JSON_PATH, encoding='utf-8').read())
	if botKey in botTree.keys():
		return processor(messageList[1:],botTree[botKey],messageDAO)
	else:
		return None

def processor(botParameter, commandTree, messageDAO):
	commandKey = "help" if len(botParameter)<1  else botParameter[0]
	botParameter = botParameter[1:]
	if commandKey in commandTree:
		if commandKey == "help":
			return howTo()
		elif commandKey == "hello":
			return "Hello "+ messageDAO.author.name
		elif commandKey == "joke":
			return info.joke()
		elif commandKey == "giphy":
			return info.giphy(botParameter)
		elif commandKey == "cmd":
		 	return pi.process(botParameter) 
		else:
		 	return howTo()
	else:
		return howTo()

def howTo():
	return "usage:\nhelp  -  to view this\nhello  -  to say hello :)\njoke  -  telling a joke (mostly chuck norris related) "