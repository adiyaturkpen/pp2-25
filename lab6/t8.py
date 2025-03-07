l=["frog1", "frog2", "frog3", "frog4", "frog5"]
file = open("output.txt", "w")  
for i in l:
    file.write(i+"\n")  
file.close()

