import random

dim_size = 10

pos = random.randint(0, dim_size ** 2 - 1)
row = pos // dim_size
col = pos % dim_size
print(pos, row, col)
