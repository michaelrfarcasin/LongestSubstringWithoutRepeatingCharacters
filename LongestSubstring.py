class LongestSubstring():
    def getLength(self, s):
        if len(s) < 2:
            return len(s)
        seen = []
        maxLength = 0
        for char in s:
            if char in seen:
                index = seen.index(char)
                del seen[:index + 1]
            seen.append(char)
            if len(seen) > maxLength:
                maxLength = len(seen)
        return maxLength
