#/usr/bin/python
from geopy import geocoders

input = open("data.txt","r+")

def format (line):

    s = line.split()
    ls = len(s)
    country = s[:ls-4]
    ten = s[-1]
    five = s[-2]
    zero = s[-3]
    nine = s[-4]
    return 

g = geocoders.GoogleV3()


#location, (lat, lng) = g.geocode("Spain")
#location, (lat, lng) = g.geocode("Hong Kong, China (SAR)")
location, (lat, lng) = g.geocode("Korea (Democratic People's Rep. of)" )


print lat, lng

for line in input.readlines():
    k =  line.split()
    k = k[1: len(k)-4]
    k = "".join(k)
    print k 
