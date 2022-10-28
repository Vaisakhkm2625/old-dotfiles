#!/bin/bash
qtile cmd-obj -o group 2 -f toscreen
brave $(python -c 'import os,urllib.parse; safe_string = urllib.parse.quote_plus(os.popen("xsel").read()); print("https://www.google.com/search?q="+safe_string)')

