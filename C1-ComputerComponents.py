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

ExplainDict = {
    "1":"The CPU is the 'Brain' of the computer and it's responsible for processing instructions and calculations\n\
A fast CPU means you computer can generally process information faster. A CPU is measured by it's frequency and how many processing cores it has\n\
A fast CPU should have speed above 2 Giga Hertz, and should have at least 6 cores to process multiple tasks simutaneously",
    "2":"The RAM is a vert fast short term memory that helps the CPU store temporary information. Ram's speed is measured in Mhz - how frequently it can be accessed\n\
And it's size is measured in Gigabytes. It's best to have RAM sizes of larger than 16GBs and faster than 2400MHz",
    "3":"Hard drives are different from RAM as they store permanent information, they are much larger but also much slower.\n\
There are two type of Hard drives, Hard Disk Drives, and Solid State Drives. Solid State drives are ,much faster but they're also\n\
more expensive at the same capacity. Depending on your use, you need for storage space ranges from 256GB ~ 2+ TB",
    "4":"Every Computer has a graphics card, they output graphics on to the display. A lot of CPUs have graphics cards integrated in them\n\
but there are dedicated graphics cards that are very fast at doing simple calculations that is important for tasks such as processing game graphics.",
    "5":"Motherboards used to carry information around to each component, but they don't too much specification differences other than build quality.\n\
Just make sure that your motherboard is compatible with all you components, expecially the CPU and the RAM"
}



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

def FindDesktopMatch(MyType):
    print("With desktops, you have a lot more opetions to customize the computer's specifications to your usage")
    print("We'll recommend a few combinations of hardware however you can match these however you want")
    

def FindPortableMatch(MyType):
    if UsageList[MyType.Usage-1] == "Desktop":
        FindDesktopMatch(MyType)
    matchingList = []
    recommendlist = []
    if MyType.OS != '':
        myFile = pandas.read_excel(MyType.OS)
    else:
        myFile = pandas.read_excel("Recommendation.xlsx")

    infoList = []
    infoList.append("Since you only do light tasks such as web browsing. Most computer today can handle it just fine, so we chose something most fitting to your budget and size")
    infoList.append("Many laptops fit your use case, most computers that have a recent cpu with more than 4 cores can handle the tasks you will give it, and 8GBs of RAM would be enough, we choses one most fitting to your price and form factor")      
    infoList.append("You use your computer for intense tasks, so you would need a fast processor with 6 cores or more.You would also need at least 16GBs of memories in order to store large amounts of temporary informataion.")

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
    Part = input("Which part of the computer do you want to learn about? 1.CPU 2.RAM 3.Storage 4.GPU 5.Motherboard 6.PSU(desktop only)")
    
    
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
            FindPortableMatch(MyType)
        elif action == '6':
            Explain()
        else:
            break


if __name__ == "__main__":
    main()