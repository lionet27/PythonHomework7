import model 
    
import view 

def actionChoice():
    n=input('Введите номер действия, которое вы хотите сделать:1-вывод данных, 2-добавление человека в справочник: ')
    if n=='1':
        m=input('Введите номер файла, которое вы хотите просмотреть:1 или 2: ')
        if m=='1':
            view.txtRead('1.txt')
        elif m=='2':
            view.txtRead('2.txt')
        else:
            print('Неправильно ввели номер.')
    elif n=='2':
        human=[]
        human=view.addPerson(human)
        model.txt1Write(human)
        model.txt2Write(human)
    else:
        print('Неправильно ввели номер.') 