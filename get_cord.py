#/bin/usr/python

from geopy import geocoders

input_file = open("countries","r+")

for countr in input_file.readlines() :
    try :
        print countr

    except:
        print "couldn't print"
