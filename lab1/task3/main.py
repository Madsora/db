import task3 as t3

def main():
    list_of_items = []

    tree = t3.create_tree('https://www.fishing-mart.com.ua/')
    links_of_items = tree.xpath("//a[@class='product_img_link']/@href")


    for link in links_of_items:
        list_of_items.append(t3.parse_item(link))

    xml_tree = t3.create_xml_tree(list_of_items)
    t3.save_to_xml_file('task3.xml', xml_tree)

main()