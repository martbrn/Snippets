#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse

headpar = argparse.ArgumentParser(description="Head Detector")
headpar.add_argument('-o','--objective',help="objective")
headpar = headpar.parse_args()


def main():
	if headpar.objective:
		try:
			url = requests.get(headpar.objective)
			headers = dict(url.headers)
			for x in headers:
				print(x + " : " + headers[x])
		except:
			print("Failed to connect")
	else:
		print("Put the objective")

if __name__ == '__main__':
	main()