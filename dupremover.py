import sys
import time as t

def get_time():
	return t.strftime('%H:%M:%S')

try:
	fileName = sys.argv[1]
except:
	print('You didn\'t supply a valid filename.')
	exit()

with open(fileName, 'r') as f:
	file = f.readlines()

wordList = []
badList = []

for line in file:
    if line in wordList:
        badList.append(line)
    else:
        wordList.append(line)

file = open(fileName, 'w')

for line in wordList:
	file.write(line)

file.close()

print('[{0}]: {1} duplicate lines removed from {2}.'.format(get_time(), len(badList), fileName))