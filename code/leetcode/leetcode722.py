class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        in_block = False
        res = []
        for line in source:
            line_com, block_start_com, block_end_com = -1, -1, -1



    def removeCom(self,line):
        for idx in range(1, len(line)):
            if line[idx - 1:idx] == r"//" and line_com < 0:
                return
            if line[idx - 1:idx] == r"/*" and block_start_com < 0:
                line_com = idx - 1

            if line[idx - 1:idx] == r"*/" and block_start_com < 0:
                line_com = idx - 1

