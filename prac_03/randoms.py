
import random


print(random.randint(5, 20))  # line 1


print(random.randrange(3, 10, 2))  # line 2

print(random.uniform(2.5, 5.5))  # line 3



# a random integer between 5 and 20.
# smallest would be 5 and largest would be 20
# a random integer chosen from 3, 5, 7, or 9.
# smallest would be 3 and largest would be 9.
# No it couldnt produce a 4, because the step is 2, so only odd numbers in that range are possible.
# a random floating point number between 2.5 and 5.5.
# smallest would be 2.5 and largest would be 5.5. However its not always guaranteed, since uniform picks from the range, usually floats close to 5.5.

