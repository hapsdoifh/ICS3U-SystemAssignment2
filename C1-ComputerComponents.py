from asyncio.windows_events import INFINITE
from copy import deepcopy
from pandas import *
import pandas
import numpy
import webbrowser

class Computer:
    def __init__(self, Price, Usage, Type, OS):
        self.Price = Price
        self.Usage = Usage
        self.portable = Type
        self.OS = OS


global UsageList
UsageList = [0,2.5,5.5,9]
global OSList
OSList = ['Apple.xlsx','WindowsLaptop.xlsx"','Apple.xlsx','Android','Linux','Chromebooks.xlsx']
global PortabilityList
PortabilityList = [0,2.5,4.5,7,'Desktop']


def getUsage():
    Usage = int(input("\nWhat programs do you use? 1.Simple programs like web browsers and text editors\
    2.Programming IDE such as <visual studio Code> 4.Modern Games: 3.Large programs like Video editing or 3D modeling: "))
    return Usage
    
def getType():
    Portability = int(input("\nDo you need your computer to be portable to work on the go? 1. Extremely small and light 2.Bigger but still portable 3. Big and Heavy 4.Desktop: "))
    return Portability

def getOS():
    Portability = int(input("\nWhat is your preferred operating system? 1. Windows 2.MacOS 3.IpadOS 4.Android: "))
    return PortabilityList[Portability-1]

def FindMatch(MyType):
    matchingList = []
    recommendlist = []
    if MyType.OS != '':
        myFile = pandas.read_excel(MyType.OS)
    else:
        myFile = pandas.read_excel("Recommendation.xlsx")

    infoList = []
    infoList.append("For your usage, you put light usage such as web browsing. Most computer today can handle it just fine, so we chose something most fitting to your budget and size")
    infoList.append("Many laptops fit your use case, most computers that have a recent cpu with more than 4 cores can handle the tasks you will give it, and 8GBs of RAM would be enough, we choses one most fitting to your price and form factor")      
    infoList.append("For your usage, you have chosen intense, for this type of usage, you would need a fast processor with 6 cores or more.You would also need at least 16GBs of memories in order to store large amounts of temporary informataion.")

    ConvertedFile = myFile.to_numpy()
    for y in range(len(ConvertedFile)):
        if not pandas.isnull(ConvertedFile[y][0]):
            if float(UsageList[MyType.Usage-1]) <= float(ConvertedFile[y][4]) <= float(UsageList[MyType.Usage]): #matches usage type to performance
                if float(ConvertedFile[y][3])<=PortabilityList[MyType.Usage]: #Match portability
                    matchingList.append([ConvertedFile[y][0],ConvertedFile[y][1],ConvertedFile[y][2]])                
    print(infoList[MyType.Usage-1])
    print()

    for i in range(4):
        min = INFINITE 
        for index, item in enumerate(matchingList):
            if int(item[1]) < min:
                min = int(item[1])
                minstore = item
        temp = deepcopy(minstore)
        recommendlist.append(temp)
        if len(matchingList)>0:
            matchingList.remove(minstore)
    for i in recommendlist:
        print(i)                
    print()

def Explain():
    pass


def main():
    MyType = Computer('',0,0,'')
    while True:
        action = input("Choose what you want to do, enter a number(1. Enter your budget| 2.Select usage| 3.Select Form factor| 4.Select OS| 5.Get a recommendation|6. Learn more about computer and their components): ")
        if action == '1':
            MyType.Price = int(input("\nEnter your budget: "))
        elif action == "2":
            MyType.Usage = getUsage()
        elif action == '3':
            MyType.portable = getType() 
        elif action == '4':
            MyType.OS = getOS()
        elif action == '5':
            FindMatch(MyType)
        elif action == '6':
            Explain()
        else:
            break


if __name__ == "__main__":
    main()