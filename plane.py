class Plane:
    def __init__(self, length):
        self.length = length
        self.seat_length = 7
        self.seats = [[[] for i in range(self.length + 2)] for j in range(self.seat_length)]

    def print_plane(self):
        row = "   "
        for i in range(self.length + 2):
            row += str(i) + "  "
        print(row)
        seat_letter = 0
        for rows in self.seats:
            row = str()
            if seat_letter < 3:
                row = chr(70 - seat_letter) + ":"
            if seat_letter > 3:
                row = chr(71 - seat_letter) + ":"
            if seat_letter is 3:
                row = "I:"
            for seat in rows:
                if len(seat):
                    row += str(seat[-1]) + "|"
                else:
                    row += "..|"
            print(row)
            seat_letter += 1
        print()

    def print_plane_scheme(self):
        seats = [[[] for i in range(self.length + 2)] for j in range(self.seat_length)]
        for col in range(self.seat_length):
            for seat in range(1, self.length + 1):
                if col == (self.seat_length - 1) / 2:
                    seats[col][seat].append("--")
                elif col < (self.seat_length - 1) / 2:
                    seats[col][seat].append(str(seat) + chr(ord("A") - 2 + self.seat_length - col))
                else:
                    seats[col][seat].append(str(seat) + chr(ord("A") - 1 + self.seat_length - col))
            print(seats[col])

    def add_passengers(self, psg_list):
        for psg in psg_list:
            psg.add_to_plane(self)

    def isEmpty(self, row, seat):
        try:
            if not(len(self.seats[seat][row])):
                return True
            else:
                return False
        except IndexError:
            return True

    def move_row(self, row, seat_letter):
        seat_index = int()
        if seat_letter in ['A', 'B', 'C']:
            seat_index = 71 - ord(seat_letter)

        if seat_letter in ['D', 'E', 'F']:
            seat_index = 70 - ord(seat_letter)

        if not(len(self.seats[3][row + 1])):
            if seat_letter is 'A':
                if len(self.seats[seat_index - 1][row]):
                    self.seats[3][row + 1].append(self.seats[seat_index - 1][row][-1])
                    self.seats[seat_index - 1][row].pop()
                if len(self.seats[seat_index - 2][row]):
                    self.seats[3][row + 1].append(self.seats[seat_index - 2][row][-1])
                    self.seats[seat_index - 2][row].pop()

            if seat_letter is 'B':
                if len(self.seats[seat_index - 1][row]):
                    self.seats[3][row + 1].append(self.seats[seat_index - 1][row][-1])
                    self.seats[seat_index - 1][row].pop()

            if seat_letter is 'E':
                if len(self.seats[seat_index + 1][row]):
                    self.seats[3][row + 1].append(self.seats[seat_index + 1][row][-1])
                    self.seats[seat_index + 1][row].pop()

            if seat_letter is 'F':
                if len(self.seats[seat_index + 1][row]):
                    self.seats[3][row + 1].append(self.seats[seat_index + 1][row][-1])
                    self.seats[seat_index + 1][row].pop()
                if len(self.seats[seat_index + 2][row]):
                    self.seats[3][row + 1].append(self.seats[seat_index + 2][row][-1])
                    self.seats[seat_index + 2][row].pop()

    def return_row(self, row):
        while len(self.seats[3][row + 1]):
            seat = self.seats[3][row + 1][-1].seat_index
            row = self.seats[3][row + 1][-1].row
            self.seats[seat][row].append(self.seats[3][row + 1][-1])
            self.seats[3][row + 1].pop()

    def move_passengers(self):
        for position in range(self.length, -1, -1):
            if len(self.seats[3][position]):
                self.seats[3][position][-1].move()

    def boarding_finished(self):
        for position in self.seats[3]:
            if len(position):
                return False

        for seat in range(self.seat_length):
            for row in range(1, self.length + 1):
                if seat != (self.seat_length - 1) / 2:
                    if not(len(self.seats[seat][row])):
                        return False
        return True
