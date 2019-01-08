#python script for finding spam content in files

import fileinput
import re

for line in fileinput.input(inplace=1):
        line = re.sub('<p\s\w+.*?(viagra)?<\/p>', '', line)
        print(line)
