#/usr/bin/python

# coding=utf-8
from geopy import geocoders

input = open("data.txt","r+")
out = open("output.txt","w")
def format (line):

    s = line.split()
    ls = len(s)
    country = s[1:ls-4]
    country = " ".join(country)
    if ( country == "C\xc3\xb4te d'Ivoire"):
        return -1 
    ten = float(s[-1])
    five = float(s[-2])
    zero = float(s[-3])
    nine = float(s[-4])
    return [ country , nine, zero, five,ten]

g = geocoders.GoogleV3()


#location, (lat, lng) = g.geocode("Spain")
#location, (lat, lng) = g.geocode("Hong Kong, China (SAR)")
#location, (lat, lng) = g.geocode("Austria" )



max_1990 = 0 
max_2000 =0
max_2005 = 0
max_2010 = 0

out_data = ['1990',[],'2000',[],'2005',[],'2010',[]]


for line in input.readlines():
    '''
    k =  line.split()
    k = k[1: len(k)-4]
    k = "".join(k)
    print k 
    '''
    print "WTF"
    line_f =  format(line)
    if line_f != -1 :
        print (line_f[0])
        location, (lat, lng) = g.geocode(line_f[0] )
        out.write(line_f[0] + " " +str(lat) + " " + str(lng)+ "\n")
    else:
        print "NEED ENCODING"
        

        
'''        
        nine = line_f[1]
        zero = line_f[2]
        five = line_f[3]
        ten = line_f[4]
        out_data[1].extend([lat,lng,nine])
        out_data[3].extend([lat,lng,zero])
        out_data[5].extend([lat,lng,five])
        out_data[7].extend([lat,lng,ten])           
        print out_data
'''
#    else:
 #ca       print "NEED ENCODING"
        

    
    
