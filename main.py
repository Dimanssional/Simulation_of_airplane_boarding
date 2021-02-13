from boarding import *
from passenger import Passenger
from plane import Plane

if __name__ == "__main__":
    airbus = Plane(8)
    airbus.print_plane_scheme()
    psg1 = Passenger(1, 'A', 2)
    psg2 = Passenger(2, 'B', 3)
    psg3 = Passenger(1, 'B', 4)

    psgrs = list()

    psgrs.append(psg1)
    psgrs.append(psg2)
    psgrs.append(psg3)

    # print(psgrs)
    for psg in psgrs:
        print(psg)

    airbus.add_passengers(psgrs)
    airbus.print_plane()
