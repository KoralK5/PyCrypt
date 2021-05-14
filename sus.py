from os import listdir, remove, system
from time import sleep
from PIL import Image
import numpy as np
import random
import base64

def encode(image):
	random.seed(seed)
	for row in range(len(image)):
		for col in range(len(image[row])):
			for rgb in range(len(image[row][col])):
				image[row][col][rgb] += random.randrange(1, 255) % 256
	return image

def decode(image):
	random.seed(seed)
	for row in range(len(image)):
		for col in range(len(image[row])):
			for rgb in range(len(image[row][col])):
				image[row][col][rgb] -= random.randrange(1, 255)
				image[row][col][rgb] += (image[row][col][rgb] < 0) * 256
				image[row][col][rgb] %= 256
	return image

loc = input('Location: '); loc = 'D:\\Users\\Koral Kulacoglu\\Coding\\python\\LOL\\( ͡° ͜ʖ ͡°)\\'
seed = int(input('Seed: '))

while True:
	system('cls')
	dirs = listdir(loc)
	if int(input('Encode (0) | Show (1): ')):
		print('\nFiles:', [f'{row+1} - ' + dirs[row] for row in range(len(dirs))])
		choice = int(input('\nShow File (n) | Show Folder (0): '))

		if choice:
			try:
				sel = loc + dirs[choice-1]
				image = np.load(sel, allow_pickle=True)
				Image.fromarray(np.array(decode(list(image))), 'RGB').show()
			except:
				print('\nOperation Failed!\n')
				sleep(1)

		else:
			random.shuffle(dirs)
			for img in range(len(dirs)):
				try:
					sel = loc + dirs[img]
					image = np.load(sel, allow_pickle=True)
					curr = Image.fromarray(np.array(decode(list(image))), 'RGB')
					curr.show()
				except:
					print('\nOperation Failed!\n')
					sleep(1)
	
	else:
		print('\nFiles:', [f'{row+1} - ' + dirs[row] for row in range(len(dirs))])
		choice = int(input('\nEncode File (n) | Encode Folder (0): '))

		if choice:
			try:
				sel = loc + dirs[choice-1]
				image = Image.open(sel)
				image = encode(np.array(image))
				np.save(sel.split('.')[0], image)
				remove(sel)
			except:
				print('\nOperation Failed!\n')
				sleep(1)
		
		else:
			dirs = listdir(loc)
			print(f'\nEncoding {len(dirs)} Files:')

			for img in range(len(dirs)):
				try:
					sel = loc + dirs[img]
					image = Image.open(sel)
					image = encode(np.array(image))
					np.save(sel.split('.')[0], image)
					remove(sel)
					print('#', end='')
				except:
					print('x', end='')
			print()
			sleep(1)

