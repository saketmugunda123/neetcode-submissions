class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        answerArr = [intervals[0]] #Stores the current interval
        arrIndex = 0
        for i in range(1, len(intervals)):

            #Case if there isn't overlap
            if answerArr[arrIndex][1] < intervals[i][0]:
                answerArr.append(intervals[i])
                arrIndex +=1
            else:
                #changing end value of the overlapping interval to be the MAX of the two end values
                answerArr[arrIndex][1] = max(intervals[i][1], answerArr[arrIndex][1])
        
        return answerArr

            





        