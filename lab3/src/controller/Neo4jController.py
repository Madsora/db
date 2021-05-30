from controller.Controller import Controller
from servers.neo4j_server.Neo4jServer import Neo4jServer
from view import ViewHelper


class Neo4jController(object):
    def __init__(self):
        self.__server = Neo4jServer()
        self.__menu = 'Neo4j menu'
        self.loop = True
        self.start()

    def start(self):
        from data import menu_list
        try:
            while self.loop:
                choice = Controller.make_choice(menu_list[self.__menu].keys(), self.__menu)
                Controller.considering_choice(self, choice, list(menu_list[self.__menu].values()))
        except Exception as e:
            ViewHelper.show_error(str(e))

    def get_users_with_tagged_messages(self):
        res = self.__server.get_users_with_tagged_messages(*Controller.get_func_arguments(
            self.__server.get_users_with_tagged_messages))
        ViewHelper.print_list("Users: ", res)

    def shortest_way_between_users(self):
        res = self.__server.shortest_way_between_users(*Controller.get_func_arguments(
            self.__server.shortest_way_between_users))
        ViewHelper.show_way(res)

    def get_users_with_n_long_relations(self):
        res = self.__server.get_users_with_n_long_relations(*Controller.get_func_arguments(
            self.__server.get_users_with_n_long_relations))
        ViewHelper.print_list("Pairs of users: ", res)

    def get_users_wicth_have_only_spam_conversation(self):
        res = self.__server.get_users_wicth_have_only_spam_conversation()
        ViewHelper.print_list("Pairs of users: ", res)

    def get_unrelated_users_with_tagged_messages(self):
        res = self.__server.get_unrelated_users_with_tagged_messages(*Controller.get_func_arguments(
            self.__server.get_unrelated_users_with_tagged_messages))
        ViewHelper.print_list("Groups of unrelated users: ", res)

