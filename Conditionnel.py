#coding:utf-8

#learning conditional operations:
""" ==, !=, >, <, >=, <=

and, or 
in , not in 

use of if, elif, else
"""

login = "pirot"
mot_de_passe = "pwd123"
print("..................INTERFACE DE CONNEXION...................")

ID_LOGIN = input("entre le login : ")
PWD_USER = input("entre le mot de passe : ")

"""
if PWD_USER == mot_de_passe : 
	print("bienvenu ", login)
else :
	print("mot de passe erroné")"""


"""if PWD_USER == mot_de_passe and login == ID_LOGIN : 
	print("bienvenu ", login)
else :
	print("mot de passe erroné")"""


if PWD_USER == mot_de_passe and login == ID_LOGIN : 
	print("bienvenu ", login)
elif PWD_USER == mot_de_passe and login != ID_LOGIN :
	print("bienvenu ", login)
else :
	print("mot de passe erroné")