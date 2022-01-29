# the continue statement if we want to skip the execution of for loop for specific condition
#nums = [1, 2, -3, 4, -5, 6]
#sum_positives = 0
#for num in nums:
    #if num<0:
        #continue
    #sum_positives += num
    #print(f'sum of positive numbers : {sum_positives}')
# python for loop with an else block
def print_sum_even_nums(even_nums):
    total = 0
    for x in even_nums:
        if x%2 != 0:
            break
        total +=x
        else:
            print("for loop executed normally")
            print(f'sum of numbers,{total}')









