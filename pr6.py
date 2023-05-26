class BullyAlgo:
    no_of_process = 0
    priority = []
    S = []
    C = 0

    @staticmethod
    def elect_process(e):
        e = e - 1
        BullyAlgo.C = e + 1

        for i in range(BullyAlgo.no_of_process):
            if BullyAlgo.priority[e] < BullyAlgo.priority[i]:
                print("Election message is sent from", e+1, "to", i+1)
                if BullyAlgo.S[i] == 1:
                    BullyAlgo.elect_process(i+1)

    @staticmethod
    def main():
        print("Select the number of processes that are to be done:")
        BullyAlgo.no_of_process = int(input())

        for i in range(BullyAlgo.no_of_process):
            print("Status for process", i+1, ":")
            BullyAlgo.S.append(int(input()))
            print("Priority of the current process", i+1, ":")
            BullyAlgo.priority.append(int(input()))

        print("Which process has to be elected for initiation:")
        e = int(input())

        BullyAlgo.elect_process(e)
        print("After electing process, the final coordinator is", BullyAlgo.C)


BullyAlgo.main()