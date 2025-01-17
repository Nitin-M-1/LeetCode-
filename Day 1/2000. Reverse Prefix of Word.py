class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        endIndex = 0 
        Found = False
        for x in range(len(word)):
            if word[x] == ch:
                Found = True
                break
            endIndex +=1
        
        if Found:
            word = [y for y in word ]
            tempIndex = endIndex
            for x in range(int((endIndex+1)/2)):
                temp = word[x]
                word[x] = word[tempIndex]
                word[tempIndex] = temp
                tempIndex -=1 
        else:
            return word

        return "".join(word)