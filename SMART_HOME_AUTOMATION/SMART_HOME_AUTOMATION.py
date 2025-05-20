from datetime import time

from flask import Flask,request,jsonify,session
from DBConnection import Db
app = Flask(__name__)
app.secret_key="kk"


@app.route('/login',methods=["post"])
def login():
    username = request.form['username']
    password = request.form['password']

    qry="SELECT `lid` FROM `login` WHERE `username`='"+username+"' AND `password`='"+password+"'"
    d=Db()
    res=d.selectOne(qry)
    if res is not None:
        return jsonify(status='ok',lid=res["lid"])
    else:
        return jsonify(status='no')

@app.route('/change_password',methods=["post"])
def change_password():
    currentpassword = request.form['currentpassword']
    newpassword = request.form['newpassword']
    confirmpassword = request.form['confirmpassword']
    ps=request.form["psw"]
    lid=request.form["lid"]
    if currentpassword==ps:
        if confirmpassword==newpassword:
            qry="UPDATE `login` SET PASSWORD='"+confirmpassword+"'WHERE `lid`='"+lid+"'"
            d=Db()
            res=d.update(qry)
            return jsonify(status='ok')
        else:
            return jsonify(status='no')
    else:
        return jsonify(status='no')


@app.route('/add_familiar_person',methods=["post"])
def add_familiar_person():
    image = request.form['image']
    name = request.form['name']
    description = request.form['description']
    qry="INSERT INTO `familiar`(`name`,`photo`,`description`)VALUES('"+name+","+image+","+description+"')"
    d=Db()
    res=d.insert(qry)
    return jsonify(status='ok')

@app.route('/device__control',methods=["post"])
def device_control():
    deviceid=request.form['deviceid']
    status=request.form['status']
    qry="UPDATE `device control` SET STATUS='"+status+"'WHERE`device id`='"+deviceid+"'"
    d=Db()
    res=d.update(qry)
    return jsonify(status='ok')

@app.route('/view_familiar_person',methods=["post"])
def view_familiar_person():
    qry="SELECT * FROM `familiar`"
    d=Db()
    res=d.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/view_visitor_log',methods=["post"])
def view_visitor_log():
    qry="SELECT * FROM `visitor log`"
    d=Db()
    res=d.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/user',methods=["post"])
def user():
    username=request.form['username']
    password=request.form['password']
    place=request.form['place']
    district=request.form['district']
    email=request.form['email']
    image=request.form['image']
    import datetime
    import  base64
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(image)
    fh = open("C:\\Users\\user\\PycharmProjects\\SMART_HOME_AUTOMATION\\static\\userpics\\" + timestr + ".jpg", "wb")
    path = "/static/userpics/" + timestr + ".jpg"
    fh.write(a)
    fh.close()
    phone=request.form['phone']
    qry1 = "INSERT INTO `login`(`username`,`password`)VALUES('" + username + "," + password + "')"
    d = Db()
    lid = str(d.insert(qry1))
    qry="INSERT INTO `user`(`uname`,`place`,`district`,`email`,`image`,`phone`,`lid`)VALUES('"+username+","+place+","+district+","+email+","+path+","+phone+","+lid+"')"
    d=Db()
    res=d.insert(qry)
    return  jsonify(status='ok')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
