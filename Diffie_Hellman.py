import sys


class Diffie_Hellman:

    def __init__(self):
        self.q = 0
        self.alpha = 0
        self.Xa = 0
        self.Xb = 0
        self.Ya = 0
        self.Yb = 0
        self.k1 = 0
        self.k2 = 0

    def CheckPrime(self):
        for i in range(2, self.q, 1):
            if self.q % i == 0:
                print("Enter Number Is Not Prime !")
                exit()

    def CheckAplha(self):
        l1 = list()
        j = 0
        if self.alpha < self.q:
            for i in range(1, self.q, 1):
                l1.append(pow(self.alpha, i, self.q))
            l1.sort()

            if len(l1) == self.q - 1:
                for i in range(1, self.q, 1):
                    if i != l1[j]:
                        print("Entered Alpha Value Is Not An Primitive Root Of q")
                        exit()
                    else:
                        j += 1
                print("Entered Alpha Value Is Primitive Root Of q please proceed further !\n")
            else:
                print("Entered Alpha Value Is Not An Primitive Root Of q")
                exit()
        else:
            print("Alpha Value Should Be Less Than Value Of q !")
            exit()

    def FindPublicKey(self):
        if self.Xa < self.q and self.Xa != self.alpha:
            if self.Xb < self.q and self.Xb != self.alpha and self.Xb != self.Xa:
                self.Ya = pow(self.alpha, self.Xa, self.q)
                self.Yb = pow(self.alpha, self.Xb, self.q)
            else:
                print("Value of Private Key Xb should be less than q and not equal to value of Alpha & value of Xa !")
                exit()
        else:
            print("Value of Private Key Xa should be less than q and not equal to value of Alpha !")
            exit()

    def DisplayKeys(self):
        print("Values Used in algorithm are: -")

        print("Value of 'q' is: -", self.q)
        print("Value of Alpha is: -", self.alpha)
        print("Private key of 'A' i.e. 'Xa' = ", self.Xa)
        print("Public key of 'A' i.e. 'Ya' = ", self.Ya)
        print("Private key of 'B' i.e. 'Xb' = ", self.Xb)
        print("Public key of 'B' i.e. 'Ya' = ", self.Yb, "\n")

    def FindSecretKeys(self):
        print("Let k1 = Person 'A' & k2 = Person 'B'")
        print("If k1=k2 then key exchange will be successfully done !\n")
        self.k1 = pow(self.Yb, self.Xa, self.q)
        self.k2 = pow(self.Ya, self.Xb, self.q)
        print('Secret key for the k1 is: - ', self.k1)
        print('Secret Key for the k2 is: - ', self.k2, "\n")

        if self.k1 == self.k2:
            print("The value of k1 & k2 is {} & {} therefore key exchange done successfully !".format(self.k1, self.k2))
        else:
            print("The value of k1 & k2 is {} & {} therefore key exchange failed !".format(self.k1, self.k2))

    def AcceptValues(self):
        
        print("Application name: - ", sys.argv[0])

        if len(sys.argv) == 2:
            if sys.argv[1] == '-h' or sys.argv[1] == '-H':
                print("This script is of Diffie Hellman Algorithm")
                exit()

            if sys.argv[1] == '-u' or sys.argv[1] == '-U':
                print("Usage: - Application Name 'Diffie Hellman Algorithm'")
                exit()

        if len(sys.argv) != 5:
            print("Error: - Invalid number of arguments")
            exit()

        try:
            self.q = int(sys.argv[1])
            self.alpha = int(sys.argv[2])
            self.Xa = int(sys.argv[3])
            self.Xb = int(sys.argv[4])
        except ValueError:
            print("Error: - Invalid datatype of input")
        except Exception as e:
            print("Error : Invalid input", e)


def main():

    Obj = Diffie_Hellman()
    Obj.AcceptValues()
    Obj.CheckPrime()
    Obj.CheckAplha()
    Obj.FindPublicKey()
    Obj.DisplayKeys()
    Obj.FindSecretKeys()


if __name__ == "__main__":
    main()
