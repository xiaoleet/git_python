#需求：自动生成.py文件，文件名根据命令行输入来定，并向.py文件中固定插入一段初始化代码
init_program="class Solution:
    # s 源字符串
    def solve(self, s):
        #    write code here
        res = s
        return res
if __name__ == '__main__':
    sol = Solution()
    s = ''
    res = sol.solve(s)
    print (res)"
touch $1
echo "$init_program">> $1