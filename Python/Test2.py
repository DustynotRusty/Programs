f1=open('some_file1.txt','r+')
f2=open('some_file2.txt','r+')
f1.write('Hello world')
f2.write('Hello world')

file1=f1.readline()
file2=f2.readline()
for line1 in file1:
    for line2 in file1:
        if line1==line2:
            print('Files are same')
            break
f1.close()
f2.close()