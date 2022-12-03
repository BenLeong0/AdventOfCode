from time import sleep

card_public_key = 15113849
door_public_key = 4206373

def get_loop_size(public_key):
	key = 1
	loop_size = 0
	while key != public_key:
		loop_size += 1
		key *= 7
		key %= 20201227
	return loop_size


def get_encryption_key(public_key, loop_size):
	key = 1
	for _ in range(loop_size):
		key *= public_key
		key %= 20201227
	return key

card_loop_size = get_loop_size(card_public_key)
door_loop_size = get_loop_size(door_public_key)

print(get_encryption_key(door_public_key, card_loop_size))
