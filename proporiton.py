#/bin/usr/python

#This piece of code is going to the GDP's in the table are fractions
#The globe doesn't take absolute data but rather comparative magnitude
#So we will create a new file where the data entries will be fracions of 1
#
#
#
def main():
    input_f = open("data","r+")
    total = [0,0,0,0]#total gdp of all countries++++++in increasing GDP order
#    input_data = [ [],[],[],[]]#each inner list is a year, increasing 09-->12
    for line in input_f.readlines():
#        print line
        k =  line.split()
        if (len(k)>5):
            numbers = k[-4: ]
            country = k[:-4]
            countr = " ".join(country)
            #numbers.insert(0,countr)
            #print numbers
            #print countr
#            print countr,numbers
#            print numbers
            for index in range(len(numbers)):#get the gdbs from each year and update the toal of each year

#               print numbers[index]
                pure_no = numbers[index].replace(",","")
#                print pure_no
                if ( pure_no.isdigit()):
                    
                    total[index] += int(pure_no)
    #            input_data[index-1].append(a_line)

    input_f.close()
    input_f2 = open("globe_data","r+")
    input_f1 = open("data","r+")
    

    t_2009 = total[0]
    t_2010 = total[1]
    t_2011 = total[2]
    t_2012 = total[3]
    for line in input_f1.readlines():
#        print line 
        k =  line.split()
        if (len(k)>5):
            numbers = k[-4:]
            country = k[:-4]
            countr = " ".join(country)
#            numbers.insert(0,countr)#now we have a list the country as 1 string and thnex
            new_numbers = ["0" for x in range(len(numbers))]
  
            for index in range(len(numbers)):
                pure_no = numbers[index].replace(",","")
                if ( pure_no.isdigit()):

                    new_numbers[index] = str(float(pure_no)/total[index])
                else:
                    continue 
            new_numbers.insert(0,countr)#now we have a list the country as 1 string and thne
#            print new_numbers
            print "  ".join(new_numbers)
        else:
            continue 
                
                
                
            
            
            
main()            
            
            
