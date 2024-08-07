from locust import HttpUser, SequentialTaskSet, constant, task, between
from utils.commons import CsvReader

class MyApiTasks(SequentialTaskSet):
    
    # def on_start(self):
    #     # Perform the login or token retrieval
    #     response = self.client.post("/api/login", json={"username": "user", "password": "pass"})
    #     if response.status_code == 200:
    #         self.token = response.json().get("access_token")
    #         self.headers = {
    #             'Authorization': f'Bearer {self.token}',
    #             'Content-Type': 'application/json',
    #             'Custom-Header': 'CustomValue'
    #         }
    #         self.cookies = {
    #             'session_id': response.cookies.get('session_id')
    #         }
    #     else:
    #         self.token = None
    #         self.headers = {}
    #         self.cookies = {}
    
    @task
    def get_users(self):
        with self.client.get("/api/users?page=2", name="get_users", catch_response=True) as response:
            if response.status_code ==200:
                response.success()
            else:
                response.failure(f"get_users failed with status code {response.status_code}")
            
        
    @task 
    def post_users(self):
        test_data = CsvReader('/Users/ayon.choudhury/Desktop/Ayon_Self_Learning/Locust_Test_Framework/test_data/data.csv').read_file()
        print(test_data)
        input_data = {
            "name": test_data['name'],
            "job": test_data['job']
        }
        with self.client.post("/api/users", data = input_data, name=f"post_users for {test_data['name']}") as response:
            if response.status_code ==200:
                response.success()
            else:
                response.failure(f"post_users failed with status code {response.status_code}")
        
class MyTestRunner(HttpUser):

    #host = "https://reqres.in"
    tasks = [MyApiTasks]
    wait_time = between(1, 5)