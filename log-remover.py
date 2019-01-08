#Sort through all files in the current directory and remove (delete) all log files from 2016 and 2017

import os, time

current_dir = os.path.dirname(os.path.realpath(__file__))

print(current_dir)

all_files = (os.listdir(current_dir))

print('Current files in dir: ')
print(all_files)


for fl in all_files:

        if fl.startswith('error_log-2017'):
                print('Deleting file ', fl)
                os.remove(fl)
                time.sleep(3)
        elif fl.startswith('error_log-2016'):
                print('Deleting file, ', fl)
                os.remove(fl)
                time.sleep(3)
        else:
                continue
