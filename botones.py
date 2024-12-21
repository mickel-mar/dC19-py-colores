import curses

# entrega el lugar de un caracter en una palabra o None si no la encuentra
def get_button_color_index(letter, word):
    index = word.index(letter) if letter in word else None
    return index

def draw_button(win, text, y, x, color_pair, pos_char):
    button_text = f"[ {text.center(10)} ]"  # Alinear el texto al centro en 12 caracteres
    if x + len(button_text) < curses.COLS:  # Verificar que el texto cabe en la pantalla
        win.attron(curses.color_pair(color_pair))  # Aplicar el par de colores
        win.addstr(y, x, button_text)
        
        # Mostrar la letra esperada en color inverso al del botón
        expected_key = text[pos_char].upper()  # Tomar la primera letra del texto
        inverted_color_pair = color_pair + 8  # Obtener el color inverso
        win.attron(curses.color_pair(inverted_color_pair))  # Aplicar color inverso
        win.addch(y, x + pos_char + 6 - (len(text) // 2) + (1 & len(text) % 2==0), expected_key)  # Colocar la letra esperada
        win.attroff(curses.color_pair(inverted_color_pair))  # Desactivar color inverso
        
        win.attroff(curses.color_pair(color_pair))  # Desactivar el par de colores
        win.refresh()
    else:
        raise ValueError("El texto del botón es demasiado largo para la posición especificada")

def main(stdscr):
    stdscr.clear()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Definir colores para el par de colores
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_YELLOW)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_CYAN)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_RED)
    
    # Definir los textos y colores de los botones
    buttons = [
        ("User", 1, 0),
        ("Chat", 2, 1),
        ("Reacciones", 3, 0),
        ("Compartir", 4, 0),
        ("Ayuda", 5, 0),
        ("Más", 6, 0)
    ]
    
    aaa = buttons[0][1]
    stdscr.addstr(1, 1, aaa.__str__())
    
    # Dibujar los botones en las dos últimas líneas de la pantalla
    button_width = 14
    button_padding = 0
    start_x = 0
    word = "" 
    
    for i, (text, color_pair, pos_char) in enumerate(buttons):
        button_x = start_x + (button_width + button_padding) * i
        draw_button(stdscr, text, 23, button_x, color_pair, pos_char)
        word += text[pos_char].upper()    
    
    # stdscr.addstr(1, 1, word)
    # stdscr.getch()

    while True:
        key = stdscr.getch()  # Obtener la tecla presionada
        
        # Lógica para cambiar el color al presionar la tecla asociada a cada botón
        if chr(key).upper() in word:
            index = word.index(chr(key).upper())
            # aaa = buttons[index][0]
            # stdscr.addstr(1, 1, aaa)
            button_x = start_x + (button_width + button_padding) * (index - 1)
            # draw_button(stdscr, chr(key).upper(), 23, button_x, color_pair, pos_char) # Cambiar a color activo basado en la letra presionada
            draw_button(stdscr, buttons[index][0], 23, button_x, 7, buttons[index][2])
        
        stdscr.refresh()

curses.wrapper(main)
