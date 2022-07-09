class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:


        max_duration=releaseTimes[0]
        max_word=keysPressed[0]
        for idx in range(1,len(releaseTimes)):
            duration=releaseTimes[idx]-releaseTimes[idx-1]
            if duration>max_duration:
                max_word=keysPressed[idx]
                max_duration=duration
            elif duration==max_duration:
                if ord(keysPressed[idx])>ord(max_word):
                    max_word=keysPressed[idx]
        return max_word





