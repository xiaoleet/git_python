#面试题58:左旋字符串
class Solution:
    # s 源字符串
    def solve(self,s,tg):
        #    write code here

        if tg > len(s):
            return '不合法'
        lg = len(s) - 1
        if lg == -1 or lg == 0 or s.isspace():
            return s
        s = list(s)
        s = self.reverse(0,lg,s)
        s = self.reverse(0,lg-tg,s)
        s = self.reverse(lg-tg+1,lg,s)
        res = ''.join(s)
        return res
    def reverse(self,i,j,s):
        tmp = ''
        while i<j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i+=1
            j-=1
        return s
if __name__ == '__main__':
    sol = Solution()
    s = 'abcdefg'#功能:正常主流程
    #s = ''#异常:空字符
    #res = sol.solve(s, 2)
    #res = sol.solve(s,0)#不旋转
    #res = sol.solve(s,1) #旋转1位
    #res = sol.solve(s,len(s)-1)#旋转n-1个字符
    res = sol.solve(s, len(s))  # 旋转n个字符
    res = sol.solve(s,len(s)+1)#旋转n个字符
    print (res)
