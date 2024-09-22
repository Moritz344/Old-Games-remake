import curses

menu_options = ["START","ABOUT","EXIT"]
def menu(stdscr,selected_row_idx):
    stdscr.clear()
    h,w = stdscr.getmaxyx()

    for idx, row in enumerate(menu_options):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu_options) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_BLACK,curses.COLOR_WHITE)

    current_row = 0
    menu(stdscr,current_row)
    
    
    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_options) - 1:
            current_row += 1

        menu(stdscr,current_row)

        stdscr.refresh()

curses.wrapper(main)



