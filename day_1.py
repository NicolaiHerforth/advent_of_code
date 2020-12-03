file_name = input(f'What is your advent day 1 file name without extension? (file has to be .txt in the data folder) \n')
items = []
with open(f"data/{file_name}.txt") as file:
    for line in file:
        line = int(line.strip('\n'))
        items.append(line)
two_sum, three_sum = 0,0

for i in range(len(items)-1):
    for j in range(1,len(items)):
        if items[i] + items[j] == 2020:
            two_sum = items[i] * items[j]
        for k in range(2, len(items)):
            if items[i] + items[j] + items[k] == 2020:
                three_sum = items[i]*items[j]*items[k]

print(str(two_sum), '\n' + str(three_sum))