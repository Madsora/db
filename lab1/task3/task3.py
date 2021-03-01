from item_class import Item 
import requests
from lxml import html
from lxml import etree
from typing import List
from result_class import Result
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()

def create_tree(url: str, filename=None):
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    html_raw = response.text
    tree = html.fromstring(html_raw)

    return tree

def parse_item(link_item):
    driver.get(f'{link_item}')
    item_tree = create_tree(f'{link_item}')
    item_name = item_tree.xpath('//h1/text()')[0] or ''
    item_img =  item_tree.xpath("//span[@id='view_full_size']//img/@src")[0] or ''
    item_price = driver.find_element_by_xpath("//span[@class='price']").text or ''
    item_description = item_tree.xpath("//div[@class='rte']/p//text()")[0] or ''
    return Item(item_name, item_img, item_price, item_description)

def create_xml_tree(results: List[Item]):
    root = etree.Element('data')
    i = 0

    for result in results:
        item = etree.SubElement(root, 'item')
        item.set('index', str(i))
        img = etree.SubElement(item, 'img')
        img.text = result.img
        price = etree.SubElement(item, 'price')
        price.text = result.price
        description = etree.SubElement(item, 'description')
        description.text = result.description
        name = etree.SubElement(item, 'name')
        name.text = result.name
        i += 1
        
    tree = etree.ElementTree(root)
    return tree

def save_to_xml_file(filename, tree):
    return tree.write(filename, pretty_print=True, xml_declaration=True, encoding="utf-8")