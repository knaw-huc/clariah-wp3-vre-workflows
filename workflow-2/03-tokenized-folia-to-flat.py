#!/usr/bin/env python3
import requests
import yaml

with open('config.yml') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

XML_FILE = cfg['xmlFile']
FLAT_HOST = cfg['flatHost']
FLAT_UPLOADEND_POINT = cfg['flatUploadEndpoint']

with open(XML_FILE, 'rb') as f:
  url = FLAT_HOST + FLAT_UPLOADEND_POINT
  r = requests.post(url, files={'file': f, 'mode': 'editor'}, allow_redirects = False)
  if(r.status_code == 302):
    print('View file in flat: \n' + FLAT_HOST + r.headers['Location'])
  else:
    print('Something went wrong: ' + str(r.status_code) + ' - ' + r.text)
