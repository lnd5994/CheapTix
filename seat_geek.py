import unirest
<<<<<<< HEAD
import fileinput
import json
import csv
import sys

=======
import json_to_csv.py
<<<<<<< HEAD
>>>>>>> 7988f9583fd6c30e5f8a2eaa326341d6c67c5250
=======
import fileinput
import json
import csv
import sys
>>>>>>> ce4346dbaa875875a78ee259f01b032d08773943

# These code snippets use an open-source library. http://unirest.io/python
def send_request(event_id):
	url = "https://seatgeek-seatgeekcom.p.mashape.com/events/" + event_id
	response = unirest.get("https://seatgeek-seatgeekcom.p.mashape.com/events",
  	headers={
    	"X-Mashape-Key": "QIwvCntKFVmshkDMUmt3GQPh0e0Dp1qw4UXjsn6sCRSiFZ7rrq",
    	"Accept": "application/json"
  		}
	)

	print response.body

    l = []
    #for line in fileinput.input(seat_geek.py):
    for line in response.body:
        l.append(line)
    myjson = json.loads(''.join(l))
    keys = {}
    for i in myjson:
        for k in i.keys():
            keys[k] = 1
    mycsv = csv.DictWriter(sys.stdout, fieldnames=keys.keys(),
                       quoting=csv.QUOTE_MINIMAL)
    mycsv.writeheader()
    for row in myjson:
        mycsv.writerow(row)
