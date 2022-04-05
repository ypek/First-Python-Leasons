perguntas = ["Telefonou para a vítima? 1/Sim ou 0/Não: ",
"Esteve no local do crime? 1/Sim ou 0/Não: ",
"Mora perto da vítima? 1/Sim ou 0/Não: ",
"Devia para a vítima? 1/Sim ou 0/Não: ",
"Já trabalhou com a vítima? 1/Sim ou 0/Não: "]
res = []
soma_respostas = 0
for i in range(len(perguntas)):
    print(perguntas[i]) 

res.append(input()) # colocando as responstas na listinha ^^

soma_respostas += int(res[i]) 
status = ["Inocente","Suspeita","Cúmplice","Cúmplice","Assassino"]

if soma_respostas < 2:
    print(status[0]) 

else:
    print(status[soma_respostas-1]) 
