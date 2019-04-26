"""
Maximize the total profit of all the persons
There is a hierarchical structure in an organization. A party is to be organized. No two immediate subordinates can come to the party. A profit is associated with every person. You have to maximize the total profit of all the persons who come to the party.

Hierarchical Structure
In a hierarchical organization, all employees(except the one at the head) are subordinates of some other employee.
Employees only directly report to their immediate superior. This allows for a flexible and efficient structure.

Examples:

Input: 
         15
       /   \
     10     12
    /  \   /  \
   26   4 7    9
Output: The Maximum Profit would be 15+12+26+9 = 62
The Parent 15 chooses sub-ordinate 12, 10 chooses 26 and 12 chooses 9.

Input:
        12
       / | \
      9 25 16
     /     / \
    13    13   9
Output: 12+25+13+13 = 63
"""


def getMaxProfit(hier): 
    # The head has no competition and therefore invited
    totSum = hier[1][0] 
    for i in hier: 
        currentSuperior = hier[i] 
        selectedSub = 0
        # select the subordinate with maximum 
        # value of each superior 
        for j in currentSuperior[1]: 
            if(hier[j][0] > selectedSub): 
                selectedSub = hier[j][0] 
        totSum += selectedSub 
    return totSum 
  
# driver function 
def main(): 
    # Define the Organization as a Dictionary 
    # Index : [Profit, List of Employees] 
        # Same as example 1 given above 
# 1:15 
#       /     \ 
# 2:10    3:12 
#    /   \    /   \ 
# 4:26 5:4 6:7  7:9 
  
    organization = {1:[15, [2, 3]], 
                    2:[10, [4, 5]], 3:[12, [6, 7]], 
                    4:[26, []], 5:[4, []], 6:[7, []], 7:[9, []]} 
    maxProfit = getMaxProfit(organization) 
    print(maxProfit) 
      
main() 
