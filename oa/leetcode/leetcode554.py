class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        wall_index=[]
        for bricks in wall:
            length=0
            for b in bricks:
                length+=b
                wall_index.append(length)
            wall_index.pop()

        wall_index.sort()
        max_num=0
        cur=0
        cur_num=0
        for i in wall_index:
            if i==cur:
                cur_num+=1
            else:
                max_num=max(max_num,cur_num)
                cur=i
                cur_num=1
        return len(wall)-max_num