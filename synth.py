#/usr/bin/python
from geopy import geocoders

input = open("data.txt","r+")

def format (line):

    s = line.split()
    ls = len(s)
    country = s[1:ls-4]
    country = "".join(country)
    ten = float(s[-1])
    five = float(s[-2])
    zero = float(s[-3])
    nine = float(s[-4])
    return [ country , nine, zero, five,ten]

g = geocoders.GoogleV3()


#location, (lat, lng) = g.geocode("Spain")
#location, (lat, lng) = g.geocode("Hong Kong, China (SAR)")
location, (lat, lng) = g.geocode("Korea (Democratic People's Rep. of)" )


print lat, lng

for line in input.readlines():
    '''
    k =  line.split()
    k = k[1: len(k)-4]
    k = "".join(k)
    print k 
    '''
    print format(line)
