import os
import subprocess 
import time
from time import sleep
from progress.spinner import MoonSpinner





def search_and_destroy():

    decision = ''

    while 'y' not in decision:

        target = input('Which subprocess are you looking for?: ')

        final_decision = input('Are you looking for subprocesses related to ' + str(target) + '?(yes/no): ')

        if 'yes' == final_decision:
            decision = 'y'
            sleep(2)

        if 'no' == final_decision:
            os.system('clear')

        if 'n' not in final_decision and 'y' not in final_decision:
            print('Invalid argument!')
            print('Please try again...')
            sleep(2)
            os.system('clear')

    with MoonSpinner('Looking for subprocesses related to '+ str(target) + ' ') as bar:
        for i in range(100):
            time.sleep(0.06)
            bar.next()



    subprocess_targets = []
    processes = os.popen('ps -ax').readlines()

    for line in processes:
        
        if target in line.lower():
            subprocess_targets.append(line)

    if len(subprocess_targets) < 1:

        print('------------------------------------------')
        print('NO ACTIVE SUBPROCESSES RELATED TO TARGET')
        print('------------------------------------------')

        print('\nPlease try again!')
        search_and_destroy()


    else:
        print('------------------------------------------')
        print('ACTIVE SUBPROCESSES RELATED TO TARGET')
        print('------------------------------------------')
        
          

    id_list = []
    for item in subprocess_targets:
        
        index = item.find('?')
        index -= 1
        item_id = item[:index]
        id_list.append(item_id)


        print(item)
        


    kill = str(input('Would you like to kill a subprocess?(yes/no/all): '))


    killing = True
    while killing:

        if 'y' in kill:
            kill_target = int(input('Which subprocess would you like to kill?: '))
            print('Would you like to kill ' + str(kill_target) + '?')

            confirm_kill = str(input('(yes/no):'))

            if 'ye' in confirm_kill:

                try:
                    kill_command = 'kill ' + str(kill_target)
                    os.system(kill_command)
                    sleep(1)
                    print('\n kill confirmed.')
                    killing = False
                except SystemError:
                    print('Subprocess not active or does not exist!')


            if 'no' in confirm_kill:
                pass

        if 'all' in kill:

            confirm_kill = str(input('Would you like to kill all subprocesses related to ' + str(target) + '?(yes/no): '))
            kill_count = 0

            if 'ye' in confirm_kill:

                for item in id_list:

                    try:
                
                        kill_command = 'kill ' + str(item)
                        os.system(kill_command)
                        print('\n kill confirmed.')
                        kill_count += 1
                    except OSError as err:
                        print("OS error: {0}".format(err))

                        
                    

                        

                print('\n['+str(kill_count)+' kills confirmed]')
                killing = False


            if 'no' in confirm_kill:
                    pass
                    

            if 'y' not in confirm_kill and 'n' not in confirm_kill:

                print('Invalid input!')
                print('Please try again...')
                print('x')


        if 'n' in kill:

            print('0.K')
            print('Have a good day!')
            killing = False
            exit()

        if 'n' not in kill and 'y' not in kill and 'a' not in kill:
            print('Invalid input!')
            print('Please try again...')







    




os.system('clear')
print('')
print('--------------------------------------------------')

print('         _____')
print('        |K .  | _____')
print('        | /.\ ||I ^  | _____')
print('        |(_._)|| / \ ||L _  | _____')
print('        |  |  || \ / || ( ) ||L_ _ |')
print("        |S____||  .  ||(_'_)||( v )|")
print("               |U____||  |  || \ / |")
print("                      |B____||  .  |")
print("                             |P____|")
print("                                                             JC")
print('--------------------------------------------------')




search_and_destroy()