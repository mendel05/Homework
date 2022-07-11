# import os.path
#
# def mkd():
#     new_dir = 'my_project'
#     if not os.path.exists(new_dir):
#         os.mkdir(new_dir)
#         os.chdir(new_dir)
#         if not os.path.exists('settings'):
#             os.mkdir('settings')
#         if not os.path.exists('mainapp'):
#             os.mkdir('mainapp')
#         if not os.path.exists('adminapp'):
#             os.mkdir('adminapp')
#         if not os.path.exists('authapp'):
#             os.mkdir('authapp')
#
#
# mkd()



import os
import random

if not os.path.exists('my_dir'):
    os.mkdir('my_dir')
os.chdir('my_dir')

for i in range(50+1):
    with open (f'{i}.txt', 'w', encoding='utf-8') as f:
        f.write(f'число равно {random.randint(0, 100) ** random.randint(0, 10000)}')

my_dict = {
    3000: 0,
    5000: 0,
    10000: 0,
    'more': 0
}


for i in os.listdir(os.getcwd()):
    f_size = os.stat(i)
    if 0<= f_size.st_size < 3000:
        my_dict[3000] += 1
    elif 3000<= f_size.st_size < 5000:
        my_dict[5000] += 1
    elif 5000<= f_size.st_size < 10000:
        my_dict[10000] += 1
    else:
        my_dict['more'] += 1


print(my_dict)