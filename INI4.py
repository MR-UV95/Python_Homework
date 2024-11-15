# Problem
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

#Code
## Given numbers are 4390, 9233
{
odd = 0
for num in range(4390, 9234):
    if num % 2 == 1:
            odd = odd + num
    
print (odd)
}
