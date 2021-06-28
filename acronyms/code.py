# function to create acronym
def fxn(stng):
    
    # add first letter
    oupt = stng[0]
      
    # iterate over string
    for i in range(1, len(stng)):
        if stng[i-1] == ' ':
            
            # add letter next to space
            oupt += stng[i]
              
    # uppercase oupt
    oupt = oupt.upper()
    return oupt
  
  
# input string
inpt1 = input("Enter a First Word Here : ")
  
# output acronym
print(fxn(inpt1))
  
# input string
inpt1 = input("Enter a Second Word Here : ")
  
# output acronym
print(fxn(inpt1))
  
# input string
inpt1 = input("Enter a Third Word Here : ")
  
# output acronym
print(fxn(inpt1))