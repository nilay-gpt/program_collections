import math


def merge_overlapping(user_list):
	count = 1
	final_list = []
	for item in user_list:
		try:
			if item[1] > user_list[count][0] and item[1] < user_list[count][1]:
				final_list.append([item[0], user_list[count][1]])
				user_list.pop(count)
			else:
				final_list.append(item)
		except:
			final_list.append(item)
		count += 1
	return final_list


if __name__ == "__main__":
	user_list = [[1,3], [2,6], [5, 7], [6, 8], [7 , 10], [12, 15], [13, 20], [17, 100], [1000, 1005]]
	loop_length = int(math.ceil(len(user_list)/2.0))
	for i in range(loop_length):
		user_list = merge_overlapping(user_list)
	print user_list
