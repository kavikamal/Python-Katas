
sampleArray = [469, 755, 244, 245, 758, 450, 302, 20, 712, 71, 456, 21, 398, 339, 882, 848, 179, 535, 940, 472]

def print_kata(kata_desc,result):
    print kata_desc,result

print ' 1. ----------------------------'
def num_up(x):
    """ Print the numbers from 1 to 20. (1, 2, 3, ...,19, 20) """
    return " ".join(str(i) for i in range(1,x+1))
print_kata("Print the numbers from 1 to 20.", num_up(20))
print " ".join(map(lambda x : x,range(1,21)))

print ' 2. ----------------------------'
def even_up(x):
    """  Print the even numbers from 1 to 20. (2, 4, 6, ..., 18, 20) """
    return " ".join (str(i) for i in range(1,x+1) if i%2==0)
print_kata("Print the even numbers from 1 to 20 :", even_up (20))

print ' 3. ----------------------------'    
def odd_up(x):
    """ Print the odd numbers from 1 to 20. (1, 3, 5, ..., 17, 19) """
    return " ".join (str(i) for i in range(1,x+1) if i%2!=0)
print_kata("Print the odd numbers from 1 to 20 :", odd_up(20)) 

print ' 4. ----------------------------'
def multiples_up(x):
    """ Print the multiples of 5 up to 100. (5, 10, 15, ..., 95, 100) """
    return " ".join(str(i) for i in range(5,x+1,5))
print_kata("Print the multiples of 5 up to 100: ",multiples_up(100))  

print ' 5. ----------------------------'  
def squares_up(x):
    """ Print the square numbers up to 100. (1, 4, 9, ..., 81, 100) """
    return " ".join(str(i) for i in range(1,x+1) if i**.5%1==0)
print_kata("Print the square numbers up to 100: ", squares_up(100))

print ' 6. ----------------------------' 
def num_down(x):
    """ Print the numbers counting backwards from 20 to 1. (20, 19, 18, ..., 2, 1) """
    return " ".join(str(i) for i in range(x,0,-1))
print_kata("Print the numbers counting backwards from 20 to 1: ", num_down(20)) 

print ' 7. ----------------------------'
def even_down(x):
    """ Print the even numbers counting backwards from 20. (20, 18, 16, ..., 4, 2) """
    return " ".join (str(i) for i in range(x,0,-1) if i%2==0)
print_kata("Print the even numbers from 20 to 2: ", even_down(20)) 

print ' 8. ----------------------------' 
def odd_down(x):
    """ Print the odd numbers from 20 to 1, counting backwards. (19, 17, 15, ..., 3, 1) """
    return " ".join (str(i) for i in range(x,0,-1) if i%2!=0)
print_kata("Print the odd numbers from 20 to 1: ", odd_down(20))     

print ' 9. ----------------------------' 
def multiples_down(x):
    """ Print the multiples of 5, counting down from 100. (100, 95, 90, ..., 10, 5) """
    return " ".join (str(i) for i in range(x,0,-5))
print_kata("Print the multiples of 5, counting down from 100: ",multiples_down(100))     

print ' 10. ----------------------------'
def squares_down(x):
    """ Print the square numbers, counting down from 100. (100, 81, 64, ..., 4, 1) """
    return " ".join(str(i) for i in range(x,0,-1) if i**.5%1==0)
print_kata("Print the square numbers, counting down from 100: ",squares_down(100)) 

print ' 11. ----------------------------'
def all_array(sample_arr):
    """ Print the 20 elements of sampleArray. (469, 755, 244, ..., 940, 472) """
    return " ".join(str(i) for i in sample_arr)
print_kata("Print the 20 elements of sampleArray: ", all_array(sampleArray) ) 

print ' 12. ----------------------------'
def even_array(sample_arr):
    """ Print all the even numbers contained in sampleArray. (244, 758, 450, ..., 940, 472) """
    return " ".join (str(i) for i in sample_arr if i%2==0)
print_kata("Print all the even numbers contained in sampleArray: ", even_array(sampleArray))  

print ' 13. ----------------------------'
def odd_array(sample_arr):
    """ Print all the odd numbers contained in sampleArray. (469, 755, 245, ..., 179, 535) """
    return " ".join (str(i) for i in sample_arr if i%2!=0)
print_kata("Print all the odd numbers contained in sampleArray: ", odd_array(sampleArray)) 

print ' 14. ----------------------------'
def square_array(sample_arr):
    """ Print the square of each element in sampleArray. (219961, 570025, ..., 222784) """
    return " ".join (str(i**2) for i in sample_arr )
print_kata("Print the square of each element in sampleArray: ", square_array(sampleArray))     

print ' 15. ----------------------------'
def sum_num(x):
    """ Print the sum of all the numbers from 1 to 20. """
    a=range(1,x+1)
    return sum(a)
print_kata("Print the sum of all the numbers from 1 to 20: ",sum_num(20)) 

print ' 16. ----------------------------'
print_kata("Print the sum of all the elements in sampleArray: ", sum(sampleArray))     

print ' 17. ----------------------------'
print_kata("Print the smallest element in sampleArray: ",min(sampleArray)) 

print ' 18. ----------------------------'
print_kata("Print the largest element in sampleArray: ",max(sampleArray)) 
 

