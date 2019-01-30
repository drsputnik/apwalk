#!/usr/bin/env python
import curses
def init_screen():
	screen = curses.initscr()				# Initialise stdscr as a curses window
	curses.noecho()						# Settings to make it terminal friendly
	curses.cbreak()
	screen.keypad(1)
	r, c = screen.getmaxyx()				# Get the size of the terminal window
	return screen, r, c

def init_win(h, w, y, x):
	newwin = curses.newwin(h, w, y, x)
	return newwin

def finish_screen(screen):
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()

stdscr, row, col = init_screen()				# Set up main screen and initialise curses
curses.start_color()

topwin = curses.newwin(2, col - 2, 1, 1)			# Set up status window
curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
topwin.bkgd(' ', curses.color_pair(1))

midwin = curses.newwin(row - 9, col - 2, 4, 1 )
botwin = curses.newwin(5, col -2, row - 8, 1)


#midwin = newwin(

topwin.addstr("Current AP: \n")
topwin.refresh();
topwin.getch()

#stdscr.addstr(row-2, 0, "This screen has " + str (row) + " rows and " + str (col) + " columns.\n")
#stdscr.addstr("Try resizing your window(if possible) and then run this program again")
#stdscr.refresh()

finish_screen(stdscr)
