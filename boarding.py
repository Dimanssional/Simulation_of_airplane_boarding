from passenger import Passenger
from plane import Plane
from random import randint

from time import sleep

# https://www.youtube.com/watch?v=oAHbLRjF0vo inspired by :D


class Boarding:
    def __init__(self):
        self.plane = None

    def generate_boarding(self, plane_length):
        pass

    def run_simulation(self, plane_length):
        self.generate_boarding(plane_length)
        if self.plane is not None:
            steps = 0
            self.plane.seats[3][0].reverse()
            while(not self.plane.boarding_finished()):
                #self.plane.print_plane()
                self.plane.move_passengers()
                #sleep(1)
                steps += 1
            self.plane.print_plane()
            return steps
        else:
            return 0

    def test_boarding_method(self, plane_length, no_simulation):
        sum_of_values = 0.0
        list_of_values = list()
        for count in range(no_simulation):
             value = self.run_simulation(plane_length)
             list_of_values.append(value)
             sum_of_values += value
        return sum_of_values / no_simulation, list_of_values


class BoardingFTB(Boarding):
    def generate_boarding(self, plane_length):
        passengers = list()
        seatList = list()
        for number in range(1, plane_length, plane_length // 4):
            seats = set()
            while len(seats) < plane_length * 6 / 4:
                seats.add((randint(number, number + (plane_length // 4) - 1), chr(randint(65, 70))))
            seatList.extend(list(seats))
        for seat in seatList:
            passengers.append(Passenger(seat[0], seat[1], randint(0, 2)))
        self.plane = Plane(plane_length)
        self.plane.add_passengers(passengers)
        return passengers


class BoardingBTF(Boarding):
    def generate_boarding(self, plane_length):
        passengers = list()
        seatList = list()
        for number in range(1, plane_length, plane_length // 4):
            seats = set()
            while len(seats) < plane_length * 6 / 4:
                seats.add((randint(number, number + (plane_length // 4) - 1), chr(randint(65, 70))))
            seatList.extend(list(seats))
        for seat in seatList:
            passengers.append(Passenger(seat[0], seat[1], randint(0, 2)))
        passengers.reverse()
        self.plane = Plane(plane_length)
        self.plane.add_passengers(passengers)
        return passengers


class BoardingWTA(Boarding):
    def generate_boarding(self, plane_length):
        passengers = list()
        seatList = list()
        for count in range(1, 4):
            seats = set()
            while len(seats) < plane_length * 2:
                seats.add((randint(1, plane_length), chr(64 + count)))
                seats.add((randint(1, plane_length), chr(71 - count)))
            seatList.extend(list(seats))
        for seat in seatList:
            passengers.append(Passenger(seat[0], seat[1], randint(0, 2)))
        self.plane = Plane(plane_length)
        self.plane.add_passengers(passengers)
        return passengers


class BoardingATW(Boarding):
    def generate_boarding(self, plane_length):
        passengers = list()
        seatList = list()
        for count in range(1, 4):
            seats = set()
            while len(seats) < plane_length * 2:
                seats.add((randint(1, plane_length), chr(64 + count)))
                seats.add((randint(1, plane_length), chr(71 - count)))
            seatList.extend(list(seats))
        for seat in seatList:
            passengers.append(Passenger(seat[0], seat[1], randint(0, 2)))
        passengers.reverse()
        self.plane = Plane(plane_length)
        self.plane.add_passengers(passengers)
        return passengers


class BoardingRandom(Boarding):
    def generate_boarding(self, plane_length):
        passengers = list()
        seatList = set()
        while len(seatList) is not 6 * plane_length:
            seatList.add((randint(1, plane_length), chr(randint(65, 70))))
        for seat in seatList:
            passengers.append(Passenger(seat[0], seat[1], randint(0, 2)))
        self.plane = Plane(plane_length)
        passengers.reverse()
        self.plane.add_passengers(passengers)
        return passengers


class BoardingSteffen(Boarding):
    def generate_boarding(self, plane_length):
        passengers = list()
        seatList = list()
        for count in range(0, 3):
            for i in range(plane_length, 0, -2):
                seatList.append((i, chr(65 + count)))
            for i in range(plane_length, 0, -2):
                seatList.append((i, chr(70 - count)))
            for i in range(plane_length - 1, 0, -2):
                seatList.append((i, chr(65 + count)))
            for i in range(plane_length - 1, 0, -2):
                seatList.append((i, chr(70 - count)))
        for seat in seatList:
            passengers.append(Passenger(seat[0], seat[1], randint(0, 2)))
        self.plane = Plane(plane_length)
        self.plane.add_passengers(passengers)
        return passengers


if __name__ == "__main__":
    """wta = BoardingWTA()
    wta.generate_boarding(8)"""


    """
    ftb = BoardingFTB()
    psgrs = ftb.generate_boarding(20)
    for psg in psgrs:
        print(psg)
    """
    #btf = BoardingBTF()
    #psgrs = btf.generate_boarding(8)
    #for psg in psgrs:
        #print(psg)
    """
    rnd = BoardingRandom()
    psgrs = rnd.generate_boarding(8)
    for psg in psgrs:
        print(psg)


    rnd = BoardingRandom()
    psgrs = rnd.generate_boarding(8)
    for psg in psgrs:
        print(psg)
    """
    #ftb = BoardingFTB()
    #print(ftb.test_boarding_method(8, 10))

    random = BoardingRandom()
    print(random.test_boarding_method(8, 10))


    #stephens = BoardingSteffen()
    #stephens.generate_boarding(8)