import md5

data = 'iwrupvqb'
a=0
while True:
    if md5.new(data+str(a)).hexdigest()[:6] == '000000': #
        print a
    a+=1
