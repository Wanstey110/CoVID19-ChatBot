import requests
import datetime
import json

##GetPop functions are commented out because the api is down / unreliable
"""
def getPopulation(country):
	url = "https://world-population.p.rapidapi.com/population"
	if country == "Korea, South":
		country = "South Korea"
	querystring = {"country_name": country}
	headers = {
        'x-rapidapi-host': "world-population.p.rapidapi.com",
        'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
    }
	response = requests.request(
        "GET", url, headers=headers, params=querystring)
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
"""
def cUpdate(country):
	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
	querystring = {"country": country}
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

    # dRC3 is equal to the number of deaths
	dRC = toReturn.find("s:")
	dRC2 = toReturn.find("recovered")
	dRC3 = int(toReturn[dRC+2:dRC2])

	# cDC3 is equal to the number of cases
	cDC = toReturn.find("d:")
	cDC2 = toReturn.find("deaths")
	cDC3 = int(toReturn[cDC+2:cDC2])

    # cCC2 is equal to the number of recovered
	cCC = toReturn.find('recovered:')
	cCC2 = int(toReturn[cCC+10:])
	mRV = (dRC3 / cDC3) * 100
	mRV = round(mRV, 2)
	mRV2 = f"{round(mRV,2)}% (2dp)"
	
	rRV = (cCC2 / cDC3) * 100
	rRV = f"{round(rRV,2)}% (2dp)"

	"""
	if country == "Sao Tome and Principe":
		cPM = (cDC3 / getPopulation("Sao Tome & Principe"))
		cPM2 = cPM * 1000000
		cPM2 = f"{round(cPM2,2)} (2dp)"	
	else:
		cPM = (cDC3/getPopulation(country))
		cPM2 = cPM * 1000000
		cPM2 = f"{round(cPM2, 2)} (2dp)"
	"""
	return f"Stats:\nConfirmed: {cDC3}\nDeaths: {dRC3}\nRecovered: {cCC2}\nMortality Rate:{mRV2}\nRecovery Rate:{rRV}"


def cUpdateWorld():
	url = "https://covid-19-tracking.p.rapidapi.com/v1"
	headers = {
        'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com",
        'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
    }
	response = requests.request("GET", url, headers=headers)
	r = json.loads(response.text)
	cases = int(r[0]["Total Cases_text"].replace(",", ""))
	deaths = int(r[0]["Total Deaths_text"].replace(",", ""))
	recovered = int(r[0]["Total Recovered_text"].replace(",", ""))
	
	mortalityRate = (deaths / cases) * 100
	mortalityRate = f"{round(mortalityRate,2)}% (2dp)"

	recoveryRate = (recovered / cases) * 100
	recoveryRate = f"{round(recoveryRate,2)}% (2dp)"

	"""
	casesperm = (cases / getPopWorld())
	casesperm = casesperm * 1000000
	casesperm = f"{round(casesperm, 2)} (2dp)"
	"""
	return f"Stats:\nConfirmed: {cases}\nDeaths: {deaths}\nRecovered: {recovered}\nMortality Rate:{mortalityRate}\nRecovery Rate:{recoveryRate}"


def cUpdateSpecial(country):
	url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
	headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
	}
	response = requests.request("GET", url, headers=headers)
	r = response.text
	r2 = json.loads(r)

	if country == "usa" or country == "us" or country == "america":
        # USA
		casesUSA = int(r2["countries_stat"][000]["cases"].replace(",", ""))
		deathsUSA = int(r2["countries_stat"][000]["deaths"].replace(",", ""))
		recoveredUSA = int(r2["countries_stat"][000]
                           ["total_recovered"].replace(",", ""))

		mortalityRateUSA = (deathsUSA / casesUSA) * 100
		mortalityRateUSA = f"{round(mortalityRateUSA,2)}% (2dp)"

		recoveryRateUSA = (recoveredUSA / casesUSA) * 100
		recoveryRateUSA = f"{round(recoveryRateUSA,2)}% (2dp)"

		"""
		casespermUSA = (casesUSA/getPopulation("United States"))
		casespermUSA = casespermUSA * 1000000
		casespermUSA = f"{round(casespermUSA, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesUSA}\nDeaths: {deathsUSA}\nRecovered: {recoveredUSA}\nMortality Rate:{mortalityRateUSA}\nRecovery Rate:{recoveryRateUSA}"

	elif country == "china":
		casesChi = int(r2["countries_stat"][6]["cases"].replace(",", ""))
		deathsChi = int(r2["countries_stat"][6]["deaths"].replace(",", ""))
		recoveredChi = int(r2["countries_stat"][6]
                           ["total_recovered"].replace(",", ""))

		mortalityRateChi = (deathsChi / casesChi) * 100
		mortalityRateChi = f"{round(mortalityRateChi,2)}% (2dp)"

		recoveryRateChi = (recoveredChi / casesChi) * 100
		recoveryRateChi = f"{round(recoveryRateChi,2)}% (2dp)"

		"""
		casespermChi = (casesChi/getPopulation("China"))
		casespermChi = casespermChi * 1000000
		casespermChi = f"{round(casespermChi, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesChi}\nDeaths: {deathsChi}\nRecovered: {recoveredChi}\nMortality Rate:{mortalityRateChi}\nRecovery Rate:{recoveryRateChi}"

	elif country == "canada":
		# Canada
		casesCan = int(r2["countries_stat"][12]["cases"].replace(",", ""))
		deathsCan = int(r2["countries_stat"][12]["deaths"].replace(",", ""))
		recoveredCan = int(r2["countries_stat"][12]
                           ["total_recovered"].replace(",", ""))

		mortalityRateCan = (deathsCan / casesCan) * 100
		mortalityRateCan = f"{round(mortalityRateCan,2)}% (2dp)"

		recoveryRateCan = (recoveredCan / casesCan) * 100
		recoveryRateCan = f"{round(recoveryRateCan,2)}% (2dp)"
		
		"""
		casespermCan = (casesCan/getPopulation("Canada"))
		casespermCan = casespermCan * 1000000
		casespermCan = f"{round(casespermCan, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesCan}\nDeaths: {deathsCan}\nRecovered: {recoveredCan}\nMortality Rate:{mortalityRateCan}\nRecovery Rate:{recoveryRateCan}"
	
	elif country == "france":
		casesFran = int(r2["countries_stat"][4]["cases"].replace(",",""))
		deathsFran = int(r2["countries_stat"][4]["deaths"].replace(",",""))
		recoveredFran = int(r2["countries_stat"][4]["total_recovered"].replace(",",""))

		mortalityRateFran = f"{round((deathsFran / casesFran) * 100,2)}% (2dp)"
		recoveryRateFran = f"{round((recoveredFran / casesFran) * 100,2)}% (2dp)"
		
		"""
		casespermFran = (casesFran / getPopulation("France")) * 100000
		casespermFran = f"{round(casespermFran, 2)}% (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesFran}\nDeaths: {deathsFran}\nRecovered: {recoveredFran}\nMortality Rate:{mortalityRateFran}\nRecovery Rate:{recoveryRateFran}"
		
	elif country == 'england' or country == 'uk' or country == 'britain' or country == 'greatbritain' or country == 'unitedkingdom':
		casesUK = int(r2["countries_stat"][6]["cases"].replace(",", ""))
		deathsUK = int(r2["countries_stat"][6]["deaths"].replace(",", ""))
		recoveredUK = int(r2["countries_stat"][6]["total_recovered"].replace(",", ""))
		
		mortalityRateUK = (deathsUK / casesUK) * 100
		mortalityRateUK = f"{round(mortalityRateUK,2)}% (2dp)"
		
		recoveryRateUK = (recoveredUK / casesUK) * 100
		recoveryRateUK = f"{round(recoveryRateUK,2)}% (2dp)"
		
		"""
		casespermUK = (casesUK/getPopulation("United Kingdom"))
		casespermUK = casespermUK * 1000000
		casespermUK = f"{round(casespermUK, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesUK}\nDeaths: {deathsUK}\nRecovered: {recoveredUK}\nMortality Rate:{mortalityRateUK}\nRecovery Rate:{recoveryRateUK}"

	elif country == 'australia':
		casesAus = int(r2["countries_stat"][27]["cases"].replace(",", ""))
		deathsAus = int(r2["countries_stat"][27]["deaths"].replace(",", ""))
		recoveredAus = int(r2["countries_stat"][27]["total_recovered"].replace(",", ""))
		
		mortalityRateAus = (deathsAus / casesAus) * 100
		mortalityRateAus = f"{round(mortalityRateAus,2)}% (2dp)"
		
		recoveryRateAus = (recoveredAus / casesAus) * 100
		recoveryRateAus = f"{round(recoveryRateAus,2)}% (2dp)"
		
		"""
		casespermAus = (casesAus/getPopulation("Australia"))
		casespermAus = casespermAus * 1000000
		casespermAus = f"{round(casespermAus, 2)} (2dp)"
		"""
		return f"Stats:\nConfirmed: {casesAus}\nDeaths: {deathsAus}\nRecovered: {recoveredAus}\nMortality Rate:{mortalityRateAus}\nRecovery Rate:{recoveryRateAus}"
