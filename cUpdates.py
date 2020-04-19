import requests
import datetime

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

def getPopWorld():
	url = "https://world-population.p.rapidapi.com/worldpopulation"
	headers = {
		'x-rapidapi-host': "world-population.p.rapidapi.com",
		'x-rapidapi-key': "96c395c12bmsh7977f2a7f725335p156aa1jsn3256842e9bbc"
	}
	response = requests.request("GET", url, headers=headers)
	toReturn = response.text
	fI1 = toReturn.find('population":')
	fI2 = toReturn.find(',"total_countries')
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

	return f"Stats:\nConfirmed: {cDC3}\nDeaths: {dRC3}\nRecovered: {cCC2}\nMortality Rate:{mRV2}\nRecovery Rate:{rRV}\nCases per 1 million:{cPM2}"

def cUpdateWorld():
	url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
	cTime = datetime.datetime.now()
	if len(str(cTime.month)) == 1:
		cTimeMonth = f"0{cTime.month}"
	else:
		cTimeMonth = cTime.month

	if int(cTime.day) == 1:
		##Checks if it is a leap year and in Februrary
		if ((y := int(cTime.year) % 4 == 0 and y % 100 != 0) or (y := int(cTime.year) % 4 == 0 and y % 100 == 0 and y % 400 == 0)) and int(cTime.month) == 2:
			cTimeDay = 29
		elif int(cTime.month) == 2:
			cTimeDay = 28
		elif (m := cTime.month) == 4 or m == 6 or m == 9 or m == 11:
			cTimeDay = 30
		else:
			cTimeDay = 31
	elif len(str(cTime.day)) == 1:
		cTimeDay = f"0{int(cTime.day)-1}"
	else:
		cTimeDay = int(cTime.day) - 1	
			
	if int(cTime.month) == 1:
		cTimeMonth = 12
	else:
		cTimeMonth = int(cTime.month) - 1
	
	cTimeReturn = f"{cTime.year}-{cTimeMonth}-{cTimeDay}"
	print(cTimeReturn)
	querystring = {"date": cTimeReturn}
	headers = {
		'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
		'x-rapidapi-key': "96c395c12bmsh7977f2a7f725335p156aa1jsn3256842e9bbc"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	r = response.text

	##Data cleaning
	r = r.replace('"', '')
	r = r.replace('data: ','')
	r = r.replace('}','')
	r = r.replace('{','')
	r = r.replace(',','')
	
	##Conf is equal to confirmed cases
	r1 = r.find('confirmed:')
	r2 = r.find('confirmed_')
	conf = int(r[r1+11:r2])

	##Deaths is equal to deaths
	r3 = r.find('deaths:')
	r4 = r.find('deaths_')
	death = int(r[r3+8:r4])

	##Recov is equal to recovered cases
	r5 = r.find('recovered:')
	r6 = r.find('recovered_')
	recov = int(r[r5+11:r6])

	##Calculation for mortality rate:
	mRV = (death / conf) * 100
	mRV = round(mRV, 2)
	mRV2 = f"{round(mRV,2)}% (2dp)"

	##Calculation for recovery rate:
	rRV = (recov / conf) * 100
	rRV = f"{round(rRV,2)}% (2dp)"
	
	##Calculation for cases per 1 million people:
	cPM = (conf/getPopWorld())
	cPM2 = cPM * 1000000
	cPM2 = f"{round(cPM2, 2)} (2dp)"

	return f"Stats:\nConfirmed: {conf}\nDeaths: {death}\nRecovered: {recov}\nMortality Rate:{mRV2}\nRecovery Rate:{rRV}\nCases per 1 million:{cPM2}"
if __name__ == "__main__":
	x = cUpdate("Russia")
	print(x)