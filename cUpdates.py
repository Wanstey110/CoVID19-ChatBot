import requests

def cUpdate(country):
	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
	querystring = {"country":country}
	headers = {
	    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
	    'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.text.find("confirmed")
	toPrint = response.text[result:].replace("}", "")
	toPrint = toPrint.replace("]", "")
	return toPrint
if __name__ == "__main__":
	x = cUpdate("Japan")
	print(x)