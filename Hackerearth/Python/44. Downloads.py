import requests
import json
import urllib3
import re
import concurrent.futures
import os
from concurrent.futures import 
def main():
    linksFile = "downloads.json"
    with open(linksFile, 'r') as f: contents = json.loads(f.read().strip())
    l=[]
    for i in contents.items():
        l.append(i)
    for j in range(2,len(l)):
        downloadVideos(l[j][0], l[j][-1])

if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            exit("[!] okay-sed :(")
