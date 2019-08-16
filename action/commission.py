from public.public_db import *
from public.public_excel import *

def b0_b1_b2_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid):
    IsPass = True
    errorInf = None
    for ZTRA in DB_zhenxuan_and_type_rate_amount:
        if ZTRA[0] == EX_resdict[1] and ZTRA[1] == 0:  # 对比甄选收益
            print('EX_resdict[13]', EX_resdict[13])
            ZX_amount = DB_orderpaid * (EX_resdict[13] / 100)
            if ZTRA[3] == ZX_amount:
                print("甄选收益正确")
            else:
                IsPass = False
                errorInf = "甄选收益错误"
                print(errorInf)
                return IsPass,errorInf
        elif ZTRA[0] == EX_resdict[6] and ZTRA[1] == 1:  # 对比一级收益
            # print(ZX_amount * ((EX_resdict[14] / 10) * EX_resdict[4]))
            if ZTRA[3] == ZX_amount * ((EX_resdict[14] / 10) * EX_resdict[4]):
                print("一级收益正确")
            else:
                IsPass = False
                errorInf = "一级收益错误"
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[9] and ZTRA[1] == 2:
            if ZTRA[3] == ZX_amount * (EX_resdict[15] / 10):
                print("二级收益正确")
            else:
                IsPass = False
                errorInf = "二级收益错误"
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[11] and ZTRA[1] == 3:
            if ZTRA[3] == round(ZX_amount * (EX_resdict[16] / 10)):
                print("育成收益正确")
            else:
                IsPass = False
                errorInf = "育成收益错误"
                return IsPass, errorInf
    print('b0_b1_b2', IsPass)
    return IsPass, errorInf

def b0_b2_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid):
    IsPass = True
    errorInf = None
    for ZTRA in DB_zhenxuan_and_type_rate_amount:
        if ZTRA[0] == EX_resdict[1] and ZTRA[1] == 0:  # 对比甄选收益
            ZX_amount = DB_orderpaid * (EX_resdict[11] / 100)
            if ZTRA[3] == ZX_amount:
                print("甄选收益正确")
            else:
                IsPass = False
                errorInf = "甄选收益错误"
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[6] and EX_resdict[6] == get_recommend_id_for_saler_binding_mapping_by_user_id(
                EX_resdict[1]) \
                and ZTRA[1] == 1:  # 对比一级收益
            if ZTRA[3] == ZX_amount * ((EX_resdict[12] / 10) * EX_resdict[4]):
                print("一级收益正确")
            else:
                IsPass = False
                errorInf = "一级收益错误"
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[9] and ZTRA[1] == 3:
            if ZTRA[3] == round(ZX_amount * (EX_resdict[13] / 10)):
                print("育成收益正确")
            else:
                IsPass = False
                errorInf = "育成收益错误"
                return IsPass, errorInf
    print('b0_b2', IsPass)
    return IsPass, errorInf

def b1_b1_b2_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid):
    IsPass = True
    errorInf = None
    for ZTRA in DB_zhenxuan_and_type_rate_amount:
        if ZTRA[0] == EX_resdict[1] and ZTRA[1] == 0:
            ZX_amount = DB_orderpaid * (EX_resdict[13] / 100)
            if ZTRA[3] == ZX_amount:  # 对比甄选收益
                print("甄选收益正确")
            else:
                IsPass = False
                errorInf = "甄选收益错误"
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[6] and ZTRA[1] == 1:  # 对比一级收益
            if ZTRA[3] == ZX_amount * ((EX_resdict[14] / 10) * EX_resdict[4]):
                print("一级收益正确")
            else:
                IsPass = False
                errorInf = "一级收益错误"
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[9] and ZTRA[1] == 2:  # 对比二级收益
            if ZTRA[3] == ZX_amount * (EX_resdict[15] / 10):
                print("二级收益正确")
            else:
                IsPass = False
                errorInf = "二级收益错误"
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[11] and ZTRA[1] == 3:  # 对比育成收益
            if ZTRA[3] == round(ZX_amount * (EX_resdict[16] / 10)):
                print("育成收益正确")
            else:
                IsPass = False
                errorInf = "育成收益错误"
                return IsPass, errorInf
    print('b1-b1-b2', IsPass)
    return IsPass, errorInf

def b1_b2_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid):
    IsPass = True
    errorInf = None
    for ZTRA in DB_zhenxuan_and_type_rate_amount:
        if ZTRA[0] == EX_resdict[1] and ZTRA[1] == 0:  # 对比甄选收益
            ZX_amount = DB_orderpaid * (EX_resdict[11] / 100)
            if ZTRA[3] == ZX_amount:
                print("甄选收益正确")
            else:
                IsPass = False
                errorInf = "甄选收益错误"
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[6] and ZTRA[1] == 1:  # 对比一级收益
            #print('!!!!!!!!!!!!!!!!',ZX_amount)
            if ZTRA[3] == ZX_amount * ((EX_resdict[12] / 10) * EX_resdict[4]):
                print("一级收益正确")
            else:
                IsPass = False
                errorInf = "一级收益错误"
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[9] and ZTRA[1] == 3:  # 对比育成收益
            if ZTRA[3] == round(ZX_amount * (EX_resdict[13] / 10)):
                print("育成收益正确")
            else:
                IsPass = False
                errorInf = "育成收益错误"
                return IsPass, errorInf
    print('b1-b2', IsPass)
    return IsPass, errorInf

def b2_b1_result(DB_zhenxuan_and_type_rate_amount, EX_resdict, DB_orderpaid):
    IsPass = True
    errorInf = None
    for ZTRA in DB_zhenxuan_and_type_rate_amount:
        if ZTRA[0] == EX_resdict[1] and ZTRA[1] == 0:  # 对比甄选收益
            ZX_amount = DB_orderpaid * (EX_resdict[7] / 100)
            if ZTRA[3] == ZX_amount:
                print("甄选收益正确")
            else:
                IsPass = False
                errorInf = "甄选收益错误"
                print(errorInf)
                return IsPass, errorInf
        elif ZTRA[0] == EX_resdict[5] and get_recommend_id_for_saler_binding_mapping_by_user_id(EX_resdict[1]) == EX_resdict[5] \
                and ZTRA[1] == 1:  # 对比一级收益
            if ZTRA[3] == ZX_amount * ((EX_resdict[8] / 10) * EX_resdict[3]):
                print("一级收益正确")
            else:
                IsPass = False
                errorInf = "一级收益错误"
                return IsPass, errorInf
    print('b2-b1', IsPass)
    return IsPass, errorInf
