# """
# MODE
# 'r'     = Open File for reading [Read meode]
# 'w'     = Open File for writing [Write mode]
# 'x'     = Create file if not exits
# 'a'     = Add moe contant to the file
# mode in file
# 't'     = text mode
# 'b'     = Binary mode
# '+'     = read and write
 


# f = open('file_io1.txt','w')

# f.write('the try file input\n')
# f.write('the second line\n')
# f.write('the third line')

# print(a)
# f.close()"""
# '''
# f = open('file_io1.txt','r+')
# print(f.read())
# a=f.write('the try file input\n')
# print(a)
# f.close()
# f = open('file_io_2.text','rt')
# #f.write('the first line\n')
# #contant = f.read()
# for read in f:
#     print(read,end='')
# f.close()
# f = open('file_io_2.text','r+')
# # f.write('the new line\n')
# # print(f.tell())  # index number of my code
# print(f.readline())
# f.seek(7)

# print(f.readline())
# f.close()'''

# # f = open(file1.text,'w')
# # f.write('first line ')

# # f.close()1

f = open('Create_file.txt ' ,'r+')
f.write('I entered the first line \n')
f.write('I entered the second line \n')
f.write('I entered the third line \n')
d = f.read()
print(d)
f.close()

# f1 = open('Create_the_file.txt ','w') 
# for data in d:
#     f1.write(data)
# f1.close()
# f.close()


# #REMOVE FILE
# import os
# if os.path.exists('file_io1.txt'):
#     os.remove('file_io1.txt')
#     print('Sucess')
# else:
#     print('File does not exit')

# # Block of file

# with open ('file_io1.txt') as f:
#     a = f.readlines()
#     print(a) 