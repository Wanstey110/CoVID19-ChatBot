import requests
def main():
    url = "https://covid-19-statistics.p.rapidapi.com/provinces"

    querystring = {"iso":"CHN"}

    headers = {
        'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
        'x-rapidapi-key': "96c395c12bmsh7977f2a7f725335p156aa1jsn3256842e9bbc"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    r = response.text
    r = r.replace('"','')
    r = r.replace('{','')
    r = r.replace('}','')
    r = r.replace(',','')

    ##Get info
    return r
if __name__ == "__main__":
    x = main()
    print(x)