#coding:utf-8


"""
file accessing mode: 
		reading - r
		writing - w
		append(write after) - a 
"""
"""
file = open("rep_fichiers/tfile.txt", "r")
content = file.read() #in this way we take al file content inside our variable content
print(content)
file.close()
"""

"""
file = open("rep_fichiers/tfile.txt", "r")
#content = file.read() #in this way we take al file content inside our variable content
line = file.readline()  #read on line of the file
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)

file.close()
"""

"""
with open("rep_fichiers/tfile.txt", "w") as file:
	numb = 758
	file.write(str(numb))
	file.write(str("\nI am  the learner"))

with open("rep_fichiers/toto.txt", "w") as file:
	numb = 18
	file.write(str(numb))
	file.write(str("\nI am  the learner"))"""

with open("rep_fichiers/toto.txt", "a") as file:
	file.write(str("\nnow I append another text :) "))