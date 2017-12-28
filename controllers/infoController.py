import requests,json,random
from const import TOKENS

headers = {
    "Accept": "application/json",
	"Content-Type": "application/json",
}
jokeUrl = "http://api.icndb.com/jokes/random"

def joke():
	response = requests.get(jokeUrl, headers=headers).json()
	return response["value"]["joke"]

def giphy(search):
	giphyUrl = "http://api.giphy.com/v1/gifs/search?q="+"+".join(search)+"&api_key="+TOKENS.GIPHY_API_KEY
	response = requests.get(giphyUrl, headers=headers).json()
	responseCount = len(response["data"])
	return response["data"][random.randint(0, responseCount)]['url']
giphy("test")