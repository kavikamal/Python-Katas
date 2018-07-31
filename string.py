def to_camel_case(str1):
    words=str1.split("-")
    result = [words[i] if i==0 else words[i].capitalize() for i in range(len(words)) ]
    return "".join(result)

def find_nth_occurrence(substr,str1,n):
    import re
    result = [m.start() for m in re.finditer('(?='+substr+')', str1)]
    if n-1<len(result):
         return result[n-1]
    else:     
        return -1 

def bumps(str1):
    count=0
    for i in str1:
        if i=='n':
           count+=1
    if count>15:
        return "Car Dead"  
    else:
        return "Woohoo!"      
   

def reverse_string(str1): 
    return " ".join([s[::-1] for s in str1.split(" ")])
    

print(to_camel_case("The-stealth-warrior"))

string = "This is an example. Return the nth occurrence of example in this example string."
print (find_nth_occurrence("example", string, 2))
print (find_nth_occurrence("TestTest", "TestTestTestTest", 3))

print(bumps("_nnnnnnn_n__n______nn__nn_nnn"))
print(bumps("______n___n_"))

print(reverse_string("This is an example!"))

