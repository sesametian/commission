from public.public_excel import *

def write_result(wbObj, sheetObj, rowNo, errorInf):
    # 将测试结果写到excel中对应的单元格中
    # 写响应body
    #wbObj .writeCell(sheet=sheetObj, content="%s" %info,
                     #rowNo=rowNo, colsNo=TestResult)
    # 写校验结果状态列及错误
    if errorInf:
        wbObj.writeCell(sheet=sheetObj, content="faild",
                        rowNo=rowNo, colsNo=TestResult)
        wbObj.writeCell(sheetObj, content="%s" %errorInf, rowNo=rowNo,
                        colsNo=TestErrorInfo)
    else:
        wbObj.writeCell(sheet=sheetObj, content="pass",
                        rowNo=rowNo, colsNo=TestResult)

def write_time(wbObj, sheetObj, rowNo, colsNo, coordinate):
    wbObj.writeCellCurrentTime(sheet=sheetObj, coordinate=coordinate, rowNo=rowNo, colsNo=colsNo)