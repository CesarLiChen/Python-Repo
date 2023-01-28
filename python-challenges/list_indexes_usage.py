# Given 10 inputs which will numbers from 1-10
# Store in a list.
# Only add numbers that between 3 and 7.
# No loops, comparison, or if statments.

print("Please input your 10 numbers")
input_1 = int(input())
input_2 = int(input())
input_3 = int(input())
input_4 = int(input())
input_5 = int(input())
input_6 = int(input())
input_7 = int(input())
input_8 = int(input())
input_9 = int(input())
input_10 = int(input())

# List below holds repetitions of each input
rep_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

rep_list[input_1] = rep_list[input_1] + 1
rep_list[input_2] = rep_list[input_2] + 1
rep_list[input_3] = rep_list[input_3] + 1
rep_list[input_4] = rep_list[input_4] + 1
rep_list[input_5] = rep_list[input_5] + 1
rep_list[input_6] = rep_list[input_6] + 1
rep_list[input_7] = rep_list[input_7] + 1
rep_list[input_8] = rep_list[input_8] + 1
rep_list[input_9] = rep_list[input_9] + 1
rep_list[input_10] = rep_list[input_10] + 1

print(rep_list)

total = (rep_list[3] * 3) + (rep_list[4] * 4) + (rep_list[5] * 5) + (rep_list[6] * 6) + (rep_list[7] * 7)
print(total)
