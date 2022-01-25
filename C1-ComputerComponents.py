from pandas import *
import pandas


class Computer:
    def __init__(self, Price, Usage, Type, OS):
        self.Price = Price
        self.Usage = Usage
        self.Type = Type
        self.OS = OS


global UsageList
UsageList = ['Light',"Medium","Intense","Gaming"]
global OSList
OSList = ['Ipad','Windows','Mac','Android','Linux','ChromeOS']
global PortabilityList
PortabilityList = ['Portable',"LessPortable","Desktop"]


def getUsage():
    Usage = int(input("\nWhat programs do you use? 1.Simple programs like web browsers and text editors\
    2.Programming IDE such as <visual studio Code> 3.Bigger programs like Video editing or 3D modeling 4.Modern Games"))
    return UsageList[Usage-1]
    
def getType():
    Portability = int(input("\nDo you need your computer to be portable to work on the go? 1. Very Portable 2.Bigger and heavier but still portable 3.Stationary"))
    return PortabilityList[Portability-1]

def getOS():
    Portability = int(input("\nWhat is your preferred operating system? 1. Windows 2.MacOS 3.IpadOS 4.Android"))
    return PortabilityList[Portability-1]

def FindMatch():
    pass

def main():
    MyType = Computer('','','','')
    
    while True:
        action = input("Choose what you want to do, enter a number(1. Enter your budget| 2.Select usage| 3.Select Form factor| 4.Select OS| 5.Get a recommendation): ")
        if action == '1':
            MyType.Price = int(input("\nEnter your budget: "))
        elif action == "2":
            MyType.Usage = getUsage()
        elif action == '3':
            MyType.Type = getType() 
        elif action == '4':
            MyType.OS = getOS()
        elif action == '5':
            FindMatch(MyType)


if __name__ == "__main__":
    main()