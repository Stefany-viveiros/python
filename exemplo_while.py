i = 1
#Enquanto i for menor que 6

while i < 6:
    print(i)
    i = i + 1 #Somando i + 1


#Pare o cógigo quando i valer 3
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i = i + 1 

#break para o looping
#continue pula para o próximo looping

i = 1
while i < 9:
    i = i + 1
    if i == 8:
        continue
    print(i)