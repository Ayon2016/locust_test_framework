from locust import User, task

class MyTest(User):
    
    @task
    def launch(self):
        print("Launching the URL")
        
    @task
    def search(self):
        print("Searching the URL")