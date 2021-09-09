#!/usr/bin/python

import argparse, scrapping, pprint

parser = argparse.ArgumentParser(description='website url/uri (str)')
parser.add_argument('--link', metavar='url_uri', type=str, nargs=1, help='The URL/URI to parse')
parser.add_argument('--depth', metavar='N', type=int, nargs=1, help='Retrieving recursively in depth N')


args = parser.parse_args()

website = args.link
d = args.depth[0]

plop = scrapping.scrapper(website, d)
plop = list(dict.fromkeys(plop))
for w in plop :
    print("[{position}]: {website}".format(position=plop.index(w), website=w))

     