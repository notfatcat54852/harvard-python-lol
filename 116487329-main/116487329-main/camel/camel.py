input1 = input("prompt")
input1 = input1.strip()
output1 = ""
for element in input1:
    if element.isupper() and element != input1[0]:
        #print(element + " is upper")
        output1 += "_" + element.lower()
    else:
        output1 += element.lower()
print(output1)