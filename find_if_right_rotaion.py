"""
Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)
"""


class IfRightRotation():
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.super_string = self.s1 + self.s1

    def check_if_right_rotation(self):
        if len(self.s1) != len(s2):
            return False
        return True if self.super_string.count(s2) > 0 else False


if __name__=="__main__":
    s1 = raw_input("Enter the S1: ")
    s2 = raw_input("Enter the S2: ")
    obj = IfRightRotation(s1, s2)
    print obj.check_if_right_rotation()
