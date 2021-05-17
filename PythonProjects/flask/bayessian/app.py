import pandas as pd
from flask import Flask, render_template, request, jsonify, send_file, redirect, json
# from werkzeug import secure_filename
import random
import csv as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import os, time
import xlrd
# import seaborn as sns
from textblob import TextBlob
# from flask_mysqldb import MySQL
app = Flask(__name__)
# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='Ayodele1'
# app.config['MYSQL_DB']='classifier'
# mysql=MySQL(app)
usersecret='admin'


@app.route('/')
def index():
    return  render_template('index.html')


@app.route('/sampledata')
def sampledata():
    data=pd.read_csv('static/document/uploadedfiles/sample.csv')
    data=pd.DataFrame(data)
    return data.to_html()

@app.route('/checkperformance', methods=['POST'])
def checkperformance():
    json_data=[]
    message={
        "msg":"norecord"
    }
    getvalue=request.form
    matricno=getvalue['matricno']
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT * FROM result_tbl WHERE matricno=%s", (matricno, ))
    # res=cur.execute(query, (matricno, ))
    if res > 0:
        row_headers=[x[0] for x in cur.description]
        rv = cur.fetchall()
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    return json.dumps(message)
    #     return  render_template('checkresult.html', result='No records found')
    # data=cur.fetchall()[0]
    # cur.close()
    # path='static/document/uploadedfiles/'+data[0]
    # getfile=pd.read_csv(path, delimiter=',')
    # res=getfile
    # sort=res[res['matricno'].str.match(matricno)]
    # sort['percentage%']=(sort['test']*0.4)+(sort['exam']*0.6)
    # sort.drop(sort.filter(regex="Unname"),axis=1, inplace=True)
    # return render_template('checkresult.html', result=sort.to_html(classes='itemlist'))

@app.route('/classfetch', methods=['POST'])
def classfetch():
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT levelname FROM category")
    if res > 0:
        data=cur.fetchall()
        cur.close()
        return jsonify(data)

@app.route('/uploadresult')
def uploadresult():
        return  render_template('uploadresult.html')

@app.route('/performance')
def performance():
        return  render_template('performance.html')

# @app.route('/checkresult')
# def checkresult():
#     cur=mysql.connection.cursor()
#     res=cur.execute("SELECT * FROM __level")
#     if res > 0:
#         data=cur.fetchall()
#         cur.close()
#     return  render_template('checkresult.html', classlist=data)

# @app.route('/uploadclass')
# def uploadclass():
#     cur=mysql.connection.cursor()
#     res=cur.execute("SELECT * FROM __level")
#     if res > 0:
#         data=cur.fetchall()
#         cur.close()
#         return render_template('uploadclass.html', classlist=data)

@app.route('/uploadfile', methods=['POST'])
def uploadfile():
    getvalue=request.form
    classid=getvalue['cid']
    session=getvalue['session']
    semester=getvalue['semester']
    getfile=request.files['filename']
    filename=getfile.filename
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT * FROM course_tbl WHERE classid=%s and session=%s and semester=%s", (classid, session, semester))
    if res > 0:
        return 'exist'
    randomnum=random.randint(1, 99999)
    getfile.save(os.path.join('static/document/uploadedfiles/', str(randomnum)+filename))
    filepath='static/document/uploadedfiles/'+str(randomnum)+filename
    res=cur.execute("INSERT INTO course_tbl(classid, session, semester, filename, dateCreated) VALUES(%s, %s, %s, %s, %s)", (classid, session, semester,  str(randomnum)+filename, dateCreated))
    if res:
       fileuploader(filepath)
       return 'created'


# @app.route('/fileuploader')
def fileuploader(file_name):
    cur=mysql.connection.cursor()
    book=xlrd.open_workbook(file_name)
    sheet=book.sheet_by_name('Sheet3')
    query="""INSERT INTO registration(SessionID, SemesterID, CourseCode, Courseid, ContinuosAssesment, Exam,
    Score, Grade, CourseUnit, ProgrammeID, LevelID, MatricNo, CPoint, SemID, DateCreated, TimeCreated,
    AStatus, ProgrammeTypeID, ProgrammeID2, DeptId)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    for r in range(1, sheet.nrows):
        SessionID=sheet.cell(r, 0).value
        SemesterID=sheet.cell(r, 1).value
        CourseCode=sheet.cell(r, 2).value
        Courseid=sheet.cell(r, 3).value
        ContinuosAssesment=sheet.cell(r, 4).value
        Exam=sheet.cell(r, 5).value
        Score=sheet.cell(r, 6).value
        Grade=sheet.cell(r, 7).value
        CourseUnit=sheet.cell(r, 8).value
        ProgrammeID=sheet.cell(r, 9).value
        LevelID=sheet.cell(r, 10).value
        MatricNo=sheet.cell(r, 11).value
        CPoint=sheet.cell(r, 12).value
        SemID=sheet.cell(r, 13).value
        DateCreated=sheet.cell(r, 14).value
        TimeCreated=sheet.cell(r, 15).value
        AStatus=sheet.cell(r, 16).value
        ProgrammeTypeID=sheet.cell(r, 17).value
        ProgrammeID2=sheet.cell(r, 18).value
        DeptId=sheet.cell(r, 19).value
        values = (SessionID, SemesterID, CourseCode, Courseid,ContinuosAssesment,
        Exam, Score, Grade, CourseUnit, ProgrammeID, LevelID, MatricNo, CPoint,
        SemID, DateCreated, TimeCreated, AStatus, ProgrammeTypeID, ProgrammeID2, DeptId)
        cur.execute(query, values)
    cur.close()
    mysql.connection.commit()

# upload result file here
@app.route('/uploadresfile', methods=['POST'])
def uploadresfile():
    getvalue=request.form
    classid=getvalue['classnameid']
    getfile=request.files['filename']
    filename=getfile.filename
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    cur=mysql.connection.cursor()
    randomnum=random.randint(1, 99999)
    getfile.save(os.path.join('static/document/uploadedfiles/', str(randomnum)+filename))
    filepath='static/document/uploadedfiles/'+str(randomnum)+filename
    res=cur.execute("INSERT INTO resultfile_tbl(classid, filename, dateCreated) VALUES(%s, %s, %s)", (classid,  str(randomnum)+filename, dateCreated))
    if res:
       fileuploaderforres(filepath, classid)
       return 'created'

def fileuploaderforres(file_name, classid):
    cur=mysql.connection.cursor()
    book=xlrd.open_workbook(file_name)
    sheet=book.sheet_by_name('Sheet1')
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    query="""INSERT INTO result_tbl(cid,text,dateCreated)
    VALUES(%s, %s, %s)"""
    for r in range(1, sheet.nrows):
        text=sheet.cell(r, 1).value
        values = (classid, text, dateCreated)
        cur.execute(query, values)
    cur.close()
    mysql.connection.commit()


@app.route('/dashboard')
def dashboard():
    return render_template('indexe.html')

@app.route('/authentication', methods=['POST', 'GET'])
def authentication():
    getvalue=request.form
    res=getvalue['adminid']
    if res == usersecret:
        return redirect("/dashboard", code=302)
    return render_template('index.html', errormessage='Invalid userID')

@app.route('/uploader', methods=['post'])
def fileupload():
    if request.method=='post':
        f=request.files['filename']
        filenm=f.filename
        f.save(os.path.join('static/document/uploadedfiles', secure_filename(filenm)))
        return 'successfully uploaded'
    return 'this is not a post method'

@app.route("/feedback")
def feedback():
    return render_template('feedback.html')

@app.route("/createclass?levelname=")
def createclass():
    return render_template('createclass.html')

@app.route("/uploadcourse")
def uploadcourse():
    return render_template('uploadcourse.html')

@app.route("/insertclass", methods=['POST'])
def insertclass():
    if request.method=='POST':
        msg=[]
        post=request.form
        levelname=post['levelname']
        dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
        cur=mysql.connection.cursor()
        res=cur.execute("SELECT * FROM level WHERE levelname=%s", (levelname,))
        if res > 0:
            msg.append('exist')
            return jsonify(msg)
        cur.execute("INSERT INTO level(levelname, status, dateCreated) VALUES(%s, %s, %s)", (levelname, 1, dateCreated))
        mysql.connection.commit()
        msg.append('created')
        return jsonify(msg)

@app.route("/listdata", methods=['POST'])
def listdata():
    json_data=[]
    if request.method=='POST':
        cur=mysql.connection.cursor()
        post=request.form
        tablename=post['tablename']
        ids=post['id']
        res=''
        if tablename=='leveldata':
            res=cur.execute("SELECT * FROM level ORDER BY id DESC")
        elif tablename=='couseupload':
            res=cur.execute("SELECT c.classid, c.id, l.levelname, c.dateCreated, c.filename FROM course_tbl c INNER JOIN level l on l.id=c.classid ORDER BY c.id DESC")
        elif tablename=='resultdata':
            res=cur.execute("SELECT c.classid, c.id, l.levelname, c.dateCreated, c.filename FROM resultfile_tbl c INNER JOIN level l on l.id=c.classid ORDER BY c.id DESC")
        elif tablename=='viewdata':
            res=cur.execute("SELECT c.id, l.levelname, c.text, c.dateCreated FROM result_tbl c INNER JOIN level l on l.id=c.cid WHERE c.cid=%s", (ids, ))
        elif tablename=='feedback':
            db=MySQLdb.connect("localhost", "root", "Ayodele1", "ecomm")
            cur=db.cursor()
            res=cur.execute("SELECT * FROM feedback_tbl")
        if res > 0:
            row_headers=[x[0] for x in cur.description]
            rv = cur.fetchall()
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)

@app.route("/trash", methods=['POST'])
def trash():
    if request.method=='POST':
        msg=[]
        query=''
        post=request.form
        ids=post['id']
        tdname=post['tdname']
        cur=mysql.connection.cursor()
        if tdname=="trashlevel":
            query="DELETE FROM level WHERE id = %s"
        elif tdname=="trashcourse":
            query="DELETE FROM resultfile_tbl WHERE id = %s"
        elif tdname=="trashtext":
            query="DELETE FROM result_tbl WHERE id = %s"
        res=cur.execute(query, (ids, ))
        if res:
            mysql.connection.commit()
            return jsonify("deleted")
        return jsonify("failed")

@app.route('/listoption', methods=['POST'])
def listoption():
    json_data=[]
    message={
        "msg":"norecord"
    }
    if request.method=='POST':
        cur=mysql.connection.cursor()
        res=cur.execute("SELECT * FROM level ORDER BY id DESC")
        if res > 0:
            row_headers=[x[0] for x in cur.description]
            rv = cur.fetchall()
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            return json.dumps(json_data)
        return json.dumps(message)


@app.route('/analysis', methods=['POST'])
def analysis():
    positive=0
    negative=0
    neutral=0
    polarity=0
    count=0
    feedback=[]
    post=request.form
    ids=post['data']
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT * FROM result_tbl WHERE cid=%s", (ids,))
    res=cur.fetchall()
    df=pd.DataFrame(res)
    for row in df[2]:
        feedback.append(row)
    for lineoftext in feedback:
        count+=1
        analysis=TextBlob(lineoftext)
        polarity+=analysis.sentiment.polarity
        if(analysis.sentiment.polarity == 0.00):
            neutral+=1
        elif(analysis.sentiment.polarity < 0.00):
            negative+=1
        elif(analysis.sentiment.polarity > 0.00):
            positive+=1
    positive =  100*float(positive)/float(count)
    negative =  100*float(negative)/float(count)
    neutral =   100*float(neutral)/float(count)
    positive = format(positive, '.2f')
    negative = format(negative, '.2f')
    neutral = format(neutral, '.2f')
    labels=['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]']
    sizes=[positive, neutral, negative]
    colors=['yellowgreen', 'gold', 'red']
    patches, texts=plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('Sentiment analysis system\nCustomer feedback chart\n Total number of feedback: '+str(count)+'')
    plt.axis('equal')
    plt.tight_layout()
    randomnum=random.randint(1, 99999)
    newfilename=str(randomnum)+'.png'
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    filepathnew='static/plots/'+str(randomnum)+'.png'
    cur.execute("INSERT INTO report_tbl(filename, dateCreated) VALUES(%s, %s)", (newfilename, dateCreated))
    mysql.connection.commit()
    cur.close()
    plt.savefig(filepathnew)
    plt.show()
    return 'created'


if __name__ == "__main__":
    app.run(debug=True)