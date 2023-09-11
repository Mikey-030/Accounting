#先做可以輸到txt，再想辦法弄到discord
import time

def writeIn(time, text):
    fout = open('money.txt', 'a')
    fout.write(time + ' ' + text + '\n')
    fout.close()

def main(selectedMode):
    if(selectedMode == 'w'):
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
    elif(selectedMode == 'r'):
        fin = open('money.txt')
        text = fin.readline()
        while(text is not None and text != ''):
            print(text, end='')
            text = fin.readline()
        fin.close()
    elif(selectedMode == 'i'):
        print("Mode w to write\nMode r to read records\nMode q to quit")    
    elif(selectedMode == 'q'):
        return 0
    else:
        print('Please select a valid mode')
        print('For further instruction press i')
        mode = str(input("Mode: "))
        main(mode)


mode = str(input("Mode: "))
main(mode)