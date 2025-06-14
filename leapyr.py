# month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

# def is_leap(year):
#     return year%4==0 and (year%100 != 0 or year%400 == 0)

# def days_inmonth(year,month):
#     if not 1<=month<=12:
#         return 'Invalid month'
#     if month==2 and is_leap(year):
#         return 29
    
#     return month_days[month]

# print(is_leap(2021))

# import random

# courses=['history','compsci','math','physics']
# random_course=random.choice(courses)

# print(random_course)

# import os 
# courses=['history','compsci','math','physics']
# print(os.getcwd())

# + os.getcwd()                                            => get current working directory
# + os.chdir(<path>)                                    => change directory 
# + os.listdir()	                                            => list directory
# + os.mkdir(<dirname>)                           => create a directory
# + os.makedirs(<dirname>)                    => make directories recursively
# + os.rmdir(<dirname>)	                   => remove directory
# + os.removedirs(<dirname>)                => remove directory recursively
# + os.rename(<from>, <to>)                   => rename file
# + os.stat(<filename>)                            => print all info of a file
# + os.walk(<path>)	                          => traverse directory recursively
# + os.environ		                                 => get environment variables
# + os.path.join(<path>, <file>)              => join path without worrying about /
# + os.path.basename(<filename>)     => get basename
# + os.path.dirname(<filename>)         => get dirname
# + os.path.exists(<path-to-file>)         => check if the path exists or not
# + os.path.splitext(<path-to-file>)      => split path and file extension
# + dir(os)			                               => check what methods exists
# import os
# os.mkdir('test')

import numpy as np 
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)