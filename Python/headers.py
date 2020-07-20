#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse

parser = argparse.ArgumentParser(description="Head Detector")
parser.add_argument('-o','--objective',help="objective")
parser = parser.parse_args()


def main():
	if parser.objective:
		try:
			url = requests.get(parser.objective)
			headers = dict(url.headers)
			for x in headers:
				print(x + " : " + headers[x])
		except:
			print("Failed to connect")
	else:
		print("Put the objective")

if __name__ == '__main__':
	main()