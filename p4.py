ser_input=input("enter a list of integers_separated by_spaces:")
result=[]
for num in user_input.split():
    if int(num)>100:
        result.append('over')
    else:
      result.append(int(num))
print ("modified list",result)

