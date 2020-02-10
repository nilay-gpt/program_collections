"""
Given arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop

Examples:

Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)

Bellow is O[n log n] complexity. Exp bellow:
O(n): to traverse atleast arrival list once completly + 
O(log n) : depends upon the arrival list we will traverse the departure list.

"""


class PlatformCounter(object):
    def __init__(self, arrival, departure):
        self.arrival = arrival
        self.departure = departure

        # Sort both the list in the starting.
        self.arrival.sort()
        self.departure.sort()

    def minimum_count_get(self):
        # platform and result will always be 1 because we need atleast one platform in minimum
        # i, j are two pointers for arrival and departure list.
        platform, result, i, j, arr_length= 1, 1, 1, 0, len(self.arrival)

        while i < arr_length and j < arr_length:
            if self.arrival[i] < self.departure[j]:
                platform += 1
                i +=1
                if platform > result: result = platform
            else:
                platform -= 1
                j +=1
        return result


if __name__ == "__main__":
    arrival = [900, 940, 950, 1100, 1500, 1800] 
    departure = [910, 1200, 1120, 1130, 1900, 2000] 
    obj = PlatformCounter(arrival, departure)
    result = obj.minimum_count_get()
    print result
