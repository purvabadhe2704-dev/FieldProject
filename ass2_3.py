# Program 3: Calculate total and average marks
marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
average = total / 5

print("Total Marks:", total)
print("Average Marks:", average)
