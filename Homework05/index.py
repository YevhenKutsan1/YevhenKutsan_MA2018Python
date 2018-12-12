import simplegui
import random

CARDS_COUNT = 16
CARD_WIDTH = 50
CARD_HEIGHT = 100
CARD_INTERVAL = 10

LABEL = None

cards = []
flipped_cards = []
game_state = 0
attempts = 0

class Point:
    # constructor
    def __init__(self, _x, _y):
        self.x = _x;
        self.y = _y;

class Card:
    # constructor
    def __init__(self, number, state, border):
        self.number = number
        self.state  = state
        self.p1 = Point(border[0].x, border[0].y)
        self.p2 = Point(border[1].x, border[1].y)
        self.p3 = Point(border[2].x, border[2].y)
        self.p4 = Point(border[3].x, border[3].y)
        self.x_min = min([self.p1.x, self.p2.x, self.p3.x, self.p4.x])
        self.x_max = max([self.p1.x, self.p2.x, self.p3.x, self.p4.x])
        self.y_min = min([self.p1.y, self.p2.y, self.p3.y, self.p4.y])
        self.y_max = max([self.p1.y, self.p2.y, self.p3.y, self.p4.y])
        
    def draw(self, _canvas):
        if self.state:
            _canvas.draw_polygon(
                [[self.p1.x, self.p1.y],
                [self.p2.x, self.p2.y],
                [self.p3.x, self.p3.y],
                [self.p4.x, self.p4.y]],
                3,
                "Green")
            _canvas.draw_text(str(self.number), [self.p1.x + CARD_WIDTH /2 - 5, self.p1.y + CARD_HEIGHT / 2 - 5], 20, "Green")
        else:
            _canvas.draw_polygon(
                [[self.p1.x, self.p1.y],
                [self.p2.x, self.p2.y],
                [self.p3.x, self.p3.y],
                [self.p4.x, self.p4.y]],
                3,
                "Red")            
        
    def flipped(self):
        return self.state
    
    def flip_up(self):
        self.state = True
        
    def flip_down(self):
        self.state = False
        
    def contains_point(self, p):
        if self.x_min <= p.x and self.x_max >= p.x and self.y_min <= p.y and self.y_max >= p.y:
            return True
        else:
            return False

def new_game():
    attempts = 0
    LABEL.set_text("Turns = " + str(attempts))
    
    L = [i for i in range(0, CARDS_COUNT / 2)] 
    L2 = [0] * CARDS_COUNT     
    for i in range(0, (CARDS_COUNT / 2)):
        L2[i] = L[i]
        L2[i + CARDS_COUNT / 2] = L[i]
    random.shuffle(L2)
    
    if len(cards) > 0:
        for card in cards:
            del card
        cards[:] = []
        
    for i in range(0, CARDS_COUNT):
        p1 = Point(CARD_INTERVAL + i * CARD_INTERVAL + i * CARD_WIDTH, CARD_INTERVAL);
        p2 = Point(CARD_INTERVAL + i * CARD_INTERVAL + i * CARD_WIDTH, CARD_INTERVAL + CARD_HEIGHT)
        p3 = Point(CARD_INTERVAL + i * CARD_INTERVAL + i * CARD_WIDTH + CARD_WIDTH, CARD_INTERVAL + CARD_HEIGHT)
        p4 = Point(CARD_INTERVAL + i * CARD_INTERVAL + i * CARD_WIDTH + CARD_WIDTH, CARD_INTERVAL)
        cards.append(Card(L2[i], False, [p1, p2, p3, p4]))
     
def mouseclick(pos):
    global game_state, attempts
    point = Point(pos[0], pos[1])
    for card in cards:
        if card.contains_point(point) and not card.flipped():
            card.flip_up()
            attempts += 1
            if game_state == 0 or game_state == 1:
                game_state += 1
                flipped_cards.append(card)
            else:
                game_state = 1
                if flipped_cards[0].number <> flipped_cards[1].number:
                    flipped_cards[0].flip_down()
                    flipped_cards[1].flip_down()                    
                flipped_cards[:] = []
                flipped_cards.append(card)
    LABEL.set_text("Turns = " + str(attempts))
                            
def draw(canvas):
    for card in cards:
        card.draw(canvas)

w = (CARDS_COUNT + 1) * CARD_INTERVAL + CARDS_COUNT * CARD_WIDTH
h = 2 * CARD_INTERVAL + CARD_HEIGHT
frame = simplegui.create_frame("Memory", w, h)

frame.add_button("Reset", new_game)
LABEL = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()