class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda box:box[1])
        max_unites=0
        while truckSize>0 and boxTypes:
            boxes=boxTypes.pop()
            if boxes[0]<truckSize:
                max_unites+=boxes[0]*boxes[1]
                truckSize-=boxes[0]
            else:
                max_unites+=boxes[0]*truckSize
                truckSize=0

        return max_unites


