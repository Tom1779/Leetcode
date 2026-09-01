class UndergroundSystem:

    def __init__(self):
        self.stationTimes = dict()
        self.people = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.people[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stations = (self.people[id][0],stationName)
        if not stations in self.stationTimes:
            self.stationTimes[stations] = [t-self.people[id][1]]
        else:
            self.stationTimes[stations].append(t-self.people[id][1])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stations = (startStation, endStation)
        if not stations in self.stationTimes:
            return 0
        return sum(self.stationTimes[stations])/len(self.stationTimes[stations])
