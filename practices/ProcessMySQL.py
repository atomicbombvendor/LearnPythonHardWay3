import datetime

import os
import pymysql
import sys


def query_data(shareClassId):
    connect = pymysql.connect(host="geapidbdev81",
                         port=3306,
                         user="GeDataAgent",
                         password="1234567#",
                         db="GEAPI")
    cursor = connect.cursor()
    (operationid, datacategoryid, idtype, productionFrom, status, MiscNotes, Notes, UpdateTime, CreateTime)\
        = (None, None, None, None, None, None, None, None, None)

    # 获取数据
    sql = "select * from GEAPI.MSSDumpMangement where OperationId='@shareId' and DataCategoryId=105031"
    cursor.execute(sql.replace("@shareId", shareClassId))

    for row in cursor.fetchall():
        operationid = row[0]
        datacategoryid = row[1]
        idtype = row[2]
        productionFrom = row[3].strftime('%Y%m%d')
        status = row[4]
        MiscNotes = row[5]
        Notes = row[6]
        UpdateTime = row[7].strftime('%Y%m%d')
        CreateTime = row[8].strftime('%Y%m%d')
    print('共查找出', cursor.rowcount, '条数据')

    file = "result/" + operationid + "/" + UpdateTime + ".dat"
    if file:
        data = "%s, %s, %s, %s, %s, %s, %s, %s, %s" \
            % (operationid, datacategoryid, idtype, productionFrom, status, MiscNotes, Notes, UpdateTime, CreateTime)
    else:
        file = datetime.date.today().strftime('%Y%m%d')
        data = "%s have no data in database" % shareClassId

    write_content(file, data)


def write_content(file, data):
    folder = os.path.dirname(file)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    with open(file, "w") as f:
        f.write(data)


shareClassId = sys.argv[1]
query_data(shareClassId)

# query_data("0P000002RH")