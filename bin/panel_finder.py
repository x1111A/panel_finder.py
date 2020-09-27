#!/usr/bin/python3.7


# panel_finder.py - simple tool for finding administrator panel
# on selected website.
# Usage: panel_finder.py www.example.com wordlist.txt
# Paths located in text files should begin with '/'

import requests
from sys import argv



def finder(website,textfile):
	path_file = open(str(textfile),'r')
	result = []
	for line in path_file:
		r = requests.get(f'https://{website}{line}')
		print(f'[#]Trying {website}{line}')
		if r.status_code == 200:
			print(f'>>> Admin panel found:https://{website}{line}')
			result.append(f'https://{website}{line}')
		else:
			print("Page doesn't exist or invalid url.")
	return result


def getResult(res):
	print(40 * '-')
	print('List of admin panels found:')
	if len(res) == 0:
		print('No admin panels found.')
	else:
		for r in res:
			print(r)


if len(argv) == 3:
	getResult(finder(argv[1],argv[2]))
else:
	print('Usage: panel_finder.py www.example.com wordlist.txt')
