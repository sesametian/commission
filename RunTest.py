from public.public_excel import *
from utils.ParseExcel import ParseExcel
from public.public_db import *
from action.write_result import write_result, write_time
from action.commission import *

def main():
    parseE = ParseExcel()
    parseE.loadWorkBook(excelPath)
    sheetObj = parseE.getSheetByName(TestExcelName)
    activeList = parseE.getColumn(sheetObj, TestCaseActive)
    #print(activeList)
    EX_resdict = {}
    IsPass = True
    errorInf = None
    for idx, cell in enumerate(activeList[1:], 2):
        #print(cell.value)
        if cell.value == "y" or cell.value == "Y":
            rowObj = parseE.getRow(sheetObj, idx)
            TestCaseName = rowObj[TestCaseSheetName -1].value
            #print(TestCaseName)
            OrderNo = rowObj[TestOrderNo -1].value
            #print(OrderNo)
            EX_buyerid = rowObj[TestBuyerid-1].value
            print("EX_buyerid",EX_buyerid)
            EX_orderpaid = rowObj[TestOrderpaid-1].value
            #print("EX_orderpaid",EX_orderpaid)
            caseSheetObj = parseE.getSheetByName(TestCaseName)
            #print(caseSheetObj)
            write_time(parseE, sheetObj, idx, TestTime, coordinate=None) # 用例执行时间

            EX_zhenxuanid_list =[v.value for v in parseE.getColumn(caseSheetObj, CASE_ZhenxuanID+1)[1:]] # excel中取出甄选师列中所有数据
            #for buyerid in buyerid_tuple[1:]:
            #    print(buyerid.value)
            #print(EX_zhenxuanid_list)
            DB_zhanxuanid = get_leaderid_for_user_by_userid(EX_buyerid)
            #print('DB', DB_zhanxuanid)
            DB_orderpaid = get_orderpaid_for_team_rebate(OrderNo)  # 获取订单实际支付金额
            print('DB_orderpaid', DB_orderpaid)

            DB_zhenxuan_and_type_rate_amount = get_userid_type_rate_amount_for_team_rebate(OrderNo, EX_buyerid)
            print(DB_zhenxuan_and_type_rate_amount)  # 从数据库中获取甄选师id，返利类型，返利比例，返利金额
            # type返利类型0甄选收益，1一级奖励，2二级奖励，3育成奖励
            DB_unique_id = get_unique_id(DB_zhanxuanid)
            print('DB_unique_id', DB_unique_id)

            if DB_orderpaid == EX_orderpaid:
                print("DB订单金额与EX一致")
            else:
                print("DB订单金额与EX不一致！！！")
                errorInf = "DB订单金额与EX不一致！！！"
                write_result(parseE, sheetObj, idx, errorInf)
                continue

            if DB_zhanxuanid in EX_zhenxuanid_list: # 按甄选师id找到excel中所在行中全部内容，可以从这个列表中找到上级和所有收益多少
                Zidx = EX_zhenxuanid_list.index(DB_zhanxuanid) # 找到甄选师行号
                #print(Zidx)
                EX_cassrow = parseE.getRow(caseSheetObj, Zidx + 1 + 1) # 获得该甄选师行的所有内容
                #print(EX_cassrow)

                for index, EX_cell in enumerate(EX_cassrow, 1): # 通过枚举得到甄选师列列号与内容的字典
                    # print(idx, EX_cell.value)
                    EX_resdict[index] = EX_cell.value
                print('111', EX_resdict)
                print('2222', EX_resdict[1])

                #ZX_amount = DB_orderpaid * 1

                #IsPass = True
                if TestCaseName == 'b0_b1_b2':
                    result = b0_b1_b2_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid)
                    errorInf = result[1]

                elif TestCaseName == 'b0_b2':
                    result = b0_b2_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid)
                    errorInf = result[1]

                elif TestCaseName == 'b1-b1-b2':
                    result = b1_b1_b2_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid)
                    errorInf = result[1]

                elif TestCaseName == 'b1-b2':
                    result = b1_b2_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid)
                    errorInf = result[1]

                elif TestCaseName == 'b2-b1':
                    result = b2_b1_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid)
                    errorInf = result[1]
            else:
                print(DB_zhanxuanid, "不在用例中")
                errorInf = "不在用例中"
                IsPass = False
                #print(Zidx)
            #print(errorInf)
            write_result(parseE, sheetObj, idx, errorInf)

if __name__=="__main__":
    main()


