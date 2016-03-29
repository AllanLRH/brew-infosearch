#!/usr/bin/env python
# -*- coding: utf8 -*-

import subprocess
import sys
import re

# Check input arguments
if len(sys.argv) > 2:
    print('Error! You must provide items to search for!', file=sys.stdout)
    sys.exit(1)

tapRx = re.compile(r'[\w_-]+?/([\w_-]+)(?:/.)?')
brewTapList = [tapRx.match(el).groups()[0] for el in subprocess.check_output('brew tap'.split()).decode('utf8').splitlines()]

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
    PRINTLINE = False
    for i, el in enumerate(stdout):
        print('')
        m = tapRx.match(el)
        if m:
            prefix = m.groups()[0]
            if prefix in brewTapList:
                subprocess.call(['brew', prefix, 'info', el])
                PRINTLINE = True
        else:
            subprocess.call(('brew info ' + el).split())
            PRINTLINE = True
        if i < len(stdout)-2 and PRINTLINE:
            print('\n' + '≈'*79)
else:
    print('No results found.')
