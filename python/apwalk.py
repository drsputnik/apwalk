import curses
def init_screen():
	stdscr = curses.initscr()			# Initialise stdscr as a curses window
	curses.noecho()					# Settings to make it terminal friendly
	curses.cbreak()
	stdscr.keypad(1)

	#row = 0
	#col = 0

	r, c = stdscr.getmaxyx()			# Get the size of the terminal window
	return r, c

row, col = init_screen();
stdscr.addstr(row-2, 0, "This screen has " + str (row) + " rows and " + str (col) + " columns.")
stdscr.addstr("Try resizing your window(if possible) and then run this program again")
stdscr.refresh()
stdscr.getch()
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

