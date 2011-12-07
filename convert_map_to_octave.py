#!/usr/bin/env python
# Usage:
#   cat random_walk_08p_01.map | python convert_map_to_octave.py > output.txt

import sys
import optparse

def main():
    parser = optparse.OptionParser()
    (options, args) = parser.parse_args()

    mapfile = sys.stdin
    output = sys.stdout

    rows = None
    cols = None
    cur_row = 0
    cur_col = 0
    my_hill = None

    map = []

    for line in mapfile:
        if line.startswith("rows"):
            rows = int(line.split()[1])
        elif line.startswith("cols"):
            cols = int(line.split()[1])
        elif line.startswith("m "):
            row = []
            line = line[2:]
            cur_col = 0
            for char in line:
                if char == '.':
                    row.append(0)
                elif char == '%':
                    row.append(1)
                elif char == '0':
                    row.append(0)
                    my_hill = (cur_row, cur_col)
                else:
                    row.append(0)
                cur_col += 1
                    
            cur_row += 1
            map.append(row)

    output.write("map = [")
    for row in map:
        output.write("[")
        for col in row:
            output.write("%d " % (col))
        output.write("]; ")
        
    output.write("];\n")
    output.write("a = [[%d, %d];];\n" % my_hill)

if __name__ == "__main__":
    sys.exit(main())
