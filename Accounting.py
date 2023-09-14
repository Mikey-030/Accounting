#先做可以輸到txt，再想辦法弄到discord
import time
def runCode():
    mode = str(input("Mode: "))
    main(mode)

def sortTypeA(str):
    if(len(str)==4):
        fin = open('record.txt', 'r', encoding='utf-8')
        text = fin.readline()
        while(text is not None and text != ''):
            if(text[:4]==str[:4]):
                print(text, end='')
            elif(int(text[:4])>int(str[:4])):
                fin.close()
                return 0
            text = fin.readline()
        fin.close()
    elif(len(str)==7):
        fin = open('record.txt', 'r', encoding='utf-8')
        text = fin.readline()
        while(text is not None and text != ''):
            if(text[:7]==str[:7]):
                print(text, end='')
            elif(int(text[:4])>int(str[:4]) or (text[:4]==str[:4] and int(text[5:7])>int(str[5:7]))):
                fin.close()
                return 0
            text = fin.readline()
        fin.close()
    elif(len(str)==10):
        fin = open('record.txt', 'r', encoding='utf-8')
        text = fin.readline()
        while(text is not None and text != ''):
            if(text[:10]==str[:10]):
                print(text, end='')
            elif((text[:7]==str[:7] and int(text[8:10])>int(str[8:10])) or (text[:4]==str[:4] and int(text[5:7])>int(str[5:7])) or (int(text[:4])>int(str[:4]))):
                fin.close()
                return 0
            text = fin.readline()
        fin.close()
    else:
        print('你輸的時間怪怪的怪怪的')

def sortTypeB(str):
    print('Fuction unfinished yet, please wait.')


def writeIn(time, text):
    fout = open('record.txt', 'a', encoding='utf-8')
    fout.write(time + ' ' + text + '\n')
    fout.close()

def readRecord():
    fin = open('record.txt', 'r', encoding='utf-8')
    text = fin.readline()
    while(text is not None and text != ''):
        print(text, end='')
        text = fin.readline()
    fin.close()
    

def main(selectedMode):
    match selectedMode:
        case 'w':
            reps = input('How many pieces of information do you want to enter? ')
            while(not reps.isnumeric()):
                reps = input('Please enter a number: ')
            reps = int(reps)
            for i in range(reps):
                preinfo = str(input('Please enter the information by the order of name, class and price: '))
                preinfo = preinfo.replace(',',' ')
                info = str(preinfo.split(' '))
                localTime = time.localtime()
                date = time.strftime("%Y-%m-%d", localTime)
                writeIn(date, info)

        case 'r':
            readRecord()

        case 'q':
            return 0

        case 's':
            searchType = input('Press t to search by time; Press c to search by categories\nMode: s -> ')
            match searchType:
                case 't':
                    searchDate = input('When? ')
                    sortTypeA(searchDate)
                case 'c':
                    searchCategories = input('Category: ')
                    sortTypeB(searchCategories)
                case _:
                    print('Wrong type')

        case _:
            print('Please select a valid mode')
            print('For further instruction press i')
            runCode()

print("Press w to write, r to read records, s to search, q to quit.")
runCode()

#report bug to me