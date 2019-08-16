import os

baseDir = os.path.dirname(os.path.dirname(__file__))
#print(baseDir,type(baseDir))
excelPath = os.path.join(baseDir,'TestData\\test_source.xlsx')
#print(excelPath)
ex = os.path.exists(excelPath)
TestExcelName='测试用例'

# 测试用例页列号数字映射
TestOrderNo = 2
TestBuyerid = 3
TestOrderpaid = 4
TestCaseSheetName = 5
TestCaseActive = 6
TestTime = 7
TestResult = 8
TestErrorInfo = 9
# 测试数据页列号数字映射
CASE_ZhenxuanID = 0 # 甄选师ID
CASE_UpperID = 1 # 上级ID
CASE_ZhenxuanLV = 2 # 等级
CASE_JumpPoint = 3 # 跳点
CASE_JumpPointEndtime = 4 # 跳点结束日期
CASE_FirstUpperID = 5 # 一级上线ID
CASE_FirstUpperLV = 6 # 一级上线等级
CASE_FirstUpperType = 7 # 分类(1为直接上级)
CASE_SecondUpperID = 8 # 二级上线ID
CASE_SecondUpperLV = 9 # 二级上线等级
CASE_BreedID = 10 # 育成ID
CASE_BreedLV = 11 # 育成等级
CASE_FirstLVIncome = 12 # 一级收益
CASE_SecondLVIncome = 13 # 二级收益
CASE_ThirdLVIncome = 14 # 三级收益
CASE_BreedIncome = 15 # 育成奖励


if __name__ == '__main__':
    print(baseDir)
    print(excelPath)
    print(ex)