import json
import requests

def fetch_shows(filmstar_name):
	base_url = "http://netflixroulette.net/api/api.php"
	url_params = { 'actor' : filmstar_name }
	try:
		r = requests.get(base_url, url_params)
		response = json.loads(r.text.encode('utf-8'))
		if type(response) == list and len(response) > 0:
				file_handle = open("cache-netflix.txt", 'w')
				for elem in response:
					file_handle.write(json.dumps(elem) + "\n")
				file_handle.close()
				print "Shows have been retrieved from Netflix Roulette API and written to the local cache successfully."
	except Exception, e:
		print "fetch_shows(): " + str(e)

fetch_shows("Dwayne Johnson")
