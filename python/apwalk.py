#!/usr/bin/env python
import curses
import subprocess

loopmax = 1000

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
	curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
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

tw = col - 2							# Set up left / right widths and positions
bw = col - 2
mw = col - 2
tx = 1
bx = 1
mx = 1
ty = 2
th = 2
bh = 4
by = row - (bh + 1)
my = th + ty + 2
mh = row - (my + bh + 3)

ah = 1
at = col - 2
ap = ah
assid = list()
apowr = list()
hscale = float(mh) / 100.0

for loop in range (ah, at):
	assid.append ("00:00:00:00:00:00")
	apowr.append (-100)

topwin = curses.newwin(th, tw, ty, tx)				# Set up status windows
midwin = curses.newwin(mh, mw, my, mx)
botwin = curses.newwin(bh, bw, by, bx)
midwin.scrollok(1)

stdscr.bkgd(' ', curses.color_pair(4))				# ...and set their colours

stdscr.addstr(ty - 1, 1, "Current AP", curses.A_BOLD)
stdscr.addstr(my - 1, 1, "RSSI", curses.A_BOLD)
stdscr.addstr(by - 1, 1, "History", curses.A_BOLD)

topwin.bkgd(' ', curses.color_pair(1))
midwin.bkgd(' ', curses.color_pair(2))
botwin.bkgd(' ', curses.color_pair(3))

init_paint()							# Paint the screen

# Main loop goes here
for loop in range(0, loopmax):
	subprocess.call('../bash/getAP.sh > MAC', shell=True)
	f = open("MAC", "r")
	SSID = (f.readline())
	powr = (f.readline())
	f.close()

	for column in range(ah + 1, (at - 1)):
		apowr[column - 1] = int(apowr[column])
	apowr[at - 2] = int(powr.strip())
	topwin.addstr(0, 0, SSID)
	midwin.clear()
	for column in range(ah, (at - 1)):
		height = abs((apowr[column]))
		for winrow in range(1, height):
			text = "X"
			midwin.addstr((mh - 1) - (int(winrow * hscale)), column, text)

	paint()							# Re-paint / update screen

#	junk = midwin.getch()

finish_screen(stdscr)						# End the program
print ("powr hscale: " + str(hscale))
