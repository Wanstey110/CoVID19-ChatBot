import requests
import json

def cUpdateWorld():
    url = "https://covid-19-tracking.p.rapidapi.com/v1"
    headers = {
        'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com",
        'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
        }
    response = requests.request("GET", url, headers=headers)
    r = json.loads(response.text)
    conf = int(r[0]["Total Cases_text"].replace(",",""))
    deaths = int(r[0]["Total Deaths_text"].replace(",",""))
    recov = int(r[0]["Total Recovered_text"].replace(",",""))
    return conf,deaths,recov

if __name__ == "__main__":
    x,y,z = cUpdateWorld()
    print(f"Confirmed Cases:{x}\nDeaths:{y}\nRecovered:{z}")