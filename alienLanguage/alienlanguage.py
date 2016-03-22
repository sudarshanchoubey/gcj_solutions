import sys
import re
std_in = sys.stdin
def conv_to_regex(inp):
    res = re.sub('\(','[',inp)
    res = re.sub('\)',']',res)
    return res
L, D, N = map(int, std_in.readline().split(' ',3))
words = set()
for i in range(D):
   words.add(std_in.readline())
#print(words)
for i in range(N):
    word = std_in.readline()
    rword = conv_to_regex(word)
    count = 0
    for one_word in words:
        match = None
#        p = re.compile(rword)
#        print("rword is " + rword)
        match = re.match(rword,one_word)
        if match != None:
            count = count + 1
    print("Case #" + str(i+1) + ": " + str(count))


