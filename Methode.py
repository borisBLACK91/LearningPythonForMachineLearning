#coding:utf-8

"""
 types the mthodes : 
 -standard : fonctions sur instances (mot clé self)
 -statiques : fonctions indépendantes mais attachées a une classe
 -methode de classes: fonction sur une classe (mot clé cls)
"""

#standard 
"""
class World: 
	def __init__(self, pays, continent):
		self.pays = pays
		self.continent = continent

	def caracteristique(self, temperature):
		print("le {} est un pays {}".format(self.pays, temperature))


myVar = World("Cameroon", "Afrique")
myVar.caracteristique("chaud")

"""


#methodes de classes: 

class World: 

	food_prefere = "koki"

	def __init__(self, pays, continent):
		self.pays = pays
		self.continent = continent

	def caracteristique(self, temperature):
		print("le {} est un pays {}".format(self.pays, temperature))

	def change_food_prefere(cls, new_food_pref): 
		World.food_prefere = new_food_pref

	change_food_prefere = classmethod(change_food_prefere)


myVar = World("Cameruon", "Afrique")
myVar.caracteristique("chaud")

print("nourriture prefere des camerounais est le : {}" .format(World.food_prefere))

World.change_food_prefere("Ndolé")

print("les camerounais prefere desormais le : {}" .format(World.food_prefere))