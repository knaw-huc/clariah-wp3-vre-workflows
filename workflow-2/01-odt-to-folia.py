#!/usr/bin/env python3

import random
import sys
import time

import clam.common.client
import clam.common.status
import yaml
# pip3 install piereling
from piereling.piereling import CUSTOM_FORMATS

with open('config.yml') as ymlfile:
    cfg = yaml.load(ymlfile)

INPUT = cfg['odtFile']
OUTPUT = cfg['xmlFile']

CLAM_USER = cfg['clam']['user']
CLAM_PASS = cfg['clam']['pass']
PIER_HOST = cfg['pier']

pier = clam.common.client.CLAMClient(PIER_HOST, CLAM_USER, CLAM_PASS,
                                     basicauth=True)

pier.register_custom_formats(CUSTOM_FORMATS)

project = "clariah" + str(random.getrandbits(64))

print("Creating project: " + project)
pier.create(project)

data = pier.get(project)

print("Adding input file: " + INPUT)
pier.addinputfile(project, data.inputtemplate("odt2folia_in"), INPUT)

print("Starting conversion:")
data = pier.start(project)

if data.errors:
    print("An error occured: " + data.errormsg, file=sys.stderr)
    for parametergroup, paramlist in data.parameters:
        for p in paramlist:
            if p.error:
                print("Error in parameter " + p.id + ": " + p.error,
                      file=sys.stderr)

    pier.delete(project)
    sys.exit(1)

while data.status != clam.common.status.DONE:
    time.sleep(0.5)  # wait a while before polling status again
    data = pier.get(project)  # get status again
    print("\tRunning: %3s%% -- %s" % (str(data.completion), data.statusmessage),
          file=sys.stderr)

for outputfile in data.output:
    try:
        outputfile.loadmetadata()
    except:
        continue

    outputtemplate = outputfile.metadata.provenance.outputtemplate_id
    if outputtemplate == "odt2folia_out":
        print("Intermediate result: " + OUTPUT)
        outputfile.copy(OUTPUT)

# Cleanup time
print("Deleting project: " + project)
pier.delete(project)
