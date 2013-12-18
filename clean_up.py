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
        
        
    ##NOW WE HAVE A DICTIONARY FOR FINDING THE LAT AND LONG
    #----Check 
#    print country_cord
    input_data = open(,"r+")
    
main()
