import re
import hashlib
import secrets

print("Bienvenue ! les caracteres speciaux sont @/;")
password = input("entrez un nouveau mot de passe :")
if (len(password)<=8):
 print("1")
elif not re.search("[a-z]", password):
 print("2")
elif not re.search("[A-Z]", password):
 print("3")
elif not re.search("[0-9]", password):
 print("4")
elif not re.search("[_@$]" , password):
 print("5")
# elif re.search("\s" , password):
#     print("les caractere < à 8")
else:
 print("Valid Password")

salt = secrets.token_hex(16)

password = input("Enter your password: ")

hash_object = hashlib.sha256((password + salt).encode())
print(hash_object.hexdigest())

N = 10
Sum = 0
  
# This loop will run forever 
while True: 
    Sum += N 
    N -= 1
      
    # the below condition will tell 
    # the loop to stop 
    if N == 0: 
        break
          
print(f"Sum of First 10 Numbers is {Sum}")


