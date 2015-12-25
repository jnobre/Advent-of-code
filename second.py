# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__' :

	sum = 0
	with open('input2.txt','r') as f:
		for line in f:
			print 'Ola : %s ' % line
			words = line.split('x')
			#print words
			l = int(line.split('x')[0])
			w = int(line.split('x')[1])
			h = int(line.split('x')[2][:-1])
			print '(%s,%s,%s)' % (l,w,h)
  			# 2*l*w + 2*w*h + 2*h*l
  			lw = l*w
  			wh = w*h
  			hl = h*l

  			sum = sum + 2*(l*w + w*h + h*l) + min(lw,wh,hl)

 	print 'Sum = %d' % sum