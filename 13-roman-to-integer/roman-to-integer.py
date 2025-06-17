class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        s = list(s)
        i=0
        while i<len(s):
            if s[i] == "I":
                if i+1<len(s):
                    if s[i+1]=="V":
                        sum+=4
                        i+=2
                    elif s[i+1]=="X":
                        sum += 9
                        i += 2
                    else:
                        sum+=1
                        i+=1
                else:
                    sum += 1
                    i += 1
            elif s[i] == "X":
                if i + 1 < len(s):
                    if s[i+1]=="L":
                        sum+=40
                        i+=2
                    elif s[i+1]=="C":
                        sum += 90
                        i += 2
                    else:
                        sum+=10
                        i+=1
                else:
                    sum += 10
                    i += 1
            elif s[i] == "C":
                if i + 1 < len(s):
                    if s[i+1]=="D":
                        sum+=400
                        i+=2
                    elif s[i+1]=="M":
                        sum += 900
                        i += 2
                    else:
                        sum+=100
                        i+=1
                else:
                    sum += 100
                    i += 1
            elif s[i] == "V":
                sum += 5
                i += 1

            elif s[i] == "L":
                sum += 50
                i += 1

            elif s[i] == "D":
                sum += 500
                i += 1

            elif s[i] == "M":
                sum += 1000
                i += 1
        return sum