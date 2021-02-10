import pygame
from pygame.locals import *
import pygame_gui
import time


pygame.init()


def border(string):
    return string[string.find('(') + 1: string.rfind(')')]
"""
Извлекает значение внутри скобок в строке
string - исходная строка (обязана содержать хотя бы одну открывающую и закрывающую скобку в нужном порядке)
"""


class UIElement:
    typ = 'None'
    name = ''
    options = []

    def __init__(self, typ, name, options=[]):
        self.typ = typ
        self.name = name
        self.options = options.copy()

    def get_gui(self, rect, manager):  # Возвращает объект GUI
        if self.typ == 'text':
            answ = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=rect,
                                                                          manager=manager)
            answ.set_text(self.name)
            return answ
        if self.typ == 'list':
            return pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(options_list=self.options.copy(),
                                                                        starting_option=self.name,
                                                                        relative_rect=rect,
                                                                        manager=manager)
"""
Класс для временного хранения результатов расшифровки входной строки программы.
"""


def decode_uis(string):
    answ = []
    arr = string.split(',')
    for com in arr:
        if com.replace(' ', '')[:4] == 'text':
            s = border(com).split()
            answ.append(UIElement('text', s[0]))
        if com.replace(' ', '')[:4] == 'list':
            s = border(com).split()
            answ.append(UIElement('list', s[0], s[1:]))
    return answ
"""
Функция для расшифровки входной строки (ввода) программы
"""


class Drawer:
    def __init__(self, params=''):
        self.UIs = decode_uis(params)
        self.scr = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('GRIT-Z')  # Generator of Randomized Instances of Tasks - Zero version
        self.manager = pygame_gui.UIManager([800, 600])
        self.generate_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 20), (800-30 - 300, 50)),
                                                            text='Generate',
                                                            manager=self.manager)
        self.reset(params)
        self.tm = time.monotonic()

    def reset(self, params):  # Пересоздаёт меню с другими настройками (ввод)
        self.UIs = decode_uis(params)
        self.guis = []
        for i, ui in enumerate(self.UIs):
            self.guis.append(ui.get_gui(pygame.Rect((20, 20 + i * 30), (250, 20)),
                                        self.manager))

    def get_values(self):  # Возвращает массив значений элементов интерфейса
        answ = []
        for ui in self.guis:
            try:
                answ.append(ui.selected_option)
            except:
                try:
                    answ.append(ui.get_text())
                except:
                    print('Visualizer ERROR!\nWrong UI type')
        return answ

    def operate_events(self):  # Обрабатывает события пользователя.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'stop'
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.generate_button:
                        return ' '.join(self.get_values())
            self.manager.process_events(event)

    def tick(self):  # Функция для обновления. Должна вызываться каждый проход основного цикла программы.
        TM = time.monotonic()
        delta = TM - self.tm
        self.tm = TM
        res = self.operate_events()
        self.manager.update(delta)
        self.scr.fill([120] * 3)
        self.manager.draw_ui(self.scr)
        pygame.display.update()
        return res
"""
Основной класс программы
"""
