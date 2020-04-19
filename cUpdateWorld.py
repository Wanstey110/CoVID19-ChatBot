import requests
import json

def cUpdateSpecial(country):
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
        'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
    }
    response = requests.request("GET", url, headers=headers)
    r = response.text
    r2 = json.loads(r)
    if country == "usa":
        ##USA
        casesUSA = r2["countries_stat"][000]["cases"]
        deathsUSA = r2["countries_stat"][000]["deaths"]
        recoveredUSA = r2["countries_stat"][000]["total_recovered"]
        return f"Stats:\nConfirmed: {casesUSA}\nDeaths: {deathsUSA}\nRecovered: {recoveredUSA}\nMortality Rate:{mRV2}\nRecovery Rate:{rRV}\nCases per 1 million:{cPM2}"
    
    elif country =="china":
        casesChi = r2["countries_stat"][6]["cases"]
        deathsChi = r2["countries_stat"][6]["deaths"]
        recoveredChi = r2["countries_stat"][6]["total_recovered"]
        return f"Stats:\nConfirmed: {casesChi}\nDeaths: {deathsChi}\nRecovered: {recoveredChi}\nMortality Rate:{mRV2}\nRecovery Rate:{rRV}\nCases per 1 million:{cPM2}"

    elif country == "canada":
        ##Canada
        casesCan = r2["countries_stat"][12]["cases"]
        deathsCan = r2["countries_stat"][12]["deaths"]
        recoveredCan = r2["countries_stat"][12]["total_recovered"]
        return f"Stats:\nConfirmed: {casesCan}\nDeaths: {deathsCan}\nRecovered: {recoveredCan}\nMortality Rate:{mRV2}\nRecovery Rate:{rRV}\nCases per 1 million:{cPM2}"

if __name__ == "__main__":
    x = cUpdateSpecial("usa") 
    print(x)
    x = cUpdateSpecial("china")
    print(x)
    x = cUpdateSpecial("canada")
    print(x)