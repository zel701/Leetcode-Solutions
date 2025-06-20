class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        word = ""
        finalsentence = ""
        for i in range(len(s)):
            if s[i] != " ":
                word = word + s[i]
            else:
                if word!= "":
                    finalsentence = word + " " + finalsentence
                    word=""
        finalsentence = word + " " + finalsentence
        return finalsentence.strip()