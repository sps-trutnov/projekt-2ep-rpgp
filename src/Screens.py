import sys
import pygame as pg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

#obrazovky
class screen():
    def __init__(self, name, background, l_buttons, t_buttons, text):
        self.name = name
        self.background = pg.transform.scale(background, (1200,900))
        self.l_buttons = l_buttons
        self.t_buttons = t_buttons
        if not text == []:
            self.text = text

class table():
    def __init__(self, name, l_buttons, t_buttons, text):
        self.name = name
        self.position = [100,100]
        self.size = [1000,700]
        self.colour = (30,30,30)
        self.alpha = 220
        self.l_buttons = l_buttons
        self.t_buttons = t_buttons
        if not text == []:
            self.text = text

class link_button():
    def __init__(self, position, width, height, link, draw, text, texture):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
        self.draw = draw
        self.colour = (150,150,150)
        if not text == []:
            self.text = text
        else:
            self.text = True
        if not texture == None:
            self.texture = pg.transform.scale(texture, (width, height))
        else:
            self.texture = None
        
    def check(self, m_pressed):
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0]:
            if self.link == "Exit":
                return "Exit"
            else:
                return self.change_screen(screens)
        else:
            pass
        
    def change_screen(self, screens):
        for screen in screens:
            if self.link == screen.name:
                return screen
            else:
                pass
            
class table_button():
    def __init__(self, position, width, height, link, draw, text, texture):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
        self.colour = (200,200,200)
        self.draw = draw
        if not text == []:
            self.text = text
        else:
            self.text = True
        if not texture == None:
            self.texture = pg.transform.scale(texture, (width, height))
        else:
            self.texture = None
        
        
    def check(self, m_pressed):
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0]:
            if self.link == "Close":
                return "Close"
            else:
                return self.open_table(tables)
        else:
            pass
        
    def open_table(self, tabls):
        for table in tables:
            if self.link == table.name:
                return table
            else:
                pass
        
# Tlačítka pro změnu obrazovky
exit_lb = link_button((490,760), 215, 85, "Exit", False, [], None)
new_game_lb = link_button((150,675), 900, 75, "Game menu", True, [], None)
main_menu_lb = link_button((30,30), 75, 75, "Main menu", True, [], None)
shop_lb = link_button((950, 600), 100, 100, "Shop", False, [], pg.image.load(DATA_ROOT + "/data/textures/icons/shop_icon.png"))
game_menu_lb = link_button((30,30), 75, 75, "Game menu", True, [], None)

link_buttons = [

                ]

# Tlačítka tabulek
new_game_tb = table_button((75,485), 445, 85, "New game table", False, [], None)
settings_tb = table_button((75,625),445,85,"Settings table", False, [], None)
credits_tb = table_button((680,625),445,85,"Credits table", False, [], None)

t_close = table_button((1000,125), 75, 75, "Close", False, [], pg.image.load(DATA_ROOT + "/data/textures/icons/close_icon.png"))

table_buttons = [
            new_game_tb,
            settings_tb,
            credits_tb,
            t_close
                ]

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"), [exit_lb], [new_game_tb, settings_tb, credits_tb], [])
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"), [main_menu_lb, shop_lb], [], [])
shop = screen("Shop", pg.image.load(DATA_ROOT + "/data/textures/screens/shop.png"), [game_menu_lb], [], [])

screens = [
            main_menu,
            game_menu,
            shop
            ]

# Tabulky
new_game_table = table("New game table", [new_game_lb], [t_close], [])
settings_table = table("Settings table", [], [t_close], [])
credits_table = table("Credits table", [], [t_close], [])

tables = [
            new_game_table,
            settings_table,
            credits_table
            ]