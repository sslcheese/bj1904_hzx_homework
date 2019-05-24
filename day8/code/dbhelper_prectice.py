import pymysql
import settings

class Dbhelper:

    def __init__(self,table):
        self.table = table #表名
        self.conn = pymysql.Connect(**settings.parameters)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.params = self.__init_param()

    def __def__(self):
        self.cursor.close()
        self.conn.close()

    def __init_param(self):
        return {
            'fields':'*',
            'table': self.table,
            'where': '',
            'groupby': '',
            'having': '',
            'orderby': '',
            'limit': '',
        }

    def fields(self,value):
        value = value.strip()
        if not value:
            return self

        self.params['fields'] = str(value)
        return self

    def where(self,**kwargs):


        pass




