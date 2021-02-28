from item_class import Item 
import requests
from lxml import html
from lxml import etree as ET
from typing import List
from result_class import Result

def create_tree(url: str, filename=None):
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    html_raw = response.text
    tree = html.fromstring(html_raw)

    return tree

def parse_good(link_item):
    item_tree = create_tree(f'{link_item}')
    item_name = item_tree.xpath('//h1/text()')[0] or ''
    item_img =  item_tree.xpath("//span[@id='view_full_size']//img/@src")[0] or ''
    item_price = item_tree.xpath("//span[@id='our_price_display']/text()")[0] or ''
    item_description = item_tree.xpath("string(//div[@class='rte'])") or ''
    return Item(item_name, item_img, item_price, item_description)

def create_xml_tree(results: List[Item]):
    root = ET.Element('data')
    i = 0

    for result in results:
        item = ET.SubElement(root, 'item')
        item.set('index', str(i))

        img = ET.SubElement(item, 'img')
        img.text = result.img

        price = ET.SubElement(item, 'price')
        price.text = result.price

        description = ET.SubElement(item, 'description')
        description.text = result.description

        name = ET.SubElement(item, 'name')
        name.text = result.name

        i += 1

    tree = ET.ElementTree(root)
    return tree

def save_to_xml_file(filename, tree):
    return tree.write(filename, pretty_print=True, xml_declaration=True, encoding="utf-8")