def txtRead(path):
    with open(path, "r") as f:
        print(f.read())

def addPerson(phoneBook):
    phoneBook.append(list(input('Введите через пробел: 1)фамилию 2)имя 3)номер телефона 4)описание: ').split()))
  
    return phoneBook