"""
If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate. Give a count as well as print the strings. 

For example: 
Input: "121". You need to general all valid alphabet codes from this string. 

Output List 

['aba', 'au', 'la'] i.e.[(1,2,1), (1,21,), (12,1)]
"""

def helper(current, i, num_str, result):
    L = len(num_str)
    if i == L:
        result.append(current)
        return
    n_s = [int(num_str[i])]
    
    if i + 1 < len(num_str):
        n_s.append(int(num_str[i] + num_str[i+1]))

    # if use on digit, delta is 1, else 2
    delta = 1
    for n in n_s:
        if 1 <= n and n <= 26:
            c = chr(ord('a') + n -1)
            helper(current + c, i + delta, num_str, result)
        delta += 1

def numDecodings(num_str):
    result = []
    helper("", 0, num_str, result)
    return result

if __name__ == "__main__":
    result = numDecodings('121')
    print result
