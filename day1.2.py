"""part 2 for AOC '23
https://adventofcode.com/2023/day/1#part2
"""


import re
from functools import reduce
input = list(open('day1.2.txt','r'))
# print(((input)))
input = [i.replace("\n", "") for i in input] #get rid of \n formatting

def find_occurrences(string, substring):
    return [i for i in range(len(string)) if string.startswith(substring, i)]
def getNums(input):
    numsLetters = {'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    allNumsLetters = list(numsLetters.keys())
    allNumsInt = list(numsLetters.values())
    numbers = []
    for i in range(len(input)):
        newStr = ''
        print("\n_________ original string: ", i, input[i], "_________")
        for n in range(len(allNumsLetters)):
            countNum = input[i].count(allNumsLetters[n])
            # print(allNumsLetters[n], input[i])
            indices = find_occurrences(input[i], allNumsLetters[n])
            if countNum > 0:
                for index in indices:
                    #count number of occurrences:
                    # turn into an int 
                    #find substring index \
                    # print("str looking at: ", input[i], (n)+1 , allNumsLetters[n])
                    # print(" word index: ",wordIndex,  input[i][wordIndex])
                    input[i] = input[i][:index+1]+ str(allNumsInt[n]) + input[i][index+1:]
                    print('added num: ', input[i])
                    # input[i]= input[i].replace(input[i][wordIndex], str(allNumsInt[n]))  #change this to change only allNUmsInt
                    # print("new changed str: ", input[i])
                    # else:
                        #iterate through char for num
                    # countNum -= 1
        for char in range(len(input[i])):#iterate through string
            if input[i][char].isdigit():
                # continue
                print("digit found:", input[i][char])
                newStr += input[i][char]
                input[i] += input[i][char]
                
                # input[i][char] = input[i][char].replace(input[i][char], '') 
        # input[i] = newStr
        print('new input: ', input[i], newStr)
        numbers.append((newStr))
    # print(numbers, len(numbers))
    total = 0
    # print(len(numbers))
    for i in range(len(numbers)):
        all = list(numbers[i])
        combined =  str(all[0] + all[len(all)-1])
        # print(all, all[0], all[len(all)-1], 'combined nums: ', combined)
        total += int(combined)
    print(total)
        
    
  
print(getNums(input))

