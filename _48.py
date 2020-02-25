#面试题48：最长不含重复字符的子字符串
#定义f(i):以"第i字符结尾"(划重点)的，不包含重复字符的最长子串
#s = 'arabcacfre'
#思路：
# 1、若s[i]没出现过，则f(i) = f(i-1)+1；
# 2、若s[i] 出现过，记该字符与上次出现的位置距离为d
#   （a）:d<=f(i-1), 则s[i]出现在最长子串中，两个s[i]之间夹得字符都是不重复的，则f(i)=d
#    (b）:d>f(i-1),   则s[i]出现在最长子串之外，则f(i)=f(i-1)+1
#1与2（b）判断逻辑一致、2（a）需要独立判断
#1、如何判定是否出现：postion = [-1]*26，postion[j]=-1 表示未出现，postion[j]>=0 记录最近一次出现s[i]的位置
#2、出现了2种子串长度需要记录：最长子串长度（记录当前最长子串，最终输出最长子串长度）、当前子串长度
#f(0)=1 a:a
#f(1)=2=f(0)+1 r:ar 这里要判断a与r是互不相同的字符
#f(2)=2 a:ra 判断了a与ar中有相同的字符，需要再判断，a离子串'ar'中a的距离，为2=d=f(i-1)，所以f(i) = f(i-1)
#f(3)=f(2)+1=3 b:rab
#f(4)=f(3)+1=4:c:rabc
#f(5)=3 a:bca a 离子串'rabc' 中的a 距离是d=3，d<f(i-1)=4,所以f(i) = d
#f(6)=2 c：ac   c距离最近的c的位置=2 <f(i-1)=3
#f(7)=f(6)+1 f:acf
#f(8)=f(7)+1 r:acfr
#f(9)=f(8)+1 e:acfre

class Solution:
    # s 源字符串
    def solve(self, s):
        #    write code here
        if s== None or len(s) == 0:
            return 0
        curLen = 0
        MaxLen = 0
        postion = [-1]*26 #初始化一个全为-1的26位字母跟踪list
        i = 0
        for i in range(0,len(s)):
            preindex = postion[ord(s[i]) - ord('a')]
            if postion == -1 or i-preindex > curLen:#未出现过 || d>f(i-1)
                curLen = curLen+1 #f(i) = f(i-1)+1
            else:
                if curLen > MaxLen:
                    MaxLen = curLen
                curLen = i-preindex #f(i)=d
            postion[ord(s[i]) - ord('a')] = i#最近一次字符串出现在s[i]的位置
            if curLen > MaxLen:
                MaxLen = curLen
        i = i+1
        res = MaxLen
        return res
if __name__ == '__main__':
    sol = Solution()
    s = 'arabcacfre'
    #s = ''
    res = sol.solve(s)
    print (res)
