"""
MDH backend containers healthcheck worker
"""
import threading
from worker import elsa_docker_event_worker, elsa_health_check_worker
if __name__ == '__main__':
    elsa_docker_worker = threading.Thread(target=elsa_docker_event_worker)
    elsa_docker_worker.start()
    elsa_health_check_worker()
