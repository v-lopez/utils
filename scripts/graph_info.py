#!/usr/bin/env python

import pygraphviz as pgv
import sys

if __name__ == '__main__':
    print 'Loading file %s', sys.argv[1]
    graph = pgv.AGraph()
    graph.read(sys.argv[1])
    for node in graph.nodes():
        if len(graph.successors(node)) == 0:
            print graph.get_node(node).attr['label']
