botnum=1                     #Номер бота
i=1                          #Флаг на окончание хода
numofbots=64                 #Число ботов
def mainfunc():
    global botnum,i           #Объявление глобальных переменных
    if botnum==1:
        gen_food()           #Генерация еды
    act=genome//8            #Тут надо вынуть цифру из массива bots и преобразовать к человеческому блен виду чтобы сунуть в switcher
    switcher = {             #Словарь который послужит переключателем команд
            1: grab,         #Тут написаны имена мини-функций
            2: attack,
            3: turn,
            4: move,
            5: look,
    }
    switcher[act]()          #По ключу переходит к функции, аргументы функции задаются в ()
    if i==0 :                 #Смена хода
        botnum+=1
    if numofbots==8 :
        mutate()            #мутатор


    mainfunc()


mainfunc()
#Нужно еще: переменная для залипания ботов
