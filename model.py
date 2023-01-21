
def txt1Write(people):
    with open("1.txt", "a") as f:
        for i in range(0,len(people)):
            for j in range (0,len(people[i])):
                f.write(f'{people[i][j]}\n')
            f.write('-------------\n')
    

def txt2Write(people):
    with open("2.txt", "a") as f:
        for i in range(0,len(people)):
            for j in range (0,len(people[i])-1):
                f.write(f'{people[i][j]},')
            f.write(f'{people[i][3]}\n')
    

    







