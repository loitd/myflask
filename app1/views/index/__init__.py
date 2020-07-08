from app1.views import oraPool
from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from lutils.lutils import printlog, printwait
import cx_Oracle
from app1.views.login import login_required

# https://flask.palletsprojects.com/en/1.1.x/blueprints/
# Define the BLUEPRINT here
index_blp = Blueprint('index_blp', __name__)

# @app.route('/', methods = ['GET'])
@index_blp.route('/', methods = ['GET'])
def index():
    if 'email' in session:
        _sessionemail = session['email']
        return render_template('home/index.html')
    else:
        return redirect(url_for('login_blp.getLogin'))

@index_blp.route('/hello', methods=['GET'])
@login_required
def hello():
    return render_template('home/index.html')

# http://58.187.9.49:9001/getreversals/20191201/20191212
@index_blp.route('/getreversals/<fromdate>/<todate>/<gateway>', methods=['GET'])
def getReversals(fromdate, todate, gateway):
    try:
        if gateway == "cbsvtb":
            sql1 = """SELECT TRX_ID from REPORTER.NPG_TRX_INTERNATIONAL_FAIL AA
        WHERE AA.TRX_DT BETWEEN '{0}' AND '{1}' AND AA.PG_ERROR_CD = '481' AND (AA.STATUS IS NULL OR AA.STATUS = '0') 
        AND AA.BANK_ID = 'VTBM' 
        MINUS SELECT TRX_ID FROM REPORTER.TBL_INTERNATIONAL_REVERSAL""".format(fromdate, todate)
        elif gateway in ["cbsscb", "cbsscb3sc", "cbsscb2sc"]:
            sql1 = """SELECT TRX_ID from REPORTER.NPG_TRX_INTERNATIONAL_FAIL AA
        WHERE AA.TRX_DT BETWEEN '{0}' AND '{1}' AND AA.PG_ERROR_CD = '481' AND (AA.STATUS IS NULL OR AA.STATUS = '0') 
        AND AA.BANK_ID = 'STBM' 
        MINUS SELECT TRX_ID FROM REPORTER.TBL_INTERNATIONAL_REVERSAL""".format(fromdate, todate)
        else:
            return json.dumps({"result":"failed", "msg":"Unknown gateway"})
        try:
            oraConn = oraPool.acquire()
            printlog("[updateReversal] Acquired Oracle connection from pool", "monitordb.log")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            printlog("Oracle-Error-Code: {0}".format(error.code), "monitordb.log")
            printlog("Oracle-Error-Message: {0}".format(error.message), "monitordb.log")
            raise(e)
        oraCurs = oraConn.cursor()
        oraCurs.execute(sql1)
        rows = oraCurs.fetchall()
        resp = {"responsecode": 1, "trxid": rows, "message":"Get reversal successfully"}
    except Exception as e:
        resp = {"responsecode": 0, "message":"Get reversal failed: {0}".format(e)}
        raise(e)
    finally:
        oraPool.release(oraConn)
        return json.dumps(resp)

# http://58.187.9.49:9001/updatereversal/BA123456
@index_blp.route('/updatereversal/<trxid>', methods=["GET"])
def updateReversal(trxid):
    try:
        sql = """INSERT INTO REPORTER.TBL_INTERNATIONAL_REVERSAL(TRX_ID) VALUES ('{0}')""".format(trxid)
        oraConn = oraPool.acquire()
        printlog("[updateReversal] Acquired connection from pool", "monitordb.log")
        oraCurs = oraConn.cursor()
        oraCurs.execute(sql)
        oraConn.commit()
        resp = {"responsecode": 1, "trxid": trxid, "message":"Update reversal successfully"}
    except Exception as e:
        resp = {"responsecode": 0, "trxid": trxid, "message":"Update reversal failed: {0}".format(e)}
        raise(e)
    finally:
        oraPool.release(oraConn)
        return json.dumps(resp)
        

    