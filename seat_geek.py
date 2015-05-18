import unirest
import fileinput
import json
from csv import DictWriter
import sys
import json_to_csv.py

# These code snippets use an open-source library. http://unirest.io/python
# def send_request(event_id):
#     url = "https://seatgeek-seatgeekcom.p.mashape.com/events/" + event_id
#     #url = 'http://api.seatgeek.com/2/events/801255'
#     #response = unirest.get(url)
#     response = unirest.get(url,
#   	headers={
#     	"X-Mashape-Key": "QIwvCntKFVmshkDMUmt3GQPh0e0Dp1qw4UXjsn6sCRSiFZ7rrq",
#     	"Accept": "application/json"
#   	 }
#     )

def send_request(event_name):
    # These code snippets use an open-source library.
    url = "http://api.seatgeek.com/2/events?q=" + event_name
    response = unirest.get(url)
        # headers={
        #     "X-Mashape-Key": "QIwvCntKFVmshkDMUmt3GQPh0e0Dp1qw4UXjsn6sCRSiFZ7rrq",
        #     "Accept": "application/json"
        # }
    #)

    jsonDump = json.dumps(response.body, sort_keys=True, indent = 4, separators=(',', ': '))
    jsonObject = json.loads(jsonDump)
    print jsonDump

    jsonEventsDump = json.dumps(jsonObject.values()[1], sort_keys=True, indent = 4, separators=(',', ': '))
    jsonEventsObject = json.loads(jsonEventsDump)
    field_names = ["announce_date", "created_at", "date_tbd", "datetime_local", "id"]
    file_name = "output_" + event_name + ".csv"
    # csv_file = open(file_name, "w")
    # writer = DictWriter(csv_file, fieldnames=field_names, delimiter=";")
    # writer.writeheader()
    # for item in jsonEventsObject:
    #     print item.values()
    #     data = {key: value for key, value in item if key in field_names}
    #     writer.writerows(data)

    # csv_file.close()
        

    # 
    # csv_file = open(file_name, "w")
    # writer = DictWriter(csv_file, fieldnames=field_names, delimiter=";")
    # writer.writeheader()
    # data = {key: value for key, value in jsonObject.values()[1] if key in field_names}
    # writer.writerows(data)
    # csv_file.close()

        

