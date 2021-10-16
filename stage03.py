with open("artifacts.txt","r") as f:
    text1=f.read()

with open("artifacts02.txt","w") as f:
    text1=f.write(text1 + "added lines")
print("end of stage 02")