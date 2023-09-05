print("How high should I count? ")
max_number = int(input())

print("where should I start")
start_number = int(input())

print("what should I count by?")
count_by = int(input())

for number in range(start_number, max_number+1, count_by):
    print (number)
