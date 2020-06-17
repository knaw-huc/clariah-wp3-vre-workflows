#!/usr/bin/env python3
import os
import random
import sys
import time

import clam.common.client
import clam.common.status
import yaml

'''
See webservices-lst.science.ru.nl/piccl/info for 
more information about the clam client and the piccl api.
'''

with open('config.yml') as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

clamclient = clam.common.client.CLAMClient(
    config['host'],
    config['clam']['user'],
    config['clam']['pass'],
    basicauth=True
)

project = "projectname" + str(random.getrandbits(64))

clamclient.create(project)

data = clamclient.get(project)

localfilename = os.path.basename(config['inputfiles'][0])
inputtemplate = "tif"
clamclient.addinputfile(project, data.inputtemplate(inputtemplate), localfilename)

data = clamclient.startsafe(
    project,
    lang='nld',
    ticcl='yes',
    frog='yes',     # still seems to be called?
    rank=1,        # required
    distance=2     # required
)

while data.status != clam.common.status.DONE:
    time.sleep(0.5)
    data = clamclient.get(project)
    print("\tRunning: %3s%% -- %s" % (str(data.completion), data.statusmessage), file=sys.stderr)

if not os.path.exists(config['outputTiccl']):
    with open(config['outputTiccl'], 'w'): pass

for outputfile in data.output:
    try:
        outputfile.loadmetadata()
        outputtemplate = outputfile.metadata.provenance.outputtemplate_id
        print('outputtemplate: ' + outputtemplate)
        if outputtemplate == 'frogfolia':
          outputfile.copy(config['outputTiccl'])
    except:
        print('could not load metadata')

clamclient.delete(project)
