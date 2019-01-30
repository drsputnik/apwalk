import curses
stdscr = curses.initscr()
row = 0
col = 0
curses.getmaxyx(stdscr, row, col)
curses.mvprintw(row-2, 0, "This screen has %d rows and %d columns\n", row, col)
curses.printw("Try resizing your window(if possible) and then run this program again")
curses.refresh()
curses.getch()
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
endwin()
