#!/usr/bin/env python
import curses
def init_screen():
	screen = curses.initscr()				# Initialise stdscr as a curses window
	curses.noecho()						# Settings to make it terminal friendly
	curses.cbreak()
	screen.keypad(1)
	r, c = screen.getmaxyx()				# Get the size of the terminal window
	curses.start_color()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
	curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLUE)
	curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLUE)
	curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_GREEN)
	return screen, r, c

def init_win(h, w, y, x):					# Set up a new window
	newwin = curses.newwin(h, w, y, x)
	return newwin

def finish_screen(screen):					# Clean up all these windows
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()

def init_paint():						# Paint the screen
	stdscr.refresh()
	topwin.refresh()
	midwin.refresh()
	botwin.refresh()

def paint():							# Re-Paint the screen
	topwin.refresh()
	midwin.refresh()
	botwin.refresh()

stdscr, row, col = init_screen()				# Set up main screen and initialise curses

th = 2								# Calculations for window positions
tw = col - 2
ty = 1
tx = 1
bh = 5
bw = col - 2
by = row - 5
bx = 1
mh = row - ( th + ty + bh + by )
mw = col - 2
my = 4
mx = 1

topwin = curses.newwin(th, tw, ty, tx)				# Set up status windows
midwin = curses.newwin(row - 14, col - 2, 4, 1 )
botwin = curses.newwin(5, col -2, row - 8, 1)

stdscr.bkgd(' ', curses.color_pair(4))				# ...and set their colours

stdscr.addstr(0, 1, "Current AP")
stdscr.addstr(my - 1, 1, "RSSI")
stdscr.addstr(by - 1, 1, "History")

topwin.bkgd(' ', curses.color_pair(1))
midwin.bkgd(' ', curses.color_pair(2))
botwin.bkgd(' ', curses.color_pair(3))

init_paint()							# Paint the screen

topwin.addstr("Current AP: \n")
botwin.addstr("Date Time RSSI SSID\n")

paint()								# Re-paint / update screen

topwin.getch()

#stdscr.addstr(row-2, 0, "This screen has " + str (row) + " rows and " + str (col) + " columns.\n")
#stdscr.addstr("Try resizing your window(if possible) and then run this program again")
#stdscr.refresh()

finish_screen(stdscr)
