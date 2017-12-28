import os

def getMyRemoteIp():
	return osCmd("wget -qO- http://ipecho.net/plain")

def process(subtree, key):
	print("processing..."+"["+key+"]")
	if key in commands:
		return commands[key]()
	

#process()
def osCmd(cmd):
	return os.popen(cmd).read()

commands = {
	'botIP':getMyRemoteIp
}

print("---------")
print(process(1,"myIP"))	