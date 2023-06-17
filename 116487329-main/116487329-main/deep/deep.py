input = input("hello")
input = input.lower()
if input.find("forty") >= 0 and input.find("two") >= 0 or input.find("42") >= 0:
    print("Yes")
else:
    print("No")