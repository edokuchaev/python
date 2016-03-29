all_trains = {}

class Station():
    def __init__(self, id, ways=()):
        self.id = id  #int
        self.ways = []  #list
        for i in ways:
            self.ways.append(i)


    def time_table (self):
        for number, way in enumerate(self.ways):
            print('Way number {} is {}'.format(number, not way.is_empty()), end=' ')
            if not way.is_empty():
                print(way.t.id, way.t.type)
            else:
                print()

class Way(object):
    def __init__(self, id):
        self.id = id  #int
        self.empty = True  #bool
        self.t = None

    def is_empty(self):
        return self.empty

    def train_set(self, train):
        self.t = train  #train
        self.empty = False

    def train_dept(self):
        print('The train number {} has departed'.format(self.t.id))
        self.t = None
        self.empty = True

class Train(object):
    def __init__(self, id, type):
        self.id = id  #int
        self.type = type  #str

for i in range(1,4):
    all_trains[i] = Train(i, 'Passenger')

class Dispatcher(object):
    def __init__(self, station):
        self.station = station

        for i in self.station.ways:
            if  i.is_empty():
                i.train_set(all_trains[1])
                break
        else:
            print('All ways are busy')

    def work(self):
        self.station.time_table()
        self.station.ways[0].train_dept()
        print('Way number {} is empty now'.format(self.station.ways[0].id))
        self.station.time_table()

def main():
    station = Station(1, (Way(1), Way(2)))
    Dispatcher(station).work()

if __name__ == '__main__':
    main()

