# -*- coding:utf-8 -*-
#https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
#请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
class Solution:
    # s 源字符串
    def replaceSpace(self, s):#开辟新空间，非原字符串上做修改
        #    write code here
        tg1 = "%20"
        tg2 = " "
        res = ""
        for ch in s:
            if ch == " ":
                ch="%20"
            res=res+ch
        return res
if __name__ == '__main__':
    sol = Solution()
    s = 'we are fans'
    res = sol.replaceSpace(s)
    print (res)