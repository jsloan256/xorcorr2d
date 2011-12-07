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
    e1_hill = None
    e2_hill = None
    e3_hill = None
    e4_hill = None
    e5_hill = None
    e6_hill = None
    e7_hill = None

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
                elif char == '1':
                    row.append(0)
                    e1_hill = (cur_row, cur_col)
                elif char == '2':
                    row.append(0)
                    e2_hill = (cur_row, cur_col)
                elif char == '3':
                    row.append(0)
                    e3_hill = (cur_row, cur_col)
                elif char == '4':
                    row.append(0)
                    e4_hill = (cur_row, cur_col)
                elif char == '5':
                    row.append(0)
                    e5_hill = (cur_row, cur_col)
                elif char == '6':
                    row.append(0)
                    e6_hill = (cur_row, cur_col)
                elif char == '7':
                    row.append(0)
                    e7_hill = (cur_row, cur_col)
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
    output.write("my_hill = [[%d, %d];];\n" % my_hill)
    if e1_hill != None:
        output.write("e1_hill = [[%d, %d];];\n" % e1_hill)
    if e2_hill != None:
        output.write("e2_hill = [[%d, %d];];\n" % e2_hill)
    if e3_hill != None:
        output.write("e3_hill = [[%d, %d];];\n" % e3_hill)
    if e4_hill != None:
        output.write("e4_hill = [[%d, %d];];\n" % e4_hill)
    if e5_hill != None:
        output.write("e5_hill = [[%d, %d];];\n" % e5_hill)
    if e6_hill != None:
        output.write("e6_hill = [[%d, %d];];\n" % e6_hill)
    if e7_hill != None:
        output.write("e7_hill = [[%d, %d];];\n" % e7_hill)

if __name__ == "__main__":
    sys.exit(main())
