import re
#part I
print len([w for w in open('inputday5.txt') if (re.search(r'([aeiou].*){3,}',w) and re.search(r'(.)\1', w) and not re.search(r'ab|cd|pq|xy', w))])

#part II
print len([w for w in open('inputday5.txt') if (re.search(r'(..).*\1', w) and re.search(r'(.).\1', w))])