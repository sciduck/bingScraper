from requests import exceptions 
import argparse 
import requests
import cv2 
import os

#argument parser -> parse argument
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
	help = "Search query to search Bing Image API for")

ap.add_argument("-o", "--output", required = True,
	help = "Output directory")

ap.add_argument("-n", "--number", required = False,
	help = "Number of desired results")

args = vars(ap.parse_args())

EXCEPTIONS = set([IOError, FileNotFoundError,
	exceptions.RequestException, exceptions.HTTPError,
	exceptions.ConnectionError, exceptions.Timeout])

API_KEY = open("api.key").readlines()[0].rstrip()
URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

MAX_RESULTS = int(args["number"])

"""
Increase the group_size if you are rich $_$

You can think of the GROUP_SIZE parameter as the 
number of search results to return “per page”. 
Therefore, if we would like a total of 250 images, 
we would need to go through 5 “pages” with 50 images “per page”.
"""

GROUP_SIZE = 10

term = args["query"]
headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
params = {"q": term, "offset": 0, "count": GROUP_SIZE}

print("[INFO] Making a Bing Search for {}".format(term))
search = requests.get(URL, headers = headers, params = params)
search.raise_for_status()

results = search.json()
estNumResults = min(results["totalEstimatedMatches"], MAX_RESULTS)
print("[INFO] {} total results for '{}'".format(estNumResults,
	term))

#counter
total = 0
for offset in range(0, estNumResults, GROUP_SIZE):
	print("[INFO] making request for group {}-{} of {}...".format(
		offset, offset + GROUP_SIZE, estNumResults))
	params["offset"] = offset
	search = requests.get(URL, headers=headers, params=params)
	search.raise_for_status()
	results = search.json()
	print("[INFO] saving images for group {}-{} of {}...".format(
		offset, offset + GROUP_SIZE, estNumResults))

	for v in results["value"]:
		try:
			print("[INFO] fetching: {}".format(v["contentUrl"]))
			r = requests.get(v["contentUrl"], timeout=30)
			ext = v["contentUrl"][v["contentUrl"].rfind("."):]
			p = os.path.sep.join([args["output"], "{}{}".format(
				str(total).zfill(8), ext)])
			f = open(p, "wb")
			f.write(r.content)
			f.close()
		except Exception as e:
			if type(e) in EXCEPTIONS:
				print("[INFO] skipping: {}".format(v["contentUrl"]))
				continue

		image = cv2.imread(p)
		if image is None:
			print("[INFO] deleting: {}".format(p))
			os.remove(p)
			continue
		total += 1


