input = input("prompt for input")
input = input.lower()
input = input.strip()

input = input[-4] + input[-3] + input[-2] + input[-1]
#input = input[-5] + input[-4] + input[-3] + input[-2] + input[-1]
if input == "jpeg":
    print("image/jpeg")
elif input == ".gif":
    print("image/gif")
elif input == ".jpg":
    print("image/jpeg")
elif input == ".png":
    print("image/png")
elif input == ".pdf":
    print("application/pdf")
elif input == ".txt":
    print("text/plain")
elif input == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")
#print(input)