# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# 主要需要理解 (idx-1)%10+1 这个表达式的意义
#  这个式子只是要和题解的那个图所对应，写成 idx%10+1 也不会有任何影响

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        idx=(rand7()-1)*7+rand7()
        if idx<=40:
            return (idx-1)%10+1