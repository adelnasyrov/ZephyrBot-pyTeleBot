stroka = input()
new_list = []
while len(stroka)>1:
    new_list.append("@" + stroka)
    stroka = input()
print("\n".join(new_list))