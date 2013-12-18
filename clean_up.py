#/bin/usr/python 

input_file = open("cia_cords","r+")

for line in input_file.readlines():

    s = line.split()
    ls = len(s)
    print s
    print s[:-6]
#    country = s[1:ls-4]
 #   country = " ".join(country)
#    print " ".join(s[:-7]) + str(s[-6:]) + "\n"
    
    
