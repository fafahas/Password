#conditions
#mdp = input ("entrez un nouveau mot de passe : ")
#def test (mdp) :
 #satisfaisant = True
#Notre mot de passe doit contenir au moins 4 caractère, sinon on note un message qui nous dit qu'il est trop court.  
 #if not len (mdp) > 4 :
  #print ("Votre mot de Passe est trop Court !" )
  #satisfaisant = False
#Maintenant le mot de passe doit contenir moins de 10 caractère donc grace à la fonction len, on dit que le mot de passe
#Doit contenir moins de 10 caractère, sinon le mot de passe est trop long.
 #if not len (mdp) < 10 :
  #print ("Votre mot de Passe est trop long !" )
  #satisfaisant = False
 
#if sum(1 for c in mdp if c.isalpha()) :
    #alpha_present = True
#else:
    #print ("Une minuscule au moins")
     
#if sum(1 for c in mdp if c.isupper()) :
    #maj_presente = True
#else:
    #print ("Une majuscule au moins")
 
#if sum(1 for c in mdp if c.isdigit()) :
    #digit_present = True
#else:
    #print ("Un chiffre au moins")
      
#Fonction principale
#mdp = input ("entrez un mot de passe : " )
    
#while test(mdp)==False :
 #print ("Erreur dans le mot de passe" )
 #mdp = input ("entrez un nouveau mot de passe : " )
    
#Si toutes les conditions sont bonnes :
#else :
 #mdp2 = input ("répetez le mot de passe : " )
 #while mdp != mdp2 : 
  #print ("mot de passe incorrect" ) 
  #mdp2 = input ("mot de passe non identique réesseyer : " )
 #else :
  #print ("Mot de passe correct. Bravo !" )
