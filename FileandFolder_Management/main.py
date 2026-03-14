from pathlib import Path
import shutil

def create_folder():
    try:
        name=input("Please tell your folder name :-")
        p=Path(name)
        p.mkdir()
        print("folder created successfully")
    except Exception as err:
        print("sorry some error occured",err)

def read_file_folder():
    try:
        p=Path('')
        items=list(p.rglob('*'))
        for i , v in enumerate(items):
            print(f"{i+1} : {v}") 
    except Exception as err:
        print("error occur",err)
def update_folder():
    try:
        read_file_folder()
        old_name=input("Which folder u want to update :-")
        p=Path(old_name)
        if p.exists() and p.is_dir():
            new_name=input("please enter new folder name")
            new_p=Path(new_name)
            p.rename(new_p)
            print("your folder name is sucessfully created")
        else:
            print("sorry no such folder exist") 
    except Exception as err:
        print("error ocureed ",err)
def delete_folder():
    try:
        read_file_folder()
        name=input("please tell which folder u want to delete : ")
        p=Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("folder deleted sucessfully")
        else:
            print("no such folder exist")
    except Exception as err:
        print("error occured",err)
def create_file():
    try:
        read_file_folder()
        name=input("please tell your file name : ")
        p=Path(name)
        if not p.exists():
            with open(name,'w')as fs:
                data=input("write what you want in this file ")
                fs.write(data)
                print("file created succesfully")
        else:
            print("file already exists")   
    except Exception as err:
        print("error ocurred",err)

def  read_file():
    try:
        read_file_folder()
        name=input("please enter which file u want to read  :  ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open (name,'r')as fs:
                content=fs.read()
                print("your file content is -  ",content)
        else:
            print("NO such file exists")
    except Exception as err:
        print("error occured ",err)

def update_file():
    try:
        read_file_folder()
        name=input("Please tell your file name : ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("1 , renaming the file")
            print("2 ,Apeending something in file")
            print("3 ,for overwriting the file content")
            choice=int(input("tell your choice"))
            if choice==1:
                new_name=input("tell me your new name with extension")
                new_p=Path(new_name)
                if not new_p.exists() :
                    p.rename(new_name)
                    print("file created successfully")
                else:
                    print("sorry this name already exist")
            if choice ==2:
                with open(name,'a') as fs:
                    data=input("what u want to append")
                    fs.write(" "+data)
                    print("file appended successfully")
            if choice ==3:
                with open(name,'w') as fs:
                    data=input("what u want to overwrite")
                    fs.write(data)
                    print("file changed successfully")
    except Exception as err:
        print(f"error occured  {err}")  
def delete_file():
    try:
        read_file_folder()
        name=input("tell your file name with extension : ")
        p=Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("file deleted successfully")
        else:
            print("NO such file exist")
    except Exception as err:
        print(f"error occured {err}")
while True:
    print("Options : - ")
    print("1 , Create Folder")
    print("2 , Read Files and Folders")
    print("3 ,  Update The Folder")
    print("4 , Delete the Folder")
    print("5 , create a file")
    print("6 , read a file")
    print("7 , update a file")
    print("8 , Delete a file")
    print("0 , enter 0 to exit the program ")

    choice=int(input("Please Choose Your Option :   "))

    if (choice == 1):
        create_folder()
    if (choice==2):
        read_file_folder()
    if (choice==3):
        update_folder()
    if (choice==4):
        delete_folder()
    if (choice ==5):
        create_file()
    if (choice ==6):
        read_file()
    if (choice ==7):
        update_file()
    if (choice ==8):
        delete_file()
    if choice==0:
        break


