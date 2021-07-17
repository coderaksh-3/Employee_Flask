import pymysql as p


def getConnect():
    return p.connect(host='localhost', user='root', password='', database='rakshita_db')


def addEmp(t):
    db = getConnect()
    cr = db.cursor()
    sql = 'insert into empf values(%s,%s,%s,%s,%s,%s)'
    cr.execute(sql,t)
    db.commit()
    db.close()


def getEmpList():
    sql="select * from empf"
    db = getConnect()
    cr = db.cursor()
    cr.execute(sql)
    elist = cr.fetchall()
    db.commit()
    db.close()
    return elist


def deleteEmp(id):
    db = getConnect()
    cr = db.cursor()
    sql = 'delete from empf where id=%s'
    cr.execute(sql,id)
    db.commit()
    db.close()


def getEmpById(id):
    db = getConnect()
    cr = db.cursor()
    sql = 'select * from empf where id=%s'
    cr.execute(sql,id)
    elist = cr.fetchall()
    db.commit()
    db.close()
    return elist[0]


def updateEmp(t):
    db = getConnect()
    cr = db.cursor()
    sql = 'update empf set name=%s, email=%s, password=%s, cont=%s, dept=%s where id=%s'
    cr.execute(sql,t)
    db.commit()
    db.close()


