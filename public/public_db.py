import os
import pymysql
import traceback
#import pandas as pd
# 整个项目根目录的绝对路劲
baseDir = os.path.dirname(os.path.dirname(__file__))

# 数据库配置文件相对于工程根目录的相对路径
config_filePath = baseDir + "\\public\\db_config.ini"

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
#cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
#data = cursor.fetchone()
#print("Database version : %s " % data)

def get_team_rebate_res(suborderid): # 通过子订单获取字段名和所有内容
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM team_rebate \
           WHERE suborderid="+str(suborderid)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        cols = cursor.description # 获取字段信息，以便取出字段名
        col = [i[0] for i in cols]
        resluts = []
        for r in res:
            data = dict(zip(col, list(r))) # 把每条查询结果和字段名组成一个字典
            resluts.append(data) # 把查询出的字典添加到列表中
        #for i in results:
        #   print(list(i))
        return resluts
    except:
        print("Error: unable to fetch data")

def get_unique_id(user_id): # 获取saler_binding_mapping表中unique_id内容，本方法将元组转成列表并反转
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "SELECT unique_id FROM saler_binding_mapping \
               WHERE user_id=" + str(user_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        #print(res)
        result = str(res[0][0]).split(',')
        #print(result)
        if len(result) == 1:
            print("没有上级")
        else:
            return result[::-1]
    except Exception as e:
        #traceback.print_exc()
        print("Error: unable to fetch data")

def get_buyerid_for_team_rebate(suborderid): # 从子订单中获得购买者id
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT buyerid FROM team_rebate \
           WHERE suborderid="+str(suborderid)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        #print(type(res[0][0]))
        return res[0][0]
    except:
        traceback.print_exc()
        print("Error: unable to fetch data")

def get_REuserid_or_VIPuserid_for_payorder(buyerid): # 通过购买者id获取其上层的id
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT recommenduserid,viprecommenduserid FROM payorder \
           WHERE buyerid="+str(buyerid)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        #print(cursor.rowcount)
        print(res)
    except:
        traceback.print_exc()
        print("Error: unable to fetch data")
        return None


def get_orderpaid_for_team_rebate(suborderid):
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT orderpaid FROM team_rebate \
           WHERE suborderid="+str(suborderid)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        #print(res[0][0])
        return res[0][0]
    except:
        traceback.print_exc()
        print("Error: unable to fetch data")
        return None


def get_userid_type_rate_amount_for_team_rebate(suborderid, buyerid): # 获取上级，上级收益类型，返利比例，返利金额
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT userid,type,rate,amount FROM team_rebate \
           WHERE suborderid="+str(suborderid)+" and buyerid="+str(buyerid)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = list(cursor.fetchall())
        print(res)
        return res
    except:
        traceback.print_exc()
        print("Error: unable to fetch data")
        return None

def get_leaderid_for_user_by_userid(userid):
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT leaderid FROM user \
           WHERE userid="+str(userid)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        print(res[0][0])
        return res[0][0]
    except:
        traceback.print_exc()
        print("Error: unable to fetch data")
        return None

def get_grade_for_saler_binding_mapping_by_user_id(user_id): # 通过user_id查询该甄选师的等级
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT grade FROM saler_binding_mapping \
           WHERE user_id="+str(user_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        print(res[0][0])
        return res[0][0]
    except:
        traceback.print_exc()
        print("Error: unable to fetch data")
        return None

def get_recommend_id_for_saler_binding_mapping_by_user_id(user_id): # 通过user_id查询该甄选师直绑上级id
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='MyPass@123', db='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT recommend_id FROM saler_binding_mapping \
           WHERE user_id="+str(user_id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        res = cursor.fetchall()
        print(res[0][0])
        return res[0][0]
    except:
        traceback.print_exc()
        print("Error: unable to fetch data")
        return None



#print(results)
#print(cols)
#print(get_team_rebate_res(452925106906472448))
#db.close()
#print(get_unique_id(996400))

#get_buyerid_for_team_rebate(452925106906472448)
#get_REuserid_or_VIPuserid_for_payorder(2688367)
#get_orderpaid_for_team_rebate(452925106906472448)
#get_userid_type_rate_amount_for_team_rebate(453294299325669376,996400)
#get_leaderid_for_user_by_userid(1565671)
#get_grade_for_saler_binding_mapping_by_user_id(284)
#get_recommend_id_for_saler_binding_mapping_by_user_id(2688367)

# 关闭数据库连接
db.close()
