import sys
import re

with open('inputday6.txt') as f:
    data = f.read().splitlines()

    lights = {}
    lights_part2 = {}

    for x in xrange(1000):
        for y in xrange(1000):
            lights[(x, y)] = False
            lights_part2[(x, y)] = 0

    for line in data:
        if line.count("turn on"):
            pairs = [map(int,x.split(',')) for x in re.findall(r"(\d+,\d+)", line)]
            begin, end = pairs
            for x in xrange(begin[0], end[0] + 1):
                for y in xrange(begin[1], end[1] + 1):
                    lights[(x, y)] = True
                    lights_part2[(x, y)] += 1
        elif line.count("turn off"):
            pairs = [map(int,x.split(',')) for x in re.findall(r"(\d+,\d+)", line)]
            begin, end = pairs
            for x in xrange(begin[0], end[0] + 1):
                for y in xrange(begin[1], end[1] + 1):
                    lights[(x, y)] = False
                    if (lights_part2[(x, y)] - 1) != -1:
                        lights_part2[(x, y)] -= 1
        else:
            pairs = [map(int,x.split(',')) for x in re.findall(r"(\d+,\d+)", line)]
            begin, end = pairs
            for x in xrange(begin[0], end[0] + 1):
                for y in xrange(begin[1], end[1] + 1):
                    lights[(x, y)] = not lights[(x, y)]
                    lights_part2[(x, y)] += 2
        #print pairs

    print "Part 1:", len(filter(lambda x: lights[x] is True, lights.keys()))
    print "Part 2:", sum(lights_part2.values())