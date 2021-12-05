import sys

def build_2d_array():
    a = []
    for row in range(5):
        v = []
        for column in range(5):
            v.append(False)
        a.append(list(v))
    return a

class Card:
    def __init__(self, lines):
        self.lines = lines
        self.marked_rows = build_2d_array()
        self.marked_columns = build_2d_array()
    
    def mark_value(self, value):
        for row in range(5):
            for column in range(5):
                if self.lines[row][column] == value:
                    self.marked_rows[row][column] = True
                    self.marked_columns[column][row] = True
                    return
    
    def wins(self):
        for i in range(5):
            if self.marked_rows[i] == [True] * 5:
                return True
            if self.marked_columns[i] == [True] * 5:
                return True

    def sum_of_unmarked(self):
        unmarked = []
        for row in range(5):
            for column in range(5):
                if not self.marked_rows[row][column]:
                    unmarked.append(self.lines[row][column])
        return sum(unmarked)
    
    def __repr__(self):
        s = ''
        for i in range(5):
            s += ' '.join(map(lambda s: s.rjust(2), map(str, self.lines[i])))
            s += ' - '
            s += ' '.join(map(lambda m: 'T' if m else 'F', self.marked_rows[i]))
            s += "\n"
        return s

picks = None
cards = []
card_lines = []

for line in sys.stdin:
    if picks is None:
        picks = map(int, line.split(','))
    else:
        if len(line.rstrip()) == 0:
            if len(card_lines) == 0:
                pass
            else:
                cards.append(Card(card_lines))
                card_lines = []
        else:
            card_lines.append(list(map(int, line.split())))

cards.append(Card(card_lines))

for pick in picks:
    print(f'--- Pick: {pick} ---')
    print()
    for card in cards:
        card.mark_value(pick)
        print(card)
    for card in cards:
        if card.wins():
            print('--- WINNER!! ---')
            print()
            print(card)
            print(card.sum_of_unmarked() * pick)
            exit()
