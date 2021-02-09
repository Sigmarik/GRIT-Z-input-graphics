from Visualiser import *

drw = Drawer('list(Testlist name1 name2), text(test), list(Testlist name1 name2), text(test), list(Testlist name1 name2), text(test), list(Testlist name1 name2), text(test), text(grtz)')
kg = True

while kg:
    res = drw.tick()
    if res == 'stop':
        kg = False
    elif res != None:
        print('Generation parameters -', res)
pygame.quit()
