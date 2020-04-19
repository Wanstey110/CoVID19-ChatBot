import requests

def cUpdateUSA(province):
    url = "https://covid-19-statistics.p.rapidapi.com/reports"

    querystring = {"region_province":province,"iso":"USA","region_name":"US","date":"2020-03-14","q":f"US {province}"}

    headers = {
        'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
        'x-rapidapi-key': "96c395c12bmsh7977f2a7f725335p156aa1jsn3256842e9bbc"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

if __name__ == "__main__":
    cUpdateUSA("Georgia")
