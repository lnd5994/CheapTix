import unirest

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