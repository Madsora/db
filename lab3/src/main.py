
from controller.controller import Controller
from controller.EmulationController import EmulationController
from controller.Neo4jController import Neo4jController
from view import ViewHelper
from faker import Faker
import random


def emulation():

    fake = Faker()
    users_amount = 10
    users = [fake.profile(fields=['username'], sex=None)['username'] for u in range(users_amount)]
    threads = []
    try:

        for i in range(users_amount):
            threads.append(EmulationController(users[i], users, users_amount, random.randint(1, 2)))
        for thread in threads:
            thread.start()

    except Exception as e:
        ViewHelper.show_error(str(e))
    finally:
        for thread in threads:
            if thread.is_alive():
                thread.stop()


if __name__ == "__main__":
    choice = Controller.make_choice(["Neo4j", "Emulation(use one time with worker for generate db)"], "Program mode")
    if choice == 0:
        Neo4jController()
    elif choice == 1:
        emulation()
