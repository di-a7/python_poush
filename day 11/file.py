# file handling

# read mode('r') - if file does not exist, error is displayed
# open a file, open method takes 2 arguments filepath and mode
# f = open('D:/Teach/Poush/first.txt','r')
# a = f.read()
# print(a)
# f.close()

# write mode('w') - if file doesnot exist, new file is created, previous data is override
# f = open('D:/Teach/Poush/first.txt','w')
# f.write("Mindrisers")
# f.close()

#  append mode('a') - if file doesnot exist, new file is created, previous date xa vani new data is added to it
f = open('D:/Teach/Poush/first.txt','a')
f.write("hello world")
f.close()

# ask user (login or register)
# if register, ask for username and password, store username it in a file
# if login, ask for username and password, and check if the username exist in the file, if yes print login, if not print something