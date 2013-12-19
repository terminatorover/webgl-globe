#/bin/usr/python 

def my_format( cords):
    '''given the input ['28', '12', 'N,', '177', '22', 'W']
    return the lat and the long in the form 
    [28,-177] note that the negative is to point out that its the WEST , and we ignore minutes since we are not 
    looking for that level of accuracy, we need a coordinate representation for the whole country "
    
    '''

    lat = int(cords[0])
    lng = int(cords[-3])
    if ( cords[2]== "S"):
        lat = lat*-1
    if ( cords[-1] == "W"):
        lng = lng * -1

    return [lat,lng]


def main():
    input_file = open("cia_cords","r+")

    country_cord ={}#this dictionary will have country:[lat,lng] as a key value pair

    for line in input_file.readlines():
        if (len(line) < 5 ):
            continue 
        s = line.split()
        ls = len(s)
        #print s
        country =  s[:-6]
#        print s[-6:]
        country = " ".join(country)
    

        country_cord[country]= my_format(s[-6:])
    data_input = open("data","r")
    DATA = ["2009",[],"2010",[],"2011",[],"2012"]#this will be converted to JSON 
    count = 0
    for line in data_input.readlines():
        k =  line.split()
        if (len(k)>5):
            numbers = k[1: len(k)-4]
            country = k[:-4]
            countr = " ".join(country)
#           if ( countr in country_cord.keys()):
 #               print "found----> " + countr
#                continue 
#            else:
#                print "coudn't find +++++>" + countr
            try: 
               print countr + " "  + str(country_cord[countr])
            except: 
               print "Couldn't find " + countr

    ##NOW WE HAVE A DICTIONARY FOR FINDING THE LAT AND LONG
    #----Check 
#    print country_cord

    
main()
