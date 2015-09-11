##########################################################################################
#This program is to resolve the 1st Project Euler's problem, who is multiples of 3 and 5 #
#                                                                                        #
#Clement_Herat                                                                           #
##########################################################################################


def main ():
    somme = 0
    i = 1
    
    while i < 1000:
        if i%3 == 0 or i%5 == 0:
            somme = somme + i
        i += 1
    print somme
    
    
main ()
