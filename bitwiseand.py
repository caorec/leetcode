#Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

def rangeBitwiseAnd(self, left: int, right: int) -> int:
    if len(bin(right)) != len(bin(left)):
        return 0
    elif right == left:
        return left
    else:
        c = len(bin(left ^ right)) - 2
        t = bin(left)[:-c] + "0" * c
        return int(t, 2)
