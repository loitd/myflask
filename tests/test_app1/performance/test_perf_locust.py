import random
from locust import HttpUser, task, between, User, TaskSet

class MyFlaskPerfTest(HttpUser):
    # Our class defines a wait_time function that will make the simulated users wait between 5 and 9 seconds after each task is executed
    wait_time = between(3, 9)

    @task
    def perf_auth_page(self):
        self.client.get("/reg")
        self.client.get("/login")

    # higher weight (3) with three times the chance of picking
    @task(1)
    def perf_login(self):
        # Test login fail
        data = dict( inputEmail="admin@myflask.com", inputPassword="123" )
        self.client.post("/login", data)
        
        # Test login success
        data = dict( inputEmail="admin@myflask.com", inputPassword="123456" )
        self.client.post("/login", data)
        
        # Test validation fail 1
        data = dict( inputEmail="a@ admin@myflask.com", inputPassword="123456" )
        self.client.post("/login", data)
        
        # Test validation fail 2
        data = dict( inputEmail="admin", inputPassword="123456" )
        self.client.post("/login", data)
        
        # item_id = random.randint(1, 10000)
        # self.client.get(f"/item?id={item_id}", name="/item")

    @task(1)
    def perf_register(self):
        data = dict( inputName="", inputEmail="admin@myflask.com", inputPassword="123" )
        self.client.post("/reg", data)
        
        data = dict( inputName="''''$'''", inputEmail="admin@myflask.com", inputPassword="123" )
        self.client.post("/reg", data)
        
        data = dict( inputName="usertest", inputEmail="a@admin@myflask.com", inputPassword="123" )
        self.client.post("/reg", data)
        
        _email = "test{0}test@myflask.com".format(random.randint(1, 10000))
        data = dict( inputName="usertest", inputEmail=_email, inputPassword="123123" )
        self.client.post("/reg", data)
        
    def on_start(self):
        # only methods decorated with @task will be called, so you can define your own internal helper methods any way you like.
        self.client.post("/login", {"username":"foo", "password":"bar"})