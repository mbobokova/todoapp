waiting_list = ['sen', 'ben', 'john']
waiting_list.sort()

for index, guest in enumerate(waiting_list):
    row = f"{index + 1}.{guest.capitalize()}"
    print(row)
