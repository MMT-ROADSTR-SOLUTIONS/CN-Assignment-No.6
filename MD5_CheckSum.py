import os
import sys
import hashlib


class CheckSum:

    def __init__(self):
        self.FileName = ""
        self.Buffer = 1024

    def CalculateCheckSum(self, path):
        try:
            fd = open(path, 'rb')
            hasher = hashlib.md5()
            Data = fd.read(self.Buffer)
            while len(Data) > 0:
                hasher.update(Data)
                Data = fd.read(self.Buffer)
            fd.close()
        except Exception as e:
            print("Error: -", e)

        return hasher.hexdigest()

    def CheckPath(self):
        flag = os.path.isabs(self.FileName)
        if not flag:
            path = os.path.abspath(self.FileName)
        else:
            path = self.FileName

        if os.path.exists(path):
            iRet = self.CalculateCheckSum(path)
            print("MD5 CheckSum of data from '{}' is {}".format(self.FileName, iRet))
        else:
            print("Error: - File Not Found !")

    def AcceptInput(self):
        
        print("Application name: - ", sys.argv[0])

        if len(sys.argv) != 2:
            print("Error: - Invalid number of arguments")
            exit()

        if sys.argv[1] == '-h' or sys.argv[1] == '-H':
            print("This script is used to traverse specific directory and display checksum of Specified file")
            exit()

        if sys.argv[1] == '-u' or sys.argv[1] == '-U':
            print("Usage: - Application Name 'CheckSum Generator'")
            exit()

        try:
            self.FileName = sys.argv[1]
            self.CheckPath()
        except ValueError:
            print("Error: - Invalid datatype of input")
        except Exception as e:
            print("Error : -", e)


def main():
    Obj = CheckSum()
    Obj.AcceptInput()


if __name__ == "__main__":
    main()
