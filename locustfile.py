from locust import HttpUser, task, between

class FlaskML_Home(HttpUser): 
    wait_time = between(1, 5)

    @task
    def flask_home(self):
        self.client.get(url='/')
    @task
    def flask_predict(self):
        self.client.get(url='/predict')
