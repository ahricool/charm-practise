class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []

        mapping={"2":"abc",
                 "3":"def",
                 "4":"ghi",
                 "5":"jkl",
                 "6":"mno",
                 "7":"pqrs",
                 "8":"tuv",
                 "9":"wxyz"}
        alphabet=mapping[digits[0]]
        if len(digits)<=1:
            return [ letter for letter in alphabet]
        else:
            combinations=self.letterCombinations(digits[1:])
            return [ letter+comb for comb in combinations for letter in alphabet]