import random
import math

#is_prime allows to verify whether the number is prime or not.

def is_prime(num):
    
    divs_count=0
    
    for i in range(1, int(math.sqrt(num))+1):
        
        if num%i==0:
            
            divs_count+=1
            
    if divs_count==1:
        
        return True
    
    else:
        
        return False
    
#generate prime generates a prime number, this function is used to generate values for p and q.
    
def generate_prime():
    
    var=random.randint(1000,5000)
    
    while is_prime(var)==False:
        
        var=random.randint(1000,5000)
        
    return var

def generate_p_and_q():
    
    p,q=generate_prime(), generate_prime()
    
    while p==q:
        
        q=generate_prime()
        
    return p,q

def find_e(phi_n):
    
    #e has to be a number between 2 and phi_n such that the greatest common divisor between e and phi_n is 1.
    
    e=random.randint(3,phi_n-1)
    
    while math.gcd(e,phi_n)!=1:
        
        e=random.randint(3,phi_n-1)
        
    return e

def find_d(e,phi_n):
    
    for i in range(3,phi_n):
        
        # d has to be number between 2 and phi_n such that e*d is congruent to 1 mod phi_n.
        
        if (e*i)%phi_n==1:
            
            return i
        
    #this line will never run but it exists for the sole purpose of finding errors in the code.
        
    raise ValueError("d does not exist")

def main():
    
    message=str(input("enter a message: "))
    
    print(f"Original message: {message}")
    
    p,q=generate_p_and_q()
    
    n=p*q
    
    phi_n=(p-1)*(q-1)
    
    e=find_e(phi_n)

    d=find_d(e,phi_n)
    
    #convert the input string into a list with the corresponding ASCII values so that it can be encrypted.
    
    lst_message=[ord(ch) for ch in message]
    
    #the pow function raises the first argument to the power of the second argument and mods the result by the third argument.
    
    #these are the same steps we need to encrypt the message in RSA.
    
    encrypted_message=[pow(elem,e,n) for elem in lst_message]
    
    encrypted_message_str="".join(str(elem) for elem in encrypted_message)
    
    print(f"The message encrypted by RSA encryption is: {encrypted_message_str}")
    
    #decryption is the same as encryption but e is now replaced with d in the pow function.
    
    decrypted_message=[pow(elem,d,n) for elem in encrypted_message]
    
    #converting each decrypted ASCII value back into a character and then joining the characters together to return the original string.
    
    decrypted_message="".join(chr(elem) for elem in decrypted_message)
    
    print(f"The message decrypted by the RSA algorithm is: {decrypted_message}")
    
    info=str(input("Do you wish to view the sensitive key information? {Y/N} "))
    
    if info=="Y" or info=="y":
        
        print(f"p: {p}")
        
        print(f"q: {q}")
        
        print(f"n: {n}")
        
        print(f"phi_n: {phi_n}")
        
        print(f"e: {e}")
        
        print(f"d: {d}")
        
    else:
        
        print("Have a good day")
        
main()
    
