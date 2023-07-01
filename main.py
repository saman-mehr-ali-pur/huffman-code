import comperession as com
import DeCompression as decom


def file_stroge(path,content):
    file = open(path,'w')
    file.write(content)
    file.close


def file_reader(path):
    file = None
    try:
        file = open(path,'r')
    except FileNotFoundError:
        print("$$$")
        return False
    content = file.read()
    file.close()
    return content


def option_1():
    path=""
    content=""
    while(True):    
        print("please write absolute path your desired text file")
        path = input(">>> ")
        file=None
        content = file_reader(path)
        if content == False:
            print("there is no such this file :(")
            continue
        break

    file_name = path.split('/').pop().split('.')[0]
    compersed_content=com.compersor(content)
    file_stroge("result/"+file_name+".compressed",compersed_content[0])
    file_stroge("result/"+file_name+".key",compersed_content[1])
    






def option_2():
    key=None
    comperssed_input=None
    path=None
    while(True):    
        print("please write absolute path your compersed text file")
        path = input(">>> ")
        
        comperssed_input = file_reader(path)
        if path==False:
            print("there is no such this file :(")
            continue
        break


    while(True):    
        print("please write absolute path your key file")
        path = input(">>> ")
        
        key = file_reader(path)
        if key==False:
            print("there is no such this file :(")
            continue
        break




    print('result file name: ')
    file_name= input(">>> ")
    decomperssed_string = decom.decompresor(comperssed_input,key)
    file_stroge("result/"+file_name,decomperssed_string)










while(True):
    while(True):
        print("which one of this algorithm do you want to use?")
        print("1) commpersor")
        print("2) decommpersor")
        print("3) exit")

        x= input()
        if x.strip()=='1':
            option_1()


        if x.strip()=='2':
            option_2()

        if x.strip()=='3':
            exit(0)
        
        while(True):
            print("another task? (type n or NO for NO and y for YES)")
            x=input(">>> ")
            if x.strip()=="n":
                print("GOOD LUCK :)")
                exit(0)

            if x.strip()=='y':
                continue
            else:
                print("invalid input :(")

    break




