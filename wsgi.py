from app1 import create_app
  
app = create_app()
app.run(host="0.0.0.0", port=9001, debug=True)