import pymysql
def dbconnect():
    connection = pymysql.connect(host='localhost', user='readonly', passwd='coursera', db='COURSERA', charset='utf8')
    return connection

