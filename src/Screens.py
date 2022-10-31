import sys
import pygame as pg
from text import *
from data import *
from items import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

class on_screen():
    def __init__(self):
        self.active_screen = None
        self.active_table = "Close"
        self.button_activity = True
        self.battle = False


on__screen = on_screen()


buttons = []

class screen():
    def __init__(self, name, background, buttons, texts, objects):
        self.name = name
        self.background = pg.transform.scale(background, (1200,900))
        self.buttons = []
        for button in buttons:
            for place in button.belonging:
                if place == self.name:
                    self.buttons.append(button)
        if not text == []:
            self.texts = texts
        self.objects = objects

class table():
    def __init__(self, name, buttons, texts):
        self.name = name
        self.position = [100,100]
        self.size = [1000,700]
        self.colour = (30,30,30)
        self.alpha = 220
        self.buttons = []
        for button in buttons:
            for place in button.belonging:
                if place == self.name:
                    self.buttons.append(button)
        if not text == []:
            self.texts = texts

class Button_cl():
    def __init__(self, buttons):
        self.buttons = buttons

class Button():
    def __init__(self, belonging, position, colour, width, height, tasks, draw, texture, scale, condition):
        self.belonging = belonging
        self.position = position
        self.width = width
        self.height = height
        self.tasks = tasks
        self.colour = colour
        self.alpha = 180
        self.draw = draw
        if not texture == None:
            if scale:
                self.texture = pg.transform.scale(texture, (width, height))
            else:
                self.texture = texture
        else:
            self.texture = None
        if not condition == None:
            self.condition = condition
        else:
            self.condition = True
            
    def check(self, m_pressed, on__screen):
        if not on__screen.active_screen == "Exit":
            if not on__screen.active_table == "Close":
                if on__screen.active_table.name in self.belonging:
                    if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0] and self.condition:
                        on__screen.button_activity = False
                        self.work()
            elif on__screen.active_screen.name in self.belonging:
                if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0] and self.condition:
                   on__screen.button_activity = False
                   self.work()
            
    def blit_self(self, screen, on__screen):
        if not on__screen.active_screen == "Exit":
            if not on__screen.active_table == "Close":
                if on__screen.active_table.name in self.belonging:
                    if self.draw:
                        button_sf = pg.Surface((self.width, self.height), pg.SRCALPHA)
                        pg.draw.circle(button_sf, self.colour, ((self.position[0]),(self.position[1])), width/2)
                        screen.blit(button_sf, (self.position))
                    if self.texture == None:
                        pass
                    else:
                        screen.blit(self.texture, (self.position))
            elif on__screen.active_screen.name in self.belonging:
                if self.draw:
                    offset = self.width/3
                    backgr_size = self.width + offset
                    button_sf = pg.Surface((backgr_size, backgr_size), pg.SRCALPHA)
                    pg.draw.circle(button_sf, self.colour, ((backgr_size/2),(backgr_size/2)), backgr_size/2)
                    screen.blit(button_sf, ((self.position[0] - offset/2),(self.position[1] - offset/2)))
                if self.texture == None:
                    pass
                else:
                    screen.blit(self.texture, (self.position))
        
    def work(self):
        for task in self.tasks:
            if task[0] == "change_role":
                self.change_role(task[1], player)
            if task[0] == "change_screen":
                self.change_screen(task[1], task[2], on__screen)
            if task[0] == "change_table":
                self.change_table(task[1], task[2], on__screen)
            if task[0] == "change_item":
                self.change_item(task[1], task[2])
            if task[0] == "create_items":
                init_items(weapon_class.weapons, player.role)
                shop_b_init(weapon_class.weapons, Button_class.buttons)
        
    def change_screen(self, screens, new_screen, on_screen):
        if new_screen == "Exit":
            on_screen.active_screen = "Exit"
        else:
            for screen in screens:
                if screen.name == new_screen:
                    on_screen.active_screen = screen
                    on_screen.active_table = "Close"
                
    def change_table(self, tables, new_table, on_screen):
        if new_table == "Close":
            on_screen.active_table = "Close"
        else:
            for table in tables:
                if table.name == new_table:
                    on_screen.active_table = table
                    
    def change_item(self, new_item, items):
        for item in items:
            item.shown = False
        new_item.shown = True
        
    def change_role(self, role, player):
        player.role = role
        
class blit_object():
    def __init__(self, position, texture, scale, width, height):
        self.texture = texture
        self.position = position
        if scale:
            self.texture = pg.transform.scale(texture, (width, height))
        
    def blit_self(self, screen):
        screen.blit(self.texture, self.position)
        
def shop_b_init(weapons, buttons):
    textures = []
    for weapon in weapons:
        textures.append(weapon.texture)
        
    sw = Button(["Weapon board"], (840,70), None, 105,105, [["change_item", weapons[0], weapons]], False, textures[0], True, None)
    Button_class.buttons.append(sw)
    w1t1 = Button(["Weapon board"], (685,200), None, 105,105, [["change_item", weapons[1], weapons]], False, textures[1], True, None)
    Button_class.buttons.append(w1t1)
    w2t1 = Button(["Weapon board"], (685,330), None, 105,105, [["change_item", weapons[2], weapons]], False, textures[2], True, None)
    Button_class.buttons.append(w2t1)
    w3t1 = Button(["Weapon board"], (685,460), None, 105,105, [["change_item", weapons[3], weapons]], False, textures[3], True, None)
    Button_class.buttons.append(w3t1)
    w4t1 = Button(["Weapon board"], (685,590), None, 105,105, [["change_item", weapons[4], weapons]], False, textures[4], True, None)
    Button_class.buttons.append(w4t1)
    w5t1 = Button(["Weapon board"], (685,720), None, 105,105, [["change_item", weapons[5], weapons]], False, textures[5], True, None)
    Button_class.buttons.append(w5t1)

    w1t2 = Button(["Weapon board"], (840,200), None, 105,105, [["change_item", weapons[6], weapons]], False, textures[6], True, None)
    Button_class.buttons.append(w1t2)
    w2t2 = Button(["Weapon board"], (840,330), None, 105,105, [["change_item", weapons[7], weapons]], False, textures[7], True, None)
    Button_class.buttons.append(w2t2)
    w3t2 = Button(["Weapon board"], (840,460), None, 105,105, [["change_item", weapons[8], weapons]], False, textures[8], True, None)
    Button_class.buttons.append(w3t2)
    w4t2 = Button(["Weapon board"], (840,590), None, 105,105, [["change_item", weapons[9], weapons]], False, textures[9], True, None)
    Button_class.buttons.append(w4t2)
    w5t2 = Button(["Weapon board"], (840,720), None, 105,105, [["change_item", weapons[10], weapons]], False, textures[10], True, None)
    Button_class.buttons.append(w5t2)
    
    w1t3 = Button(["Weapon board"], (995,200), None, 105,105, [["change_item", weapons[11], weapons]], False, textures[11], True, None)
    Button_class.buttons.append(w1t3)
    w2t3 = Button(["Weapon board"], (995,330), None, 105,105, [["change_item", weapons[12], weapons]], False, textures[12], True, None)
    Button_class.buttons.append(w2t3)
    w3t3 = Button(["Weapon board"], (995,460), None, 105,105, [["change_item", weapons[13], weapons]], False, textures[13], True, None)
    Button_class.buttons.append(w3t3)
    w4t3 = Button(["Weapon board"], (995,590), None, 105,105, [["change_item", weapons[14], weapons]], False, textures[14], True, None)
    Button_class.buttons.append(w4t3)
    w5t3 = Button(["Weapon board"], (995,720), None, 105,105, [["change_item", weapons[15], weapons]], False, textures[15], True, None)
    Button_class.buttons.append(w5t3)
    
    
# Objekty na vykreslení
weapon_tree = blit_object((0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/weapon_tree.png"), True, 1200, 900)
armour_tree = blit_object((0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/general_item_tree.png"), True, 1200, 900)
item_tree = blit_object((0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/general_item_tree.png"), True, 1200, 900)

# Tlačítka pro změnu obrazovky
exit_b = Button(["Main menu"], (490,760), None, 215, 85, [["change_screen", [], "Exit"]], False, None, False, None)

warrior_class_b = Button(["New game table"], (230, 400), None, 180, 220, [["change_role", "warrior"], ["change_screen", [], "Game menu"], ["create_items"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/warrior_class_icon.png"), True, None)
ranger_class_b = Button(["New game table"], (510, 400), None, 180, 220, [["change_role", "ranger"], ["change_screen", [], "Game menu"], ["create_items"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/ranger_class_icon.png"), True, None)
mage_class_b = Button(["New game table"], (790, 400), None, 180, 220, [["change_role", "mage"], ["change_screen", [], "Game menu"], ["create_items"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/mage_class_icon.png"), True, None)

main_menu_b = Button(["Game menu"], (30,30), (30,30,30,180), 64, 64, [["change_screen", [], "Main menu"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
shop_b = Button(["Game menu"], (940, 550), (30,30,30,180), 100, 100, [["change_screen", [], "Shop"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/shop_icon.png"), True, None)
profile_b = Button(["Game menu"], (95,550), (30,30,30,180), 100, 100, [["change_screen", [], "Profile"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/profile_icon.png"),True, None)
campaign_b = Button(["Game menu"], (550,400), (30,30,30,180), 100, 100, [["change_screen", [], "Campaign"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/campaign_icon.png"), True, None)
game_menu_b = Button(["Shop", "Profile", "Campaign"], (30,30), (30,30,30,180), 64, 64, [["change_screen", [], "Game menu"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)

shop_back_b = Button(["Weapon board", "Armor board", "Item board"], (30,30), (30,30,30,180), 64, 64, [["change_screen", [], "Shop"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
weapon_board_b = Button(["Shop"], (731,245), (255,0,0), 221, 267, [["change_screen", [], "Weapon board"]], False, None, False, None)
armor_board_b = Button(["Shop"], (239,240), (255,0,0), 232, 126, [["change_screen", [], "Armor board"]], False, None, False, None)
item_board_b = Button(["Shop"], (248,395), (255,0,0), 224, 105, [["change_screen", [], "Item board"]], False, None, False, None)

# Tlačítka tabulek
new_game_b = Button(["Main menu"], (75,485), None, 445, 85, [["change_table", [], "New game table"]], False, None, False, None)
settings_b = Button(["Main menu"], (75,625), None, 445,85, [["change_table", [], "Settings table"]], False, None, False, None)
credits_b = Button(["Main menu"], (680,625), None, 445,85, [["change_table", [], "Credits table"]], False, None, False, None)

close_b = Button(["New game table", "Settings table", "Credits table"], (1000,125), None, 64, 64, [["change_table", [], "Close"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/close_icon.png"), False, None)


buttons = [
            exit_b,
            main_menu_b,
            shop_b,
            profile_b,
            game_menu_b,
            shop_back_b,
            campaign_b,
            weapon_board_b,
            armor_board_b,
            item_board_b,
            new_game_b,
            settings_b,
            credits_b,
            close_b,
            warrior_class_b,
            ranger_class_b,
            mage_class_b,
            ]

# Pavlovo Objektová hovadina
Button_class = Button_cl(buttons)

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"), Button_class.buttons, [], None)
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"), Button_class.buttons, [], None)
shop = screen("Shop", pg.image.load(DATA_ROOT + "/data/textures/screens/shop.png"), Button_class.buttons, [], None)
profile = screen("Profile", pg.image.load(DATA_ROOT + "/data/textures/screens/profile.png"), Button_class.buttons, [], None)
campaign = screen("Campaign", pg.image.load(DATA_ROOT + "/data/textures/screens/campaign.png"), Button_class.buttons, [], None)

# Podobrazovky obchodu
weapon_board = screen("Weapon board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), Button_class.buttons, [], [weapon_tree])
armor_board = screen("Armor board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), Button_class.buttons, [], [armour_tree])
item_board = screen("Item board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), Button_class.buttons, [], [item_tree])

screens = [
            main_menu,
            game_menu,
            shop,
            weapon_board,
            armor_board,
            item_board,
            profile,
            campaign,
            ]

# Tabulky
new_game_table = table("New game table", buttons, texts_new_game)
settings_table = table("Settings table", buttons, texts_settings)
credits_table = table("Credits table", buttons, texts_credits)

tables = [
            new_game_table,
            settings_table,
            credits_table
            ]


# Speciální vyjímky pro přepínací čudlíky
for button in buttons:
    for task in button.tasks:
        if task[0] == "change_screen":
            task[1] = screens
        if task[0] == "change_table":
            task[1] = tables
        