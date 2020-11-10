"""
To achieve this, begin with a list of numbers from 0 to 255, a current position which begins at 0 (the first element in the list), a skip size (which starts at 0), and a sequence of lengths (your puzzle input). Then, for each length:

Reverse the order of that length of elements in the list, starting with the element at the current position.
Move the current position forward by that length plus the skip size.
Increase the skip size by one.

input = [187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216]

Problem - what is the result of multiplying the first two numbers in the list?
"""
test_list = [0, 1, 2, 3, 4, 5]
test_lengths = [3, 4, 1, 5]
test = 3
# input_list = list(range(0, 256))

def knot_hash(input_list, lengths):
	# create current position at index 0
	length_slice = 0
	skip_size = 0
	input_list_length = len(input_list)
	current_list = input_list

	for l in lengths:
		# read first length then select slice of the input based on that length
		# first length 3
		current_position = input_list[0]
		current_selection = current_list[current_position:test]
		remaining_list = current_list[]
		# reverse the selection and update the current list
		reversed_selection = current_selection[::-1]
		updated_list = current_list[current_position:+1]=lst[start:end+1][::-1]
		# obtain remaing part of list without selection
		current_list = reversed_selection + 

		# take the index of current position, subtract from the length of the input list, and start the remaining list slice -2 back from current position, then that list is the size difference of total length - index position

		print()


knot_hash(test_list, test_lengths)