#!/usr/bin/env python
# -*- coding: utf8 -*-

import subprocess
import sys

# Check input arguments
if len(sys.argv) > 2:
    print('Error! You must provide items to search for!', file=sys.stdout)
    sys.exit(1)

# Obtain search result, decode bytes type to str
c = subprocess.Popen(('brew search ' + sys.argv[1]).split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
c.wait()
stdout, stderr = c.communicate()
stdout = stdout.decode('utf-8').splitlines()  # list
stderr = stderr.decode('utf-8')  # str

if stderr:
    print(stderr, file=sys.stderr)
    sys.exit(1)

# Call brew-info command if any search results were returned
if stdout:
    for i, el in enumerate(stdout):
        print('')
        if el.startswith('Caskroom/cask/'):
            subprocess.call(('brew cask info ' + el).split())
        else:
            subprocess.call(('brew info ' + el).split())
        if i < len(stdout):
            print('\n' + '≈'*79)
else:
    print('No results found.')
