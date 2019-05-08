"""Given an array of distinct integers and a sum value.
Find count of triplets with sum smaller than given sum value.
Expected Time Complexity is O(n2).

Input : arr[] = {-2, 0, 1, 3}
        sum = 2.
Output : 2
Explanation :  Below are triplets with sum less than 2
               (-2, 0, 1) and (-2, 0, 3) 
"""

def triplte_counter(array, length, sum_total):
    count = 0
    triplet_list = []
    for i in range(0, length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                if array[i] + array[j] + array[k] < sum_total:
                    count += 1
                    triplet_list.append([array[i], array[j], array[k]])
    print "total triplet count: ", count
    print "triplet list", triplet_list


if __name__ == "__main__":
    array = [-2, 0, 1, 3]
    length = len(array)
    sum_total = 2
    triplte_counter(array, length, sum_total)
