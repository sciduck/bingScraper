from requests import exceptions 
import argparse 
import requests
import cv2 as cv
import os

#argument parser -> parse argument
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
	help = "Search query to search Bing Image API for")
ap.add_argument("-o", "--output", required = True,
	help = "Output directory")
args = vars(ap.parse_args())