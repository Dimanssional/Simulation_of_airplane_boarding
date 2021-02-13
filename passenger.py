class Passenger:
    def __init__(self, row, seat, no_of_bags):
        if seat not in ['A', 'B', 'C', 'D', 'E', 'F']:
            raise ValueError("Seat must be a letter from A to F")

        self.row = row
        self.seat = seat
        self.bags = no_of_bags * 4
        self.seat_index = int()
        self.remove_row = False

        if self.seat in ['A', 'B', 'C']:
            self.seat_index = 71 - ord(self.seat)

        if self.seat in ['D', 'E', 'F']:
            self.seat_index = 70 - ord(self.seat)

        self.plane = None
        self.current_position = [None, None]
                                #ROW   SEAT

    def __str__(self):
        return "{}{}".format(self.row, self.seat)

    def get_position(self):
        if self.plane is not None:
            return [self.current_position[1], self.current_position[0]]

    def get_seat(self):
        return [self.seat_index, self.row]

    def add_to_plane(self, plane):
        self.current_position = [0, 3]
        self.plane = plane
        self.plane.seats[3][0].append(self)

    def can_sit(self):
        if self.plane is not None:
            if self.seat is 'A' and not(len(self.plane.seats[self.current_position[1] + 2][self.current_position[0]])) and not(len(self.plane.seats[self.current_position[1] + 1][self.current_position[0]])):
                return True
            if self.seat is 'B' and not(len(self.plane.seats[self.current_position[1] + 1][self.current_position[0]])):
                return True
            if self.seat is 'C':
                return True
            if self.seat is 'D':
                return True
            if self.seat is 'E' and not(len(self.plane.seats[self.current_position[1] - 1][self.current_position[0]])):
                return True
            if self.seat is 'F' and not(len(self.plane.seats[self.current_position[1] - 2][self.current_position[0]])) and not(len(self.plane.seats[self.current_position[1] - 1][self.current_position[0]])):
                return True
        return False

    def forced_to_move(self, row, seat):
        self.current_position = [seat, row]
        self.plane.seats[row][seat].append(self)

    def move(self):
        if self.plane is None:
            raise TypeError("Passenger is not in the plane!")

        if self.row is not self.current_position[0]:
            if not(len(self.plane.seats[self.current_position[1]][self.current_position[0] + 1])):
                self.plane.seats[self.current_position[1]][self.current_position[0] + 1].append(self)
                self.plane.seats[self.current_position[1]][self.current_position[0]].pop()
                self.current_position[0] += 1
                return self.current_position[0], self.current_position[1]
            else:
                return self.current_position[0], self.current_position[1]

        if self.bags:
            self.bags -= 1
            return self.current_position[0], self.current_position[1]

        if self.row is self.current_position[0]:
            if self.can_sit():
                if self.remove_row:
                    self.remove_row = False
                    self.plane.return_row(self.row)
                self.plane.seats[self.seat_index][self.row].append(self)
                self.plane.seats[self.current_position[1]][self.current_position[0]].pop()
                self.current_position = [self.row, self.seat_index]
            else:
                self.plane.move_row(self.row, self.seat)
                self.remove_row = True
        return self.current_position[0], self.current_position[1]
