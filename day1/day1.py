day1_input = open('day1/input.txt', 'r')
lines = day1_input.readlines()

answer = 0
line_val = 0
prev_line_val = 0

for line in lines:
    line_val = int(line)

    if line_val > prev_line_val:
        answer+=1
        
    prev_line_val = line_val

print(answer-1)