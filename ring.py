class Process:
    def __init__(self, pid):
        self.id = pid
        self.active = True


class Ring:
    def __init__(self):
        self.noOfProcesses = 0
        self.processes = []

    def initialiseRing(self):
        print("Enter the number of processes:")
        self.noOfProcesses = int(input())
        self.processes = [Process(i) for i in range(self.noOfProcesses)]

    def getMax(self):
        maxId = -99
        maxIdIndex = 0
        for i in range(len(self.processes)):
            if self.processes[i].active and self.processes[i].id > maxId:
                maxId = self.processes[i].id
                maxIdIndex = i
        return maxIdIndex

    def performElection(self):
        maxIndex = self.getMax()
        if maxIndex == -1:
            print("No active processes found. Exiting.")
            return

        print("Process no", self.processes[maxIndex].id, "fails")
        self.processes[maxIndex].active = False

        print("Election Initiated by")
        initiatorProcess = int(input())

        prev = initiatorProcess
        next = (prev + 1) % self.noOfProcesses

        while next != initiatorProcess:
            if self.processes[next].active:
                print("Process", self.processes[prev].id, "pass Election(", self.processes[prev].id, ") to",
                      self.processes[next].id)
                prev = next

            next = (next + 1) % self.noOfProcesses

        print("Process", self.processes[self.getMax()].id, "becomes coordinator")
        coordinator = self.processes[self.getMax()].id

        prev = coordinator
        next = (prev + 1) % self.noOfProcesses

        while next != coordinator:
            if self.processes[next].active:
                print("Process", self.processes[prev].id, "pass Coordinator(", coordinator, ") message to process",
                      self.processes[next].id)
                prev = next

            next = (next + 1) % self.noOfProcesses

        print("End Of Election")

    def main(self):
        r = Ring()
        r.initialiseRing()
        r.performElection()


if __name__ == "__main__":
    ring = Ring()
    ring.main()
