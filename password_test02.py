# Python program to check validation of password
# Module of regular expression is used with search()
# password = input("fgdg:")
# flag = 0
# while True:
#     if (len(password)<=8):
#         flag = -1
#         break
#     elif not re.search("[a-z]", password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]" , password):
#         flag = -1
#         break
#     elif re.search("\s" , password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break

# if flag == -1:
#     print("Not a Valid Password ")
    

import re
import hashlib
import secrets
import json


while True:
 
 username = input("entrez un nouveau username :")
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
 salt = secrets.token_hex(10)

 password = input("Enter your password: ")

 hash_object = hashlib.sha256((password + salt).encode())
 print(hash_object.hexdigest())

 SSID = username
 PSK = hash_object.hexdigest()
 
 donnees = {"user": SSID, "mdp": PSK}
 with open("data.json", "r") as f:
        test = json.load(f)

 test.append(donnees)

 with open ("data.json", "w") as f:
       json.dump(test, f, indent=4)

 mdp = input ("entrez un mot de passe : " )
    
 while (mdp)==False :
  print ("Erreur dans le mot de passe" )
  mdp = input ("entrez un nouveau mot de passe : " )
    
#Si toutes les conditions sont bonnes :
 else :
  mdp2 = input ("répetez le mot de passe : " )
  while mdp != mdp2 : 
   print ("mot de passe incorrect" ) 
   mdp2 = input ("mot de passe non identique réesseyer : " )
  else :
   print ("Mot de passe correct. Bravo !" )

# N = 10
# Sum = 0
  
# # This loop will run forever 
# while True: 
#     Sum += N 
#     N -= 1
      
#     # the below condition will tell 
#     # the loop to stop 
#     if N == 0: 
#         break
          
# print(f"Sum of First 10 Numbers is {Sum}")