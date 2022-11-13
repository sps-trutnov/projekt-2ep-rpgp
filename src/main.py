# --- Projekt Role-playing parodie Vojtěcha Nepimacha a Pavla Kotka ---
import sys
import pygame as pg
from Screens import *
from dev_tools import *
from items import *
from campaign import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

resolution = 1200, 900

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(resolution)
pg.display.set_caption("Generic Game")

on__screen.active_screen = main_menu
on__screen.active_table = "Close"

dev_shortcut = None
devmode = False

click_acc = True
bt_acc = True
tt_acc = True
pt_acc = True

while True:
    # Získání infa o akcích
    events = pg.event.get()
    pressed = pg.key.get_pressed()
    m_pressed = [pg.mouse.get_pressed()[0], pg.mouse.get_pressed()[1], pg.mouse.get_pressed()[2]]
    
    # Možnosti vypnutí
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    if on__screen.active_screen == "Exit":
        pg.quit()
        sys.exit()
    
    # Vykreslení obrazovky/tabulky
    screen.blit(on__screen.active_screen.background,(0,0))
    if not on__screen.active_screen.objects == None:
        for object in on__screen.active_screen.objects:
            object.blit_self(screen)
    if not on__screen.active_table == "Close":
        table = pg.Surface(on__screen.active_table.size)
        table.set_alpha(on__screen.active_table.alpha)
        screen.blit(table, (on__screen.active_table.position))
    
    # Vykreslování itemů v obchodě
    if not item_class.weapons == []:
        for weapon in item_class.weapons:
            weapon.draw(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", screen, on__screen)
    if not item_class.armors == []:
        for armor in item_class.armors:
            armor.draw(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", screen, on__screen)
    if not item_class.misc_items == []:
        for misc_item in item_class.misc_items:
            misc_item.draw(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", screen, on__screen)
            
    # Vykreslování věcí v kampani
    counter.blit_self(screen, on__screen)
    
    # Zrušení multi-klikání
    if not devmode:
        if click_acc and m_pressed[0]:
            click_acc = False
        elif not click_acc and m_pressed[0]:
            m_pressed[0] = False
        elif not click_acc and not m_pressed[0]:
            click_acc = True
     
     
    # BITVA
    if on__screen.battle:
        while on__screen.battle:
            events = pg.event.get()
            m_pressed = [pg.mouse.get_pressed()[0], pg.mouse.get_pressed()[1], pg.mouse.get_pressed()[2]]
            
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
        
            screen.fill((255,255,255))
        
            pg.display.update()
            clock.tick(144)
    
    ### Vykreslení tlačítek + kontrola stisku tlačítek ###
    if not on__screen.active_screen == "Exit" or not on__screen.active_screen == None:
        for button in button_class.buttons:
            button.blit_self(screen, on__screen)
            if on__screen.button_activity:
                button.check(m_pressed, on__screen)
                
    if not on__screen.button_activity:
        on__screen.button_activity = not on__screen.button_activity
        
    if not on__screen.active_screen == "Exit":
        for t in on__screen.active_screen.texts:
            t.blit_self(screen)
        if not on__screen.active_table == "Close":
            for t in on__screen.active_table.texts:
                t.blit_self(screen)
    
    ### DEVELOPER MODE ###
    if pressed[pg.K_d]:
        dev_shortcut = 1
    
    if pressed[pg.K_e] and dev_shortcut == 1:
        dev_shortcut = 2
    
    if pressed[pg.K_v] and dev_shortcut == 2:
        if devmode == False:
            devmode = True
            dev_shortcut = None
        else:
            devmode = False
            dev_shortcut = None

    ### DEVELOPER MODE ###
    if devmode:
        ### TEXTURE PREVIEW TOOL ###
        # Zde se do podprogramu zadá cesta textury, kterou chceme vidět ve hře
        pt.get_texture(DATA_ROOT + "/data/textures/weapons/warrior/type_2/5.png")
        # Zde se textury zobrazují
        pt.render_preview(screen, resolution)
        
        # Aktivace a deaktivate Texture Preview Toolu
        if pressed[pg.K_r] and pt_acc:
            pt.on_off()
            pt_acc = False
            
        elif pressed[pg.K_r] and not pt_acc:
            pass
        else:
            pt_acc = True
        
        ### BUTTON TOOL ###
        # Práce Button_tool -> třeba aktivovat
        bt.find(m_pressed)
        bt.calculate()
        
        # Vypisování výsledků Button_tool
        bt.list(pressed, screen)
        
        # Aktivace/Deaktivace Button_tool
        if pressed[pg.K_s] and bt_acc:
            bt.on_off()
            bt_acc = False
        elif pressed[pg.K_s] and not bt_acc:
            pass
        else:
            bt_acc = True
            
        ### TEXT TOOL ###
        # Práce Text_tool -> třeba aktivovat
        tt.find(m_pressed)
        tt.change(pressed)
        
        # Vypisování a vykreslení výsledků Text_tool
        tt.show("You own: 200 G.olds", pressed, screen)
        
        # Aktivace/Deaktivace Text_tool
        if pressed[pg.K_t] and tt_acc:
            tt.on_off()
            tt_acc = False
        elif pressed[pg.K_t] and not tt_acc:
            pass
        else:
            tt_acc = True
    
    pg.display.update()
    clock.tick(144)
    