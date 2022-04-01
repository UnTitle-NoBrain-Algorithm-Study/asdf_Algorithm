def solution(s):
    
    num_list = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for n in range (10):
      k = str(n)
      s = s.replace(num_list[n], k)


    answer = int(s)
    return answer