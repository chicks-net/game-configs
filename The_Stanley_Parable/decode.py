#!/usr/bin/env python
"""decode secret message from clipboard in The Stanley Parable"""

numbers = []

with open('number_message.txt') as msg:
	for line in msg:
		tokens = line.split()
		#print "line had " + str(len(tokens)) + " items"
		for tok in tokens:
			numbers.append(int(tok))

print "got " + str(len(numbers)) + " numbers"

characters = []
for num in numbers:
	characters.append(str(chr(num)))
	#print str(num) + ' -> ' + str(chr(num))

print "".join(characters)
