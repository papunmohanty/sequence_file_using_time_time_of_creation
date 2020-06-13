"""
Date format used(take the pattern from the 
expression `time.ctime(os.path.getmtime(file))`)
Example:
for          - 'Fri Jun 12 01:10:35 2020' 
pattern used - '%a %b %d %H:%M:%S %Y'
"""


import datetime
import os
import time 

def sort_file_using_old_to_new():
    files_time = []
    
    format = '%a %b %d %H:%M:%S %Y' # The Datetime format    

    for file in os.listdir():
        file_creation_time = time.ctime(os.path.getmtime(file))
        formated_date = datetime.datetime.strptime(file_creation_time, format)
        files_time.append((file, formated_date))
    
    sorted_files = sorted(files_time, key=lambda x:x[1])
    final_sort = [file[0] for file in sorted_files]
    return final_sort


def numbering_files_old_to_new():
    sorted_files = sort_file_using_old_to_new()
    
    for index_num, file_name in enumerate(sorted_files):
        os.rename(file_name, str(index_num+1)+ "_" + file_name)

numbering_files_old_to_new()
