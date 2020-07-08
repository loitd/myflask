from views import app, oraPool
from lutils.lutils import printlog, printwait

# HOW TO RUN:
# set FLASK_APP=runme.py
# python -m flask run --host=0.0.0.0 --port=9001
# python -m flask init-db

if __name__ == "__main__":
    try:
        # debug = True to forece flask reload when code changed
        # app.config.from_object('config.ProductionConfig')
        # app.run(host="0.0.0.0", port=9001, debug=True)
        pass
    except Exception as e:
        raise(e)
    finally:
        # Your destructor here
        printlog("Finally destructor called", "monitordb.log")
        oraPool.close()
        