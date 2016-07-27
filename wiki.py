#!/usr/bin/python
import json
import requests
import getopt
import sys
import webbrowser

LANG=""




def loadAndParse(url):
	requests.get(url).json()


def wikiSearch(searchTerm, language):
	found=False
	url="https://en.wikipedia.org/w/api.php?action=opensearch&search=" + searchTerm
	r=requests.get(url)
	json_objekt=r.json()
	if not json_objekt[1]:
		print "no page found"
		return "404.html"
		exit()
	page = json_objekt[1][0]
	origPage=json_objekt[3][0]
	if language=="":
	  return origPage
	  exit()
	urlpage = "https://en.wikipedia.org/w/api.php?action=parse&page=%s&prop=langlinks&format=json"%page
	# print urlpage
	r2 = requests.get(urlpage)
	json_objekt=r2.json()
	langarray = json_objekt["parse"]["langlinks"]

	if len(langarray)==0:
	  print "No alternative languages"
	  return origPage
	  exit()
	for langItem in langarray:
	  if langItem["lang"]==language:
	    return langItem["url"]
	    found=True
	if found==False:
	  print "Selected language not found, loading default. The following languages are available:"
	  for alt in langarray:
	    print alt["lang"]
	  return origPage


def usage():
	print "usage"

def main():
	language=LANG
	opts, args = getopt.getopt(sys.argv[1:], "hl:",["help", "lang"])
	if len(sys.argv)==1:
		print "Error, no input\n"
		usage()		
	for opt, arg in opts:
		if opt in ("-h","--help"):
			usage()
		if opt in ("-l","--lang"):
			language=arg
	for searchTerm in args:
		url = wikiSearch(searchTerm, language)
		print "TO LOAD:"
		print url
		webbrowser.open(url)


if (__name__ == "__main__"):
	main()

