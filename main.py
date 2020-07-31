from app1 import create_app
from lutils.utils import printlog, printwait

if __name__ == "__main__":
    try:
        app = create_app()
        app.run(host="0.0.0.0", port=9001, debug=True)
    except Exception as e:
        raise(e)
    finally:
        # Your destructor here
        print("[Main] Finally destructor called")
    