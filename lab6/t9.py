file1 = open("C:\Users\Lenovo\pp2\pp2-spring-1\file1.txt", "r")  
file2 = open("file2.txt", "w")  
file2.write(file1.read())  
file1.close()  
file2.close()  