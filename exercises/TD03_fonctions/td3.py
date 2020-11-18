def tempsEnSeconde(temps):
    secondes = temps[0]*60*60*24 + temps[1]*3600 + temps[2]*60 + temps[3]
    return secondes


temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
     = seconde // (60*60*24)
    h = (seconde % (60*60*24)) // (60*60)
    m = ((seconde % (60*60*24)) % (60*60)) // 60
    s = ((seconde % (60*60*24)) % (60*60)) % 60 
    return temps

    
temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

temps = secondeEnTemps(100000)
print(j,"jours",h,"heures",m,"minutes",s,"secondes")
