class TokenRing:
    def __init__(self, n):
        self.n = n
        self.m = n - 1
        self.token = 0

    def send_data(self, sender, receiver, data):
        print("Token passing:", end="")
        for i in range(self.token, self.token + self.n):
            print(" " + str(i % self.n) + "->", end="")
        print(" " + str(sender))

        print("Sender", sender, "sending data:", data)

        for i in range(sender + 1, receiver):
            print("data", data, "forwarded by", i % self.n)

        print("Receiver", receiver, "received data:", data)
        self.token = sender

    def main(self):
        while True:
            try:
                print("Enter the number of nodes:")
                n = int(input())
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")

        token_ring = TokenRing(n)

        while True:
            try:
                print("Enter sender:")
                sender = int(input())
                print("Enter receiver:")
                receiver = int(input())
                print("Enter data:")
                data = int(input())
                token_ring.send_data(sender, receiver, data)
            except ValueError:
                print("Invalid input! Please enter an integer.")
            except KeyboardInterrupt:
                print("\nProgram interrupted. Exiting...")
                break

            while True:
                try:
                    print("Do you want to send again? Enter 1 for Yes and 0 for No:")
                    choice = int(input())
                    if choice == 1:
                        break
                    elif choice == 0:
                        print("Exiting...")
                        return
                    else:
                        print("Invalid input! Please enter either 1 or 0.")
                except ValueError:
                    print("Invalid input! Please enter an integer.")



if __name__ == "__main__":
    token_ring = TokenRing(5)
    token_ring.main()
