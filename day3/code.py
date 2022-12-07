import numpy as np 
import math
import collections as col

'''
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, 
that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments.
 The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. 
Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in
 each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the 
 characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

    The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, 
	while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
    The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments 
	is uppercase L.
    The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
    The fourth rucksack's compartments only share item type v.
    The fifth rucksack's compartments only share item type t.
    The sixth rucksack's compartments only share item type s.

To help prioritize item rearrangement, every item type can be converted to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t),
 and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
'''
def chartoint(a):
	if a.islower():
		return ord(a)-96
	else:
		return ord(a) -38

def find_dup(r):
	l = len(r)//2
	print(r)
	for i in range(l):
		for j in range(l,2*l):
			if r[i]==r[j]:
				d = r[i]
				print(d,chartoint(d))
				return chartoint(d)
	return 0

def q1(rucksacks):
	priority = 0
	for r in rucksacks:
		priority+=find_dup(r)
	print(priority)
	return priority

def q2(rucksacks):
	l = len(rucksacks)
	badge=0
	for i in range(0,l,3):
		r0 =set(rucksacks[i]).intersection(rucksacks[i+1])
		r0 = r0.intersection(set(rucksacks[i+2]))
		badge +=chartoint(r0.pop())
	print(badge)
	return badge

def main():
	#path = str(input())
	path="./in"
	with open(path) as file:
		lines = file.readlines()
	
	rucksacks = []
	for l in lines:
		rucksacks.append(l.strip("\n"))
	print(rucksacks)
	#q1(rucksacks)
	q2(rucksacks)

if __name__=="__main__":
	main()
