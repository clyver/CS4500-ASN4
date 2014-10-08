#!/usr/bin/python

import sys
import os
import wave

# Check to make sure we have the correct number of args, along with '-f's
if len(sys.argv) != 5 or sys.argv[1] != '-f' or sys.argv[3] != '-f':
    print 'ERROR: incorrect command line'
else:
    # Check to make sure the first file argument exists
    if not os.path.isfile(sys.argv[2]):
        print 'Error: {arg} does not exist'.format(arg=sys.argv[2])
    # Check to make sure the seconds file argument exists
    elif not os.path.isfile(sys.argv[4]):
        print 'Error: {arg} does not exist'.format(arg=sys.argv[4])
    # Ensure the first file argument is in the .wav format
    elif sys.argv[2][-4:] != '.wav':
        print 'Error: {arg} is not a supported format'.format(arg=sys.argv[2])
    # Ensure the second file argument is in the .wav format
    elif sys.argv[4][-4:] != '.wav':
        print 'Error: {arg} is not a supported format'.format(arg=sys.argv[4])
    elif:
        # Ensure wave.open works on both file inputs
        try:
            wave1 = wave.open(sys.argv[2], 'r')
        except TypeError:
            print "{arg} does not meet .wav requirement".format(arg=sys.argv[2])
        try:
            wave2 = wave.open(sys.argv[4], 'r')
        except TypeError:
            print sys.argv[4] + "does not meet .wav requirement"


