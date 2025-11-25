###
# Sums numbers entered by user
#
total_sum = 0
arytmetyczna = 0
l_liczb = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    l_liczb += 1

print(f"The total sum of the numbers is: {total_sum}")

if l_liczb >0:
    arytmetyczna = total_sum/l_liczb
    print(f"sednia arytmetyczna to: {arytmetyczna}")
