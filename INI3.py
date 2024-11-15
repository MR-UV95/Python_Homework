# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices athrough band cthrough d(with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

#creating a s list of 200 letters
{
    s = ("9wRYFSwXlYV7R6mmZeJKk3sAZuR4aC9xkE9WCvhmCharadriusmskrB0AaIXbBLTWyl1PMFrXt5QpyuLrQiQTLGWuRakoFgfvoiIWucDBYXRy61XXSt7Kw1Qn8hzeMQQGi0zO68L1XQjhm0b24cPKIZDfRqcouN7Kjnkw7hyHk4heliacaEtC7n91ZVR6mG")
}

# Splicing at a = 40, b = 49, c = 171 and d = 177 and showing output
{
    a = s[40:50]
    b = s[171:178]
    print (a,b)
}