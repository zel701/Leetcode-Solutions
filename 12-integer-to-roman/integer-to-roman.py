class Solution:
    def intToRoman(self, num: int) -> str:
        finaltext = ""
        if num//1000 > 0:
            finaltext = finaltext + "M"*(num//1000)
            num = num%1000
        if num//900 == 1:
            finaltext = finaltext + "CM"
            num = num -900
        if num//500 == 1:
            finaltext = finaltext + "D"
            num = num - 500
        if num//400 == 1:
            finaltext = finaltext + "CD"
            num = num - 400
        if num//100 > 0:
            finaltext = finaltext + "C" * (num // 100)
            num = num % 100
        if num//90 == 1:
            finaltext = finaltext + "XC"
            num = num - 90
        if num//50 == 1:
            finaltext = finaltext + "L"
            num = num - 50
        if num//40 == 1:
            finaltext = finaltext + "XL"
            num = num - 40
        if num//10 > 0:
            finaltext = finaltext + "X" * (num // 10)
            num = num % 10
        if num//9 == 1:
            finaltext = finaltext + "IX"
            num = num - 90
        if num//5 == 1:
            finaltext = finaltext + "V"
            num = num - 5
        if num//4 == 1:
            finaltext = finaltext + "IV"
            num = num - 4
        if num//1 > 0:
            finaltext = finaltext + "I" * (num // 1)
            num = num % 1
        return finaltext