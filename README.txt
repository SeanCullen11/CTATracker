Built with Python 3.10.11 and using an Anaconda environment with the packages in requirements.txt

StationInfo.py returns infomration from a fixed single station or set of stations
AllTrains.py allows you to pick a station by name and it will change the api request to get that station info

The station id numbers for each station can be found in the 'stations' dictionary in AllTrains.py

Replace the api key value with your own, change the station id to your desired station and it's good to go

Both programs will return the next 4 trains to arrive at the station and print them in the color of the train
(terminal colors are a bit limited so not all colors are perfect)

To Do:
- Add a scheduler to send the api call every minuite while the program runs
- Add code to print text on LED board
- Integrate aletrs api notifications
