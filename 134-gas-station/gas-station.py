class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        profit = []
        gasleft = [0]
        for i in range(len(gas)):
            profit.append(gas[i] - cost[i])

        x = -1
        j = 0
        gasremain = 0
        Tripstart = False
        reset = True
        while x < len(profit):
            x += 1
            if x == len(profit) and reset == True:
                if Tripstart == False:
                    j = -1
                    break
                x = 0
                reset = False
            if x == len(profit):
                j = -1
                break
            if profit[x] < 0 and not Tripstart:
                pass
            if not Tripstart:
                if profit[x] >= 0:
                    j = x
                    gasremain = profit[x]
                    print(gasremain)
                    Tripstart = True
            else:

                gasremain = gasremain + profit[x]

                print(gasremain)
                if x == j:
                    break
                if gasremain < 0:
                    print(gasremain)
                    Tripstart = False
                    j=-1

        for i in range(len(profit)):
            if i>0:
                gasleft.append(gasleft[i-1] + profit[i])

        for i in range(len(gasleft)):
            if gasleft[i] >= 0:
                return j
        return -1
