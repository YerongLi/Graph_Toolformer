import re
import sys

# define the regular expression pattern to match allowed characters
pattern = r'^[a-zA-Z0-9,-\.\s]+$'

# open the input file and read each line
with open(sys.argv[1], 'r') as f:
    for line in f:
        # check if the line contains any non-matching characters
        if not re.match(pattern, line):
            print(line)