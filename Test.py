from Visualiser import *

# Объявление художника
drw = Drawer('list(Testlist name1 name2), text(test), list(Testlist name1 name2), text(test), list(Testlist name1 name2), text(test), list(Testlist name1 name2), text(test), text(grtz)')


kg = True # Условие основного цикла программы


while kg: # ОЦП (Основной Цикл Программы)
    res = drw.tick() # Обновление интерфейса и приём команд пользователя. Для пересоздания интерфейса используется функция reset("новый_ввод")

    # Обработка вывода интерфейса
    if res == 'stop':
        kg = False
    elif res != None:
        print('Generation parameters -', res)

# Выход из программы
pygame.quit()
