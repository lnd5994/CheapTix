import unirest
import fileinput
import json
import csv
import sys

# These code snippets use an open-source library. http://unirest.io/python
def send_request(event_id):
    url = "https://seatgeek-seatgeekcom.p.mashape.com/events/" + event_id
    response = unirest.get("https://seatgeek-seatgeekcom.p.mashape.com/events",
  	headers={
    	"X-Mashape-Key": "QIwvCntKFVmshkDMUmt3GQPh0e0Dp1qw4UXjsn6sCRSiFZ7rrq",
    	"Accept": "application/json"
  	 }
    )
    print "HELLO"
    print "Response body: ", response.body
    l = []
    for line in response.body:
        l.append(line)
    myjson = json.loads(response.raw_body) 
    keys = {}
    for i in myjson:
        print "i is: ", i
        for k in i.keys():
            keys[k] = 1
    mycsv = csv.DictWriter(sys.stdout, fieldnames=keys.keys(),
                       quoting=csv.QUOTE_MINIMAL)
    mycsv.writeheader()
    for row in myjson:
        mycsv.writerow(row)

