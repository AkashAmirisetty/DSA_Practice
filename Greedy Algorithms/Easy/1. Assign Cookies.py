class Solution:
    def findMaximumCookieStudents(self, Student, Cookie):
        #your code goes here
        Student.sort()
        Cookie.sort()
        s=len(Student)
        c=len(Cookie)
        cnt=0
        i,j=0,0
        while i<s and j<c:
            if Cookie[j]>=Student[i]:
                cnt+=1
                i+=1
            j+=1
        return cnt