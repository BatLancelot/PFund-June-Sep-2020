import math

first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
student_count = int(input())

total_employee_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
time = student_count / total_employee_efficiency
employee_breaks = 0

for i in range(math.ceil(time)):
    student_count -= total_employee_efficiency
    if (i + 1) % 3 == 0:
        if student_count == 0:
            continue
        else:
            employee_breaks += 1

total_time = time + employee_breaks

print(f'Time needed: {math.ceil(total_time)}h.')
