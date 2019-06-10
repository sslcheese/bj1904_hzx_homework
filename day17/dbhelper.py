'''
db.field('sname,ssex,sclass).where(ssex='男').orderby('sname desc).select()

db.where(ssex='男').orderby('sname desc).field('sname,ssex,sclass).select()

'''
import pymysql
import settings

class Dbhelper:

    def __init__(self,table):
        self.table = table #表名
        self.conn = pymysql.Connect(**settings.parameters) #连接数据库
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor) #游标
        self.params = self.__init_param() #初始化字典参数

    def __def__(self):
        self.cursor.close()
        self.conn.close()

    def __init_param(self):
        return {
            'fields': '*',
            'table': self.table,
            'where': '',
            'groupby': '',
            'having': '',
            'orderby': '',
            'limit': ''
        }


    def where(self,**kwargs):
        """
        where:'uid=1'
        :param args: {'uid':2,username:'tom',password:'dddd'}
        :return:
        """
        if len(kwargs) <= 0:
            return self
        self.__add_quote(kwargs)
        ops = {
            'gt':'>',
            'ge': '>=',
            'lt': '<',
            'le': '<=',
            'ne': '!=',
            'in': ' in ',
            'nin': ' not in ',
            'is': '  is '

        }
        # print(kwargs)
        # if self.params['where']:    #where有值
        #     self.params['where'] += " and "+" and ".join([key +"="+value for key,value in kwargs.items()])
        # else: #where没有值
        #     self.params['where'] = "where " + " and ".join([key +"="+value for key,value in kwargs.items()])
        # print(self.params)
        for key in kwargs:
            keys = key.split("__")
            if len(keys)>1: #运算符不是等号
                op = keys[1] #运算符
                if self.params['where']:
                    self.params['where'] += " and " + keys[0] + ops[op] + kwargs[key]
                else:
                    self.params['where'] = "where " + keys[0] + ops[op] + kwargs[key]
            else:
                if self.params['where']:
                    self.params['where'] += " and " + keys[0] + '=' + kwargs[key]
                else:
                    self.params['where'] = "where " + keys[0] + '=' + kwargs[key]
        # print(self.params['where'])
        return self


    def __add_quote(self,data):
        """
        :param data: 参数字典
        :return:
        """
        for key in data:
            if isinstance(data[key],str): #是字符串两边添加单引号
                data[key] = "'" + data[key] + "'"
            else: #不是字符串，转换为字符串
                data[key] = str(data[key])



    def orderby(self,*args):
        if len(args) <= 0:
            return self
        self.params['orderby'] = ' order by '+ ','.join(args)
        return self


    def groupby(self,*args):
        if len(args) <=0:
            return self
        self.params['groupby'] = ' group by '+ ','.join(args)
        return self


    def having(self,**kwargs):
        if len(kwargs) <= 0:
            return self
        self.__add_quote(kwargs)
        print(kwargs)
        if self.params['having']:  # having有值
            self.params['having'] += " and " + " and ".join([key + "=" + value for key, value in kwargs.items()])
        else:  #having没有值
            self.params['having'] = "having " + " and ".join([key + "=" + value for key, value in kwargs.items()])
        # print(self.params)
        return self

    def fields(self,value):
        '''

        :param value: 形如‘sid,name,sex’
        :return:
        '''
        value = value.strip()
        if not value:
            return self

        self.params['fields'] = str(value)
        return self


    def limit(self,*args):
        if len(args) <= 0:
            return self
        # print(args)
        my_args = [str(value) for value in args]
        # print(my_args)
        self.params['limit'] = " limit "+",".join(my_args)
        return self

    def insert(self,**kwargs):
        """

        :param data: {'name':'tom','sex':'男'}
        :return:
        """
        self.__add_quote(kwargs)
        if len(kwargs)<=0:
            return 0
        else:
            self.params["insert_fields"] = ",".join([key for key,value in kwargs.items()])
            self.params["values"] = ",".join([value for key,value in kwargs.items()])

        sql = "INSERT INTO {table}({insert_fields}) VALUES({values})"
        sql = sql.format(**self.params)
        print(sql)
        return self.execute(sql)

    def update(self,data):
        self.__add_quote(data)
        self.params['value']=','.join([key + '=' + value for key,value in data.items()])
        sql = "UPDATE {table} SET {value} {where}".format(**self.params)
        return self.execute(sql)

    def delete(self):
        sql = "DELETE FROM {table} {where}".format(**self.params)
        return self.execute(sql)




    def execute(self,sql):
        self.sql = sql
        self.__init_param()
        try:
            res = self.cursor.execute(sql)
            if res > 0:
                self.conn.commit()
                return True
            else:
                self.conn.rollback()
                return False
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False


    def select(self):
        sql="SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit};"
        sql = sql.format(**self.params)
        print(sql)
        return self.query(sql)

    def query(self,sql):
        print("1111")
        self.params = self.__init_param() #参数字典初始化

        try:
            # print(self.cursor.execute('SELECT * FROM areainfo where pid=110000'))
            res = self.cursor.execute(sql)
            print(res)
            if res > 0:
                # print("返回数据")
                return self.cursor.fetchall()
            else:
                # print('啥也不返回')
                return None
        except Exception as e:
            print(e)
            return None



if __name__ == "__main__":
    db = Dbhelper('areainfo')
    res = db.where(pid=110000).select()
    print(res)
    # print(db.select())
    # db.where(username='tom',password='123').where(uid=2).select()
    # db.orderby('username asc','uid desc').select()
    # db.limit(5).select()
    # db.limit(1,2).select()
    # db.limit('2').select()
    # data = db.fields("ssex,count(*)").groupby("ssex").select()
    # print(data)
    # data = db.insert(sno=102, sname="张溜溜", sclass= "90444")

    # print(data)