from locust import HttpUser, TaskSet, constant, task

class MyApiTasks(TaskSet):
    
    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        
    @task 
    def post_users(self):
        res = self.client.post("/api/users", data = {"name": "Test","job": "User"})
        
class MyTestRunner(HttpUser):

    host = "https://reqres.in"
    tasks = [MyApiTasks]
    wait_time = constant(1)