#simulate rolling a dice 10,000 times
from random import randint
r = [randint(1,6) for iter in range(10000)]
#plot histogram of rolls
import matplotlib.pyplot as plt
plt.hist(r,bins = 6)
#count and print number of times a number was rolled
r_counts = {}
for n in r:
    if n in r_counts:
        r_counts[n] += 1
    else:
        r_counts[n] = 1
print(*r_counts.items())
