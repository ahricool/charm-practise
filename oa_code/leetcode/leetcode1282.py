import collections


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d=collections.defaultdict(list)
        for idx in range(len(groupSizes)):
            max_size=groupSizes[idx]
            groups=d[max_size]
            joined=False
            for group in groups:
                if len(group)<max_size:
                    group.append(idx)
                    joined=True
            if not joined:
                groups.append([idx])

        return [group for groups in d.values() for group in groups]


    


