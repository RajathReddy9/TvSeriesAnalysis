# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
for _ in range(16504):
	value = randint(500000, 1500000)
	print(value)