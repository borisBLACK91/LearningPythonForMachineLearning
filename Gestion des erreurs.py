#coding:utf-8

#how to manage errors


"""
numTel = input("Quel est votre numero de telephone : ")
numTel = int(numTel)
print("le numero saisi est le ", numTel)
"""


numTel = input("Quel est votre numero de telephone : ")
try:
	numTel = int(numTel)
except:
	print("le numero n'est pas valide!") #error message in case of issue
else:	
	print("le numero saisi est le ", numTel) #action to do if correct numero inserted
finally: 
	print("FERMETURE DU PROGRAMME.......") #line always executed
