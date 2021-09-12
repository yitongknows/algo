class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        tmp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, tmp)
        
    def mergeSort(self, A, start, end, tmp):
        if start >= end:
            return
        
        self.mergeSort(A, start, (start + end) // 2, tmp)
        self.mergeSort(A, (start + end) // 2 + 1, end, tmp)
        
        self.merge(A, start, end, tmp)
        
    def merge(self, A, start, end, tmp):
        mid = (start + end) // 2
        leftIndex = start
        rightIndex = mid + 1
        index = leftIndex
        
        while leftIndex <= mid and rightIndex <= end:
            if A[leftIndex] <= A[rightIndex]:
                tmp[index] = A[leftIndex]
                leftIndex += 1
            else:
                tmp[index] = A[rightIndex]
                rightIndex += 1
            index += 1
            
        while leftIndex <= mid:
            tmp[index] = A[leftIndex]
            index += 1
            leftIndex += 1
        while rightIndex <= end:
            tmp[index] = A[rightIndex]
            index += 1
            rightIndex += 1
            
        for index in range(start, end + 1):
            A[index] = tmp[index]