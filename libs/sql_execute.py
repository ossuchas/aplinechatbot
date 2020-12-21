from sqlalchemy import text, create_engine
import urllib

db_params = 'Driver={ODBC Driver 17 for SQL Server};Server=192.168.3.33;Database=crmrevo;uid=app_link;pwd=lin@aru12x;'
db_params = urllib.parse.quote_plus(db_params)
db = create_engine('mssql+pyodbc:///?odbc_connect=%s' % db_params, fast_executemany=True)


def sql_exec(str_sql: str = None):
    # result_set = db.execute("UPDATE dbo.chatbot_mst_user SET modifyby = 'test',  WHERE USER_ID = 1")
    result_set = db.execute(str_sql)
    # print(result_set.rowcount)
    if int(result_set.rowcount) > 0:
        msg_val = 'Update Success'
    else:
        msg_val = 'Update Failed'
    return msg_val

