class ViewHelper(object):

    def show_menu(menu_list, name_of_menu: str):
        print(f"\n{name_of_menu}")
        number = 0
        for menu_item in menu_list:
            print(f" {number}: {menu_item}")
            number += 1

    def show_item(item):
        print(f"Item: {item}")

    def show_way(nodes: list):
        way = ""
        for node in nodes:
            way += f"{node} ->"
        print(way[:-3])

    def print_items(items: list):
        count = 1
        for item in items:
            print(f"{count}: {item}")
            count += 1

    def show_error(err: str):
        print(f"Error occured: {err}")

    def show_text(text: str):
        print(text)

    def print_line():
        print('==============================================================================')

    def print_list(list_name, list):
        print(list_name)
        print('------------------------')
        count = 1
        self.print_items(list)
