import requests
def main():
    log = open("log.txt", "w")
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    querystring = {"country": "USA"}
    headers = {
	    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
	    'x-rapidapi-key': "b087d3c483msha78ec3f9ef8104cp1b83e5jsn6eb7ac519d97"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)

    r = response.text
    r = r.replace('"','')
    r = r.replace('{','')
    r = r.replace('}','')
    r = r.replace(',',' ')
    r = r.replace('covid19Stats:[',"")

    ##Get info
    tConf = []
    while r.find("confirmed:") != 0:
        conf = r.find("confirmed")
        confEnd = r.find(" deaths:")
        x = r[conf+10:confEnd]
        log.write(x)
        ##print(x)
        tConf.append(int(x))
        ##r = r[conf+10:confEnd:]
    print(sum(tConf))
    return r
if __name__ == "__main__":
    x = main()
    print(x)
