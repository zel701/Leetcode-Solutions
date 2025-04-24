def add_candy(grade,candyamount):
    i=0
    while i < len(grade):
        if i == 0:
            if grade[i] > grade[i + 1] and candyamount[i] <= candyamount[i + 1]:
                candyamount[i] = candyamount[i + 1] + 1

            '''if grade[i] == grade[i+1] and candyamount[i] <= candyamount[i+1]:
                candyamount[i] = candyamount[i+1]'''
            i += 1

        elif 0 < i < len(grade) - 1:
            if grade[i] > grade[i - 1] and candyamount[i] <= candyamount[i - 1]:
                candyamount[i] = candyamount[i - 1] + 1

            if grade[i] > grade[i + 1] and candyamount[i] <= candyamount[i + 1]:
                candyamount[i] = candyamount[i + 1] + 1

            '''if grade[i] == grade[i+1] and candyamount[i] <= candyamount[i+1]:
                candyamount[i] = candyamount[i+1]
            if grade[i] == grade[i-1] and candyamount[i] <= candyamount[i-1]:
                candyamount[i] = candyamount[i-1]'''
            i += 1

        elif i == len(grade) - 1:
            if grade[i] > grade[i - 1] and candyamount[i] <= candyamount[i - 1]:
                candyamount[i] = candyamount[i - 1] + 1
            '''if grade[i] == grade[i-1] and candyamount[i] <= candyamount[i-1]:
                candyamount[i] = candyamount[i-1]'''
            i += 1

    return candyamount
class Solution:
    
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        candyamount = [1] * len(ratings)
        candyamount = add_candy(ratings,candyamount)
        candyamount.reverse()
        ratings.reverse()
        candyamount = add_candy(ratings, candyamount)
        candyamount.reverse()

    

        return sum(candyamount)