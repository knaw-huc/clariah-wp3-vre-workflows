#!/usr/bin/env python3

import clam.common.client
import clam.common.data
import clam.common.status
import random
import sys
import os
import time
import yaml

# process Word file converted using 'Piereling' with 'Frog'

with open('config.yml') as ymlfile:
    cfg = yaml.load(ymlfile)

INPUT  = cfg['files']['pier']
OUTPUT = cfg['files']['frog']

CLAM_USER = cfg['clam']['user']
CLAM_PASS = cfg['clam']['pass']
FROG_HOST = cfg['frog']['host']
FROG_SKIP = cfg['frog']['skip']

frog = clam.common.client.CLAMClient(FROG_HOST, CLAM_USER, CLAM_PASS,
        basicauth=True)

project = "clariah" + str(random.getrandbits(64))
print("Creating project: " + project)
frog.create(project)

data = frog.get(project)

print("Adding input file: " + INPUT)
frog.addinputfile(project, data.inputtemplate("foliainput"), INPUT)

print("Starting conversion (skip=%s):"% FROG_SKIP)
data = frog.start(project, skip=FROG_SKIP)

if data.errors:
    print("An error occured: " + data.errormsg, file=sys.stderr)
    for parametergroup, paramlist in data.parameters:
        for p in paramlist:
            if p.error:
                print("Error in parameter " + p.id + ": " + p.error,
                        file=sys.stderr)

    frog.delete(project)
    sys.exit(1)

while data.status != clam.common.status.DONE:
    time.sleep(1) # wait a while before polling status again
    data = frog.get(project) # get status again
    print("\tRunning: %3s%% -- %s" % (str(data.completion), data.statusmessage),
            file=sys.stderr)

for outputfile in data.output:
    try:
        outputfile.loadmetadata()
    except:
        continue

    outputtemplate = outputfile.metadata.provenance.outputtemplate_id
    if outputtemplate == "foliaoutput":
        print("Frog result: " + OUTPUT)
        outputfile.copy(OUTPUT)

# Cleanup time
print("Deleting project: " + project)
frog.delete(project)
