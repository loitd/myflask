from app1 import create_app
  
app = create_app()
app.run(host="127.0.0.1", port=9001, debug=True)