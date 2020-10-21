#Bello~ Welcome to Minions Lab!
# Hello word - homework - week 3
# Yuxuan Hou
#Actually I don't know why my minions can't go up and down. And when it died, it won't print the slogan"Madoka, sayonara!"



# Minions LAB
import curses
import random

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

minions_y = int(sh/2)
minions_x = int(sw/4)
minions = [
    [minions_y, minions_x],
    [minions_y, minions_x-1],
    [minions_y, minions_x-2]
]

banana = [int (sh/2), int (sw/2)]
w.addch(banana[0], banana[1], "$")

kr = curses.KEY_RIGHT
kl = curses.KEY_LEFT
ku = curses.KEY_UP
kd = curses.KEY_DOWN

key = kr
while True:
    next_key = w.getch()
    if next_key in [kr, kl, ku, kd]:
        if (key == kr and next_key != kl) or\
            (key == kl and next_key != kr) or\
            (key == ku and next_key != kd) or\
            (key == kd and next_key != ku) :
            key = next_key

    if minions[0] in minions[1:] or\
        minions[0] [0] in [0, sh] or\
        minions[0] [1] in [0, sw] :
        curses.endwin()
        print ("Madoka, sayonara!")
        quit()
      
    new_head = [minions[0][0], minions[0][1]]
    if key == kl:
          new_head[1] -= 1
    if key == kr:
          new_head[1] += 1
    if key == ku:
          new_head[1] -= 1
    if key == kd:
          new_head[1] += 1
    minions.insert(0, new_head)

    if minions[0] == banana:
        banana = None
        while banana is None:
            newbanana = [
                random.randint(1, sh - 1), 
                random.randint(1, sw - 1)
            ]
            banana = newbanana if newbanana not in minions else None
        w.addch(banana[0], banana[1], "$")
    else:
        hair = minions.pop()
        w.addch(hair[0], hair[1], " ")
    w.addch (minions[0][0], minions[0][1], "0")
  