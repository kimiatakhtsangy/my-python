import base64

file = open("output.txt", "r")
flag = str(file.read())
file.close()


# latitude
# for i in range(34):
    # tmp = flag.encode("ascii")
    # message = base64.b64decode(tmp)
    # flag = message.decode("ascii")

# longitude
for i in range(48):
    tmp = flag.encode("ascii")
    message = base64.b64decode(tmp)
    flag = message.decode("ascii")

print("The CFT result is:\n")
print(flag)


fileoutput = open("secret_message.txt", "w")
fileoutput.writelines(flag)
fileoutput.close()
