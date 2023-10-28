
import math

class MinStack:
    def __init__(self):
        self.stack = [] # 正常的栈
        self.min_stack = [math.inf] # 辅助栈， 保存正常栈入栈时的最小元素
        # 辅助栈和正常栈要同步操作

        # Python 中 math.inf 返回的是 float("inf")  表示无穷大 无穷小可以表示为 -math.inf

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()