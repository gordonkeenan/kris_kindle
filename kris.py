import sys
import random

def readgivers(filename):
	f = open(filename,'r')
	givers = f.read().splitlines()
	f.close()
	return givers

if len(sys.argv) != 2: sys.exit("Usage: python kris.py [list of name]")
givers = readgivers(sys.argv[1])
receivers = givers[:]

random.shuffle(givers,random.random)
random.shuffle(receivers,random.random)

try:
	giftMatches = []
	for name in givers:
		if len(receivers) == 1 and name == receivers[0]: 
			raise Exception("The last person got left on his own, try running again")
		asigned = False
		while not asigned:
			x = random.randint(0, len(receivers)-1)
			if name != receivers[x]:
				#print name + " -> " + receivers[x]
				giftMatches.append((name, receivers[x]))
				receivers.pop(x)
				asigned = True
			else:
				print "Trying again"
	if len(giftMatches) != len(givers): raise Exception("Something went wrong givers[%d] receivers[%d]" % (len(giftMatches), len(givers),))
	for g,r in giftMatches:
			#print g + " " + r
			f = open(g,'w')
			f.write(r)
			f.close
except Exception as e: print 'Error:', e


