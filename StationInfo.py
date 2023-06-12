import requests
import colorama
from colorama import Fore
import json
from datetime import datetime
import sys
from apscheduler.schedulers.background import BackgroundScheduler as scheduler


def main():
    apiKey = ''
    numResponses = '4'
    now = datetime.now()

    # Chicago Brown Line Request
    print("Chicago Brown Line")
    mapid = '40710'
    response = sendRequest(apiKey, mapid, numResponses)
    parseRequest(response, now)

    # Chicago Red Line Request
    print("Chicago Red Line")
    mapid = '41450'
    response = sendRequest(apiKey, mapid, numResponses)
    parseRequest(response, now)


def sendRequest(apiKey, mapid, numResponses):
    request = requests.get(
        "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=" + apiKey + "&mapid=" + mapid + "&max=" + numResponses + "&outputType=JSON")
    response = request.json()
    return response


def parseRequest(response, now):
    # Loop through each arriving train and get it's line color, direction, and mins to arrival
    for eta in response['ctatt']['eta']:
        color = eta['rt']
        bound = eta['destNm']
        arrivalTime = eta['arrT']
        datetime_arrivalTime = datetime.strptime(arrivalTime, '%Y-%m-%dT%H:%M:%S')
        timeToArrival = datetime_arrivalTime - now
        mins = round(timeToArrival.seconds/60)

        if mins <= 1:
            time = "Due"
        else:
            time = str(mins) + " mins"

        if color == 'Brn':
            print(Fore.YELLOW + bound + " " + time)
        elif color == 'P':
            print(Fore.MAGENTA + bound + " " + time)
        elif color == 'Red':
            print(Fore.RED + bound + " " + time)
        elif color == 'Y':
            print(Fore.YELLOW + bound + " " + time)
        elif color == 'Org':
            print(Fore.YELLOW + bound + " " + time)
        elif color == 'Blue':
            print(Fore.BLUE + bound + " " + time)
        elif color == 'Pink':
            print(Fore.CYAN + bound + " " + time)
        elif color == 'G':
            print(Fore.GREEN + bound + " " + time)

    print(Fore.RESET + "")

if __name__ == "__main__":
    main()
    # sch = scheduler()
    # sch.add_job(main, 'interval', seconds=5)
    # sch.start()
