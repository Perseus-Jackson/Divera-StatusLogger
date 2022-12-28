# Status Logger for Divera 24/7
This project is able to get the status of all your users at specific times of the day. The data can then be used for 
statistics or performance reviews and further analytics.

## Functionality
This program is sending an HTTPS request to the Divera API with the url and accesskey provided in the config file at
12am, 8am, 12pm, 4pm and 8pm every day, using the python schedule package, and saves the number of users at each status 
in a json file in the out directory. The file names represent the date and time, when the API has been called.<br>
You can easily change the times, when the requests are send by editing the schedule.<br>
In case the request fails, the system will automatically retry up to 5 times. After that the program will abort and wait till the next trigger 
in the schedule is reached.

## Installation
1. Download the repository 
2. Execute the setup.sh with  `sudo sh ./setup.sh`
3. Change the config file and add your accesskey
4. Execute the python file `python3 divera_status_logger.py`

## Config File
The config file contains the data that is needed to send requests to the Web API. 
```
{
    "url":"https://app.divera247.com/api/users?accesskey=",
    "accesskey":"YOUR_ACCESSKEY"
}
```

## Log File
When the system is up and running, a log file will be generated in the log directory, 
where you can see the current status of the program.

## Legal Advice
Because of the data protection laws in Germany the program will __NOT__ save any information about the users, 
e.g. at which times, which users have been on a specific status. The system will __ONLY__ save the number of users 
at each status of your unit.<br>
Furthermore, I would recommend to inform all users, about the collection of these 
information or even get their approval.

## Documentation
- Divera 24/7 Web API: https://www.divera247.com/funktionen/datenaustausch-alarmierung/web-api.html
- Python requests: https://www.geeksforgeeks.org/get-post-requests-using-python/
- Python schedule: https://schedule.readthedocs.io/en/stable/examples.html