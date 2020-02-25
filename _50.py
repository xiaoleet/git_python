#面试题50：第一个只出现一次的字符
#暴力解法：两个for 循环嵌套，挨个遍历，把当前字符和字符串中的其他字符相互比较。
# 发现相同，则置标志位=1，表征该字符重复出现，内层for循环终止，继续外层循环。
# 发现不同，继续向下比较，只到整个字符串比较完成，标志位依然=0，则外层for循环终止，返回首次出现的字符s[i]。
# 时间复杂度o（n2）,空间复杂度o（1） 。

#时间复杂度o（n）,空间复杂度o（n）的解法
#hash表解法：扫描2次字符串，
# 第一次扫描字符串，记录各个字符出现的次数，存储起来,第二次扫描字符串，查询hash中value=1的字符，返回该字符，并停止第二次扫描

class Solution:
    # s 源字符串
    def solve_1(self, s):
        #    write code here
        lg = len(s)
        res = ''
        if len(s) == 0:
            return res
        flag = 0#记录是否是首次出现的字符
        for i in range(0,lg):
            for j in range(0,lg):
                if s[i]==s[j] and i!=j:
                    flag = 1
                    break
            if flag == 1:
                flag = 0
            else:
                res = s[i]
                break
        return res

    def solve_2(self, s):
        res = ''
        lg = len(s)
        if lg == 0:
            return res
        tablesize = 256
        hashtable = [0]*tablesize
        for i in range(0,len(s)):
            hashtable[ord(s[i])]+=1
        for i in range(0,len(s)):
            if hashtable[ord(s[i])] == 1:
                res = s[i]
                break
        return res
if __name__ == '__main__':
    sol = Solution()
    s = 'abaccdeff'
    #s = ''
    res_1 = sol.solve_1(s)#暴力解法o（n2)+o(1)
    print (res_1)
    res_2 = sol.solve_2(s)  #降低时间复杂度的解法o(n)+o(n)
    print(res_2)
