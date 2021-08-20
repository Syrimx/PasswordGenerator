import time
from random import randint

def magic(n):
	solve = []

	for i in range(0,n):
		solve.append(chr(randint(41, 126)))

	solve = ''.join(solve)
	with open('keys+.txt' , 'a') as file:
		file.write(f'{solve} {time.ctime(time.time())}\n')

	return solve


if __name__ == '__main__':
	magic(12)