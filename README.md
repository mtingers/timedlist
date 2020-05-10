# timedlist

A self-pruning list based off of time. Items are removed when their age is greater than the max time specified.

# Examples

```python
import time
from timedlist import TimedList

# Create a TimedList object that will remove items older than 10 seconds within
# 3% of maxtime
tl1 = TimedList(maxtime=10, filled_percent=3.0)
tl2 = TimedList(maxtime=10, filled_percent=3.0)

for i in range(20):
    tl1.append(time.time(), i)
    time.sleep(0.75)
    print('tl1: len:{} is_filled:{} elapsed:{}'.format(len(tl1), tl1.is_filled, tl1.elapsed))
    time.sleep(0.1)
    tl2.append(time.time(), i*10)

for i in range(20):
    tl2.append(time.time(), i)
    time.sleep(0.1)
    print('tl2: len:{} is_filled:{} elapsed:{}'.format(len(tl2), tl2.is_filled, tl2.elapsed))

# Delete like a normal list
del(tl1[0])

# Access with helper methods or index
print('first item example 1: {}'.format(tl1[0]))
print('first item example 2: {} {}'.format(tl1.get_time(0), tl1.get_item(0)))


# loop over all items
for i in tl1:
    print('loop: {}'.format(i))

# Prune back to a smaller list manually
print('len-before: {}'.format(len(tl1)))
tl1.prune(maxtime=5)
print('len-after: {}'.format(len(tl1)))


# Combine two TimedList
# This can only be done if the right hand's
# end time is > the left hand's end time
combined_tl = tl1 + tl2
print('len-combined: {}'.format(len(combined_tl)))

# reverse in place
combined_tl.reverse()
for i in combined_tl:
    print('combined_tl: loop-after-reverse: {}'.format(i))

# same as a list's clear()
tl1.clear()
print('len-after-clear: {}'.format(len(tl1)))

# there is no sort (exception is raised)
# tl1.sort()

# __str__/__repr__ example
print(tl2)
```
