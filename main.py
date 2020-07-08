from app1.views import app, oraPool
from lutils.lutils import printlog, printwait

if __name__ == "__main__":
    try:
        # debug = True to forece flask reload when code changed
        # app.config.from_object('config.DevelopmentConfig')
        app.run(host="0.0.0.0", port=9001, debug=True)
    except Exception as e:
        raise(e)
    finally:
        # Your destructor here
        printlog("Finally destructor called", "monitordb.log")
        oraPool.close()
    