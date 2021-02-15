
#FIX PATHS AND RENAMING
#FILE NOT BECOMING A WORD DOCX
#CHECK IF WHEN FILE IS SAVED PRE-CORRUPTION, IF FILE IS DOCX
#TRY IGNORING THE WHOLE PATH SECTION TO SEE IF SELENIUM IS WORKING CORRECTLY







def main():
    
    print('=============================================================')
    print('')
    print(' ___        _______    ____________  ______     ____                               ')
    print('/   \      /       \   |______   __|  \    \   /   /                               ')
    print('|   |     |   __    |       /   /      \    \/    /                                ')
    print('|   |     |  [  ]   |      /   /        \       /                                  ')
    print('|   |     |   __    |     /   /          |     |                                   ')
    print('|   |__   |  /  \   |  _ /   /_____       |   |                                    ')
    print('\_______/ |__|   |__| |____________|      |___|    [AF]                            ')
    print('')

    print('=============================================================')

        
        
        

    print('\n W E L C O M E   T O   C Ø R R U P T E R . P Y')

    Possible_Options()
    
    



def Invalid_Option():
    os.system('clear')
    print('\n Invalid input! Please try again.')
    print('\n =============================================================')
    print('')
    sleep(0.5)
    Possible_Options()


def Possible_Options():
    print('\n What would you like to do?')
    for option in options:
        print('\n'+ '    -> ' + option)

    decision = input('\n$')
    with PixelSpinner('') as bar:
        for i in range(10):
            sleep(0.06)
            bar.next()
            
    Switch(decision.capitalize())



#Switches amongst possible cases
def Switch(key):    
    switcher={
        'Create corrupted file':Create_New_File,
        'Corrupt existing file':Corrupt_Existing_File,
        'Exit':Exit
        }

    func = switcher.get(key,lambda:Invalid_Option())
    func()
    
    


#Creates corrupted File
def Create_New_File():
    new_file_name = str(input('Enter file name: '))
    new_file = Document()
    new_file.add_heading(new_file_name, 0)
    new_file_path = documents_path + "/" + new_file_name
    new_file.save(new_file_path)

    print('File has been succesfully created!')

    corrupt = input('\nPress "Enter" to corrupt ' + "'" + new_file_name + "'")

    print("\nCorrupting the file located @ " + new_file_path)
    sleep(3)
    print("\nStarting irrersible corruption...")
    sleep(3)
    print("Press 'Ctrl/Command + Z' to cancel")

    count_down = 3
    for i in range(3):
        sleep(1.5)
        print(count_down)
        count_down -= 1

    y = threading.Thread(target=main_loop, args=(new_file_path,))
    y.start()

    
    print('\nFile has been succesfully corrupted!')
    print('File has been renamed to :')
    final_file_name = 'final_' + new_file_name
    init_path = os.path.expanduser('~/Documents/'+ new_file_name)
    final_path = os.path.expanduser('~/Documents/'+ final_file_name)
    os.rename(init_path, final_path)
    print('\n[ '+ final_file_name + ']')
    print('\nFile has been placed inside the  C Ø R R U P T   folder')
    print('\n=============================================================')
    

    restart = input('Press "Enter" to continue ')
    os.system('clear')
    main()

    
    
    
    


#Accesses usr files, finds File, and corrupts it.
def Corrupt_Existing_File():
    
    file_path = easygui.fileopenbox(filetypes = ['*.docx'])

    print("\nCorrupting the file located @ " + file_path)
    sleep(3)
    print("\nStarting irrersible corruption...")
    sleep(3)
    print("Press 'Ctrl/Command + Z' to cancel")

    count_down = 3
    for i in range(3):
        sleep(1.5)
        print(count_down)
        count_down -= 1
        
        
        
    x = threading.Thread(target=main_loop, args=(file_path,))
    x.start()

    print('\nFile has been succesfully corrupted!')
    print('File has been placed inside the  C Ø R R U P T   folder')
    print('\n=============================================================')
    

    restart = input('Press "Enter" to continue ')
    os.system('clear')
    main()
    

    
          
          
    
    
    
    
                    
   

#Closes Program
def Exit():
    print('\nShutting Down...')
    mytime = time.localtime()
    if mytime.tm_hour < 6 or mytime.tm_hour > 18:
        print('Have a good night!')
        print('')
    else:
        print('Have a good day!')
        print('')
    sleep(1)
    exit()






#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


import os,sys
import time
from time import sleep
from progress.spinner import PixelSpinner

import threading
import easygui
from headless import main_loop

from docx import Document
from docx.shared import Inches
    

options = ['Create corrupted file',
               'Corrupt existing file',
               'Exit',
               ]

documents_path = os.path.expanduser('~/Documents')
folder_path = os.path.expanduser('~/Documents/C Ø R R U P T/')



try:
    os.mkdir(folder_path)


    
except OSError:
    print('')
    print('            All requirements Satisfied...')
    print('')
    print('')
else:
    print("Satisfying Requirements")
    for i in range(3):
        print('.')
        sleep(1)


        

main()


