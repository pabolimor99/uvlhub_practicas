from locust import HttpUser, task, between
from core.environment.host import get_host_for_locust_testing

class WebsiteTestUser(HttpUser):
    """
    Igual que en el tutorial: tareas sencillas.
    En UVLHub, /notepad suele exigir login; por eso aceptamos 302 como correcto.
    """
    wait_time = between(1, 5)
    host = get_host_for_locust_testing()

    @task(2)
    def load_notepad(self):
        r = self.client.get("/notepad", allow_redirects=False)
        if r.status_code not in (200, 302):
            print(f"Error al cargar /notepad: {r.status_code}")
