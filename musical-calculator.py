import pygame
import sys
from pygame import mixer 
pygame.init()
mixer.init()
pygame.mixer.set_num_channels(8)

#music
button_click_sound1 = mixer.Sound("./audio/C4.wav")
button_click_sound1.set_volume(1)
button_click_sound2 = mixer.Sound("./audio/D4.wav")
button_click_sound2.set_volume(1)
button_click_sound3 = mixer.Sound("./audio/E4.wav")
button_click_sound3.set_volume(1)
button_click_sound4 = mixer.Sound("./audio/F4.wav")
button_click_sound4.set_volume(1)
button_click_sound5 = mixer.Sound("./audio/G4.wav")
button_click_sound5.set_volume(1)
button_click_sound6 = mixer.Sound("./audio/A5.wav")
button_click_sound6.set_volume(1)
button_click_sound7 = mixer.Sound("./audio/B5.wav")
button_click_sound7.set_volume(1)
button_click_sound8 = mixer.Sound("./audio/C5.wav")
button_click_sound8.set_volume(1)
button_click_sound9 = mixer.Sound("./audio/D5.wav")
button_click_sound9.set_volume(1)
button_click_sound0 = mixer.Sound("./audio/E5.wav")
button_click_sound0.set_volume(1)
button_click_soundplus = mixer.Sound("./audio/274775__ianstargem__simple-kick-drum.wav")
button_click_soundplus.set_volume(0.5)
button_click_soundmin = mixer.Sound("./audio/183150__ondrosik__hihat2.wav")
button_click_soundmin.set_volume(0.3)
button_click_sounddiv = mixer.Sound("./audio/102035__rytmenpinnen__hihatopen.wav")
button_click_sounddiv.set_volume(1)
button_click_soundmul = mixer.Sound("./audio/102034__rytmenpinnen__hhfootkick.wav")
button_click_soundmul.set_volume(1)

# Set up display
screen = pygame.display.set_mode((400, 600))
BGCOLOUR = (178, 190, 181)
white = (255, 255, 255)
black = (0, 0, 0)
resultscreenfont = pygame.font.SysFont('fixedsys', 30)
pygame.display.set_caption("Musical Calculator")

# Key to button mapping
key_to_button_map = {
    pygame.K_1: '1', pygame.K_KP1: '1',
    pygame.K_2: '2', pygame.K_KP2: '2',
    pygame.K_3: '3', pygame.K_KP3: '3',
    pygame.K_4: '4', pygame.K_KP4: '4',
    pygame.K_5: '5', pygame.K_KP5: '5',
    pygame.K_6: '6', pygame.K_KP6: '6',
    pygame.K_7: '7', pygame.K_KP7: '7',
    pygame.K_8: '8', pygame.K_KP8: '8',
    pygame.K_9: '9', pygame.K_KP9: '9',
    pygame.K_0: '0', pygame.K_KP0: '0',
    pygame.K_PLUS: '+', pygame.K_KP_PLUS: '+',
    pygame.K_MINUS: '-', pygame.K_KP_MINUS: '-',
    pygame.K_ASTERISK: '*', pygame.K_KP_MULTIPLY: '*',
    pygame.K_SLASH: '/', pygame.K_KP_DIVIDE: '/',
    pygame.K_RETURN: '=', pygame.K_KP_ENTER: '=',
    pygame.K_ESCAPE: 'AC', pygame.K_DELETE: 'AC',
    pygame.K_BACKSPACE: 'BACK'
}

# Button class
class Button:
    def __init__(self, x, y, width, height, text, colour=white, hovercolour=(138, 154, 91)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.colour = colour
        self.hovercolour = hovercolour
        self.text_surf = resultscreenfont.render(text, True, black)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect, border_radius=5)
        pygame.draw.rect(screen, black, self.rect, 2, border_radius=5)
        screen.blit(self.text_surf, self.text_rect)

    def isclicked(self, pos):
        return self.rect.collidepoint(pos)

# Create buttons
Buttons = [
    Button(20, 150, 80, 80, '1'),
    Button(110, 150, 80, 80, '2'),
    Button(200, 150, 80, 80, '3'),
    Button(290, 150, 80, 80, '+'),
    Button(20, 250, 80, 80, '4'),
    Button(110, 250, 80, 80, '5'),
    Button(200, 250, 80, 80, '6'),
    Button(290, 250, 80, 80, '-'),
    Button(20, 350, 80, 80, '7'),
    Button(110, 350, 80, 80, '8'),
    Button(200, 350, 80, 80, '9'),
    Button(290, 350, 80, 80, '/'),
    Button(20, 450, 80, 80, 'AC'),
    Button(110, 450, 80, 80, '0'),
    Button(200, 450, 80, 80, '='),
    Button(290, 450, 80, 80, '*'),
]

# Music stop button
music_stop_button = Button(20, 550, 350, 40, 'All music stop')

# Calculator logic
currentinput = ""
result = None

def calculate():
    global currentinput, result
    try:
        result = eval(currentinput)
        currentinput = str(result)
    except:
        result = "Error."

def AC():
    global currentinput, result
    currentinput = ""
    result = None

def musicstop():
    pygame.mixer.stop()

# Main game loop
running = True
while running:
    screen.fill(BGCOLOUR)

    inputsurf = resultscreenfont.render(currentinput, True, black)
    screen.blit(inputsurf, (20, 50))
    
    if result is not None:
        result_surf = resultscreenfont.render(f'{result}', True, black)
        screen.blit(result_surf, (20, 100))
        result = None
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in Buttons:
                if button.isclicked(event.pos):
                    if button.text == "=":
                        calculate()
                    elif button.text == "AC":
                        AC()
                    else:
                        currentinput += button.text
                        if button.text == '1': button_click_sound1.play()
                        elif button.text == '2': button_click_sound2.play()
                        elif button.text == '3': button_click_sound3.play()
                        elif button.text == '4': button_click_sound4.play()
                        elif button.text == '5': button_click_sound5.play()
                        elif button.text == '6': button_click_sound6.play()
                        elif button.text == '7': button_click_sound7.play()
                        elif button.text == '8': button_click_sound8.play()
                        elif button.text == '9': button_click_sound9.play()
                        elif button.text == '0': button_click_sound0.play()
                        elif button.text == '+': button_click_soundplus.play(loops=-1)
                        elif button.text == '-': button_click_soundmin.play(loops=-1)
                        elif button.text == '/': button_click_sounddiv.play(loops=-1)
                        elif button.text == '*': button_click_soundmul.play(loops=-1)
            
            if music_stop_button.isclicked(event.pos):
                musicstop()
        
        # Keyboard
        if event.type == pygame.KEYDOWN:
            if event.key in key_to_button_map:
                button_text = key_to_button_map[event.key]
                
                if button_text == 'BACK':
                    currentinput = currentinput[:-1]
                elif button_text == '=':
                    calculate()
                elif button_text == 'AC':
                    AC()
                else:
                    currentinput += button_text
                    if button_text == '1': button_click_sound1.play()
                    elif button_text == '2': button_click_sound2.play()
                    elif button_text == '3': button_click_sound3.play()
                    elif button_text == '4': button_click_sound4.play()
                    elif button_text == '5': button_click_sound5.play()
                    elif button_text == '6': button_click_sound6.play()
                    elif button_text == '7': button_click_sound7.play()
                    elif button_text == '8': button_click_sound8.play()
                    elif button_text == '9': button_click_sound9.play()
                    elif button_text == '0': button_click_sound0.play()
                    elif button_text == '+': button_click_soundplus.play(loops=-1)
                    elif button_text == '-': button_click_soundmin.play(loops=-1)
                    elif button_text == '/': button_click_sounddiv.play(loops=-1)
                    elif button_text == '*': button_click_soundmul.play(loops=-1)
    
    # Check for currently pressed keys for highlighting
    pressed_keys = pygame.key.get_pressed()
    current_key_button = None
    
    for key, button_text in key_to_button_map.items():
        if pressed_keys[key]:
            current_key_button = button_text
            break

    for button in Buttons:
        if (current_key_button == button.text or 
            button.rect.collidepoint(pygame.mouse.get_pos())):
            button.colour = button.hovercolour
        else:
            button.colour = white
        button.draw(screen)
    
    if music_stop_button.rect.collidepoint(pygame.mouse.get_pos()):
        music_stop_button.colour = music_stop_button.hovercolour
    else:
        music_stop_button.colour = white
    music_stop_button.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
    pygame.display.flip()

pygame.quit()
sys.exit()
