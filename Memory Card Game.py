# Memory Card Game
# Turn over the cards, match the pairs

import simplegui
import random
c = [i % 8 for i in range(16)]
state = 0
cards = [[i % 8 for i in range(16)], False]
cardone = 0
cardtwo = 1
moves = 0

# helper function to initialize globals
def init():
    global state, cards, moves
    cards = [[c[0], False],[c[1], False],[c[2], False],[c[3], False],
    [c[4], False],[c[5], False],[c[6], False],[c[7], False],
    [c[8], False],[c[9], False],[c[10], False],[c[11], False],
    [c[12], False],[c[13], False],[c[14], False],[c[15], False]]

    random.shuffle(cards)

    state = 0
    moves = 0

# define event handlers
def mouseclick(pos):
    global state, cards, cardone, cardtwo, moves

    if 0 <= pos[1] <= 100 and cards[pos[0] // 50][1] == False: # if the y coordinate of pos is within the frame and the card you clicked on is face down
        if state == 0:
            state = 1
            cardone = pos[0] // 50
            cards[(pos[0] // 50)][1] = True
        elif state == 1:
            state = 2
            cardtwo = pos[0] // 50
            cards[(pos[0] // 50)][1] = True
            moves += 1
        elif state == 2:
            state = 1
            if cards[cardone][0] != cards[cardtwo][0] :
                cards[cardone][1] = False
                cards[cardtwo][1] = False
            cardone = pos[0] // 50
            cards[pos[0] // 50][1] = True

# cards are logically 50x100 pixels in size
def draw(canvas):
    global cards, state
    l.set_text("Moves = " + str(moves))
    for c in range(len(cards)):
        if cards[c][1] == True:
            canvas.draw_text(str(cards[c][0]), (c*50 + 10, 75), 50, "White")
        elif cards[c][1] == False:
            canvas.draw_polygon([(c*50, 0), ((c+1)*50, 0), ((c+1)*50, 100), (c*50, 100)], 5,"Orange", "Black")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart Game", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
