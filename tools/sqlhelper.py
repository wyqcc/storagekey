import pymysql



class Mysqls(object):
    def __init__(self):
        # 读取配置文件
        self.connect()


    def connect(self):

        self.connection = pymysql.connect(host="192.168.0.105", user="root", password="123456", database="allinones")
        self.cursor = self.connection.cursor()

    # def execute_db(self):


    # 获取所以数据
    def get_all(self, sql):

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except:

            self.connection()
            self.cursor.execute(sql)
            return self.cursor.fetchall()



    # 获取一行数据
    # def get_one(self, sql, args):
    #     self.cursor.execute(sql, args)
    #     res = self.cursor.fetchone()
    #     return res
    #
    # # 添加  就是添加一次提交多次
    # def get_mode(self, sql, args):
    #     self.cursor.execute(sql, args)
    #     self.conn.commit()
    #
    # # 添加并且带返回值
    # def get_create(self, sql, args):
    #     self.cursor.execute(sql, args)
    #     self.conn.commit()
    #     return self.cursor.lastrowid
    #
    # # python插入记录后取得主键id的方法(cursor.lastrowid和conn.insert_id())
    #
    # # 批量加入 以元祖的形式传参数   就是添加一次提交一次
    # def mul_mode(self, sql, args):
    #     # self.cursor.executemany("insert into user (id,name) values (%s,%s)",[(1,"aaa"),(2,"bbb"),(3,"ccc")])  传参方式
    #     self.cursor.executemany(sql, args)
    #     self.conn.commit()

    def get_close(self):
        self.cursor.close()
