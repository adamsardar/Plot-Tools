#!/usr/bin/env python

import sys
import argparse
import re
from os import system
from ete2a1 import Tree, TreeStyle, NodeStyle


parser = argparse.ArgumentParser(description = "Display a phylogenetic tree.")
#parser.add_argument('trees', metavar='T', nargs='+', type=argparse.FileType('r'), help="a phylogenetic tree to render interactively.", required=True )
parser.add_argument('-f','--format', action="store", default="square")
parser.add_argument('trees', metavar='T', nargs='+', type=str, help="a phylogenetic tree to render interactively.")
args = parser.parse_args()

if not (args.format == "square" or args.format == "circle"):
		sys.stderr.write("Format should either be 'square' or 'circle'\n\n")
		parser.print_help(sys.stderr)
		sys.exit(1)

def filterNames(names,reg):
	return [i for i in names if reg(i)]


def colourNodes(tree,names,colour):
	is_arabidopsis = re.compile('.*Arabidopsis.*thal.*').match;
	for name in names:
		if is_arabidopsis(name):
			for n in tree.get_leaves_by_name(name):
				nstyle = NodeStyle()
				nstyle["bgcolor"] = 'red'
				n.set_style(nstyle)
		else:
			for n in tree.get_leaves_by_name(name):
				nstyle = NodeStyle()
				nstyle["bgcolor"] = colour
				n.set_style(nstyle)

#t = PhyloTree("RAxML_result.ITPR_LIKE_CHANNEL", alignment="hits_align.phy", alg_format="iphylip")
#t.show()

t = Tree(args.trees[0])


#Get leaves
#names = t.get_leaf_names()

#algae = filterNames(names, re.compile('.*ALGA.*').match)
#plants = filterNames(names, re.compile('.*PLANT.*').match) 

#colourNodes(t,algae,"green")
#colourNodes(t,plants,"#4ED34E")

circle = TreeStyle()
circle.show_leaf_name = True
#circle.scale =  3
circle.mode = "c"
circle.arc_start = 0 # 0 degrees = 3 o'clock
circle.arc_span = 360
circle.show_branch_length = True

square = TreeStyle()
square.show_leaf_name = True
#square.scale = 5
square.show_branch_length = True

#t.render("out.png", tree_style=circle, dpi=48000)
#system("convert -trim out.png itpr_channel_circle.png && rm out.png")

style = square if args.format == "square" else circle

t.show( tree_style=style)
#system("convert -trim out.png itpr_channel_normal.png && rm out.png")

