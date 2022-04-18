start_num = 0
n_list = []
index_num = int(input())

while len(n_list) != index_num:
  temp_str = str(start_num)
  if temp_str.find('666') == -1: 
    pass
  else:
    n_list.append(start_num)
  start_num +=1 

print(n_list[index_num-1])