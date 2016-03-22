import sys
import numpy as np
std_in = sys.stdin

def main():
    no_of_cases = int(std_in.readline())
    my_array = np.empty((19,500,2),object)

# w  e  l  c  o  m  e     t  o     c  o  d  e     j  a  m
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
    for n in range(no_of_cases):
        my_array[:] = 0
        input_line = std_in.readline()
        fill_array(my_array,input_line)
#        print(my_array)
        count_array(my_array)
#        print(my_array)
        result = 0
        for j in range(500):
            if my_array[18,j,0] != 0:
                result = my_array[18,j,1] + result
            else:
                break
#        print("result is " + str(result))
        result = result % 10000
        res = str(result)
        res = res.zfill(4)
        print("Case #" + str(n+1) + ": " + res)
            
def fill_array(arr,inp):
    input_len = len(inp)
    for ind in range(input_len):
        ch = inp[ind]
        if ch == 'w':
            for i in range(500):
                if arr[0,i,0] == 0:
                    arr[0,i,0] = ind+1
                    break
            continue
        elif ch == 'e':
            for i in range(500):
                if arr[1,i,0] == 0:
                    arr[1,i,0] = ind+1
                    break
            for i in range(500):
                if arr[6,i,0] == 0:
                    arr[6,i,0] = ind+1
                    break
            for i in range(500):
                if arr[14,i,0] == 0:
                    arr[14,i,0] = ind+1
                    break
            continue
        elif ch == 'l':
            for i in range(500):
                if arr[2,i,0] == 0:
                    arr[2,i,0] = ind+1
                    break
            continue
        elif ch == 'c':
            for i in range(500):
                if arr[3,i,0] == 0:
                    arr[3,i,0] = ind+1
                    break
            for i in range(500):
                if arr[11,i,0] == 0:
                    arr[11,i,0] = ind+1
                    break
            continue
# w  e  l  c  o  m  e     t  o     c  o  d  e     j  a  m
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
        elif ch == 'o':
            for i in range(500):
                if arr[4,i,0] == 0:
                    arr[4,i,0] = ind+1
                    break
            for i in range(500):
                if arr[9,i,0] == 0:
                    arr[9,i,0] = ind+1
                    break
            for i in range(500):
                if arr[12,i,0] == 0:
                    arr[12,i,0] = ind+1
                    break
            continue
        elif ch == 'm':
            for i in range(500):
                if arr[5,i,0] == 0:
                    arr[5,i,0] = ind+1
                    break
            for i in range(500):
                if arr[18,i,0] == 0:
                    arr[18,i,0] = ind+1
                    break
            continue
        elif ch == ' ':
# w  e  l  c  o  m  e     t  o     c  o  d  e     j  a  m
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
            for i in range(500):
                if arr[7,i,0] == 0:
                    arr[7,i,0] = ind+1
                    break
            for i in range(500):
                if arr[10,i,0] == 0:
                    arr[10,i,0] = ind+1
                    break
            for i in range(500):
                if arr[15,i,0] == 0:
                    arr[15,i,0] = ind+1
                    break
            continue
        elif ch == 't':
            for i in range(500):
                if arr[8,i,0] == 0:
                    arr[8,i,0] = ind+1
                    break
            continue
        elif ch == 'd':
            for i in range(500):
                if arr[13,i,0] == 0:
                    arr[13,i,0] = ind+1
                    break
            continue
        elif ch == 'j':
            for i in range(500):
                if arr[16,i,0] == 0:
                    arr[16,i,0] = ind+1
                    break
            continue
        elif ch == 'a':
            for i in range(500):
                if arr[17,i,0] == 0:
                    arr[17,i,0] = ind+1
                    break
            continue
        else:
            continue

def count_array(arr):
    for j in range(0,500):
        if arr[0,j,0] != 0:
            arr[0,j,1] = 1
        else:
            break
    for i in range(1,19):
        for j in range(500):
            curindex = arr[i,j,0]
            count = 0
            for prev_char_ind in range(0,500):
                if arr[i - 1,prev_char_ind,0] !=0:
                    if arr[i - 1,prev_char_ind,0] < curindex:
                        count = count + arr[i - 1, prev_char_ind,1]
                else:
                    break
            arr[i,j,1] = count

main()