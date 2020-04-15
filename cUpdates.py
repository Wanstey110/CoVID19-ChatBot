import requests

def getPopulation(country):
	url = "https://world-population.p.rapidapi.com/population"
	querystring = {"country_name": country}
	headers = {
		'x-rapidapi-host': "world-population.p.rapidapi.com",
		'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	toReturn = response.text
	fI1 = toReturn.find('"population":')
	fI2 = toReturn.find(',"ranking')
	toReturn = int(toReturn[fI1+13:fI2])

	return toReturn

def cUpdate(country):
	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
	querystring = {"country":country}
	headers = {
	    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
	    'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.text.find('"confirmed')
	
	toReturn = response.text[result:].replace("}", "")
	toReturn = toReturn.replace("]", "")
	toReturn = toReturn.replace('"', "")
	toReturn = toReturn.replace(',', " ")

	##dRC3 is equal to the number of deaths
	dRC = toReturn.find("s:")
	dRC2 = toReturn.find("recovered")
	dRC3 = int(toReturn[dRC+2:dRC2])

	##cDC3 is equal to the number of cases
	cDC = toReturn.find("d:")
	cDC2 = toReturn.find("deaths")
	cDC3 = int(toReturn[cDC+2:cDC2])

	##cCC2 is equal to the number of recovered
	cCC = toReturn.find('recovered:')
	cCC2 = int(toReturn[cCC+10:])
	
	##Calculation for mortality rate:
	mRV = (dRC3 / cDC3) * 100
	mRV = round(mRV, 2)
	mRV2 = f"{round(mRV,2)}% (2dp)"

	##Calculation for recovery rate:
	rRV = (cCC2 / cDC3) * 100
	rRV = f"{round(rRV,2)}% (2dp)"

	##Calculation for cases per 1 million people:
	cPM = (cDC3/getPopulation(country))
	cPM2 = cPM * 1000000
	cPM2 = f"{round(cPM2, 2)} (2dp)"

	return f"Stats:{toReturn}\nMortality Rate:{mRV2}\nRecovery Rate:{rRV}\nCases per 1 million:{cPM2}"

if __name__ == "__main__":
	x = cUpdate("Japan")
	print(x)