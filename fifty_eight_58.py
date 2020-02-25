#面试题58:翻转字符串
#不开辟空间
#两次循环：
# 第一次遍历翻转原所有字符,
# 第二次遍历翻转后的字符集合
class Solution:
    # s 源字符串
    def solve(self, s):
        #    write code here
        s = list(s)
        lg = len(s)
        res = ''
        if lg == 0:
            return res
        i = 0  #记录字母开端
        j = 0  #记录单词的尾巴
        s = self.reverse(i,lg-1,s)#翻转整个句子
        #翻转单词
        while i<lg and j <lg:#防止溢出
            if s[i] == ' ':#i 指到单词的空格
                i+=1
                j+=1
            elif s[j] == ' ':#j 指到单词的空格
                j-=1
                s = self.reverse(i,j,s)
                j+=1
                i = j
            elif j == (lg - 1):
                s = self.reverse(i, j, s)
                j+=1
                i=j
            else:
                j+=1
        res = ''.join(s)
        return res
    def reverse(self,i,j,s):
        res = ''
        tmp = ''
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        return s
if __name__ == '__main__':
    sol = Solution()
    s = 'I am a student.'
    s = 'ansonwan '#功能测试：单个字符+空格
    s = ' ansonwan'#功能测试：空格+单个字符
    s = 'ansonwan'#功能测试：单个字符
    s = ''#异常测试：为空的字符串
    s = '    '#异常测试：4个空格的字符串
    res = sol.solve(s)
    print (res,len(res))
