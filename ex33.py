# This is the thirty-third exercise.
# Date: 2014-06-23

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

def loop_test(n):
    """Adds numbers to a list until n."""
    i = 0
    container = []
    while i < n:
        # print "Adding %d to the list." % i
        container.append(i)
        i += 1
    return container

counter = int(raw_input("How many numbers do you want to put in the list? "))
increment = int(raw_input("In what increments do you want to put numbers in the list? "))

print "The list: ", loop_test(counter)

def smart_loop(end, inc):
    """Adds numbers to a list until end with inc increments."""
    container = []
    for i in range(0,end,inc):
        container.append(i+1)
    return container

print "The smart list: ", smart_loop(counter, increment)