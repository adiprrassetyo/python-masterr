# Belajar Break

while True:
    data = input("Data : ")
    if data == "x":
        break 
    print(data)
    
    
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print(f'Huruf saat ini: {huruf}')
    
for i in range (0,10):
    for j in range (0,10):
        if j>i:
            print()
            break
        else:
            print("*",end="")