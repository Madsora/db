from link_class import Link
import requests
from lxml import html
from typing import List
from lxml import etree as ET
from result_class import Result

def parse_all_links(links_list, max_links=20):
    parsed_links = 0

    for tmp_link in links_list:
        if tmp_link.is_parsed:
            parsed_links += 1
    return parsed_links < max_links

def get_unparsed_link(links_list):
    for tmp_link in links_list:
        if not tmp_link.is_parsed:
            return tmp_link

    raise Exception("Can't find links to parse!")

def filter_for_available_links(links_list: list):
    return list(filter(lambda link_url: link_url.startswith('http') and 'ostriv.in.ua' in link_url, links_list))

def fill_links_list(links_list: list, links_store: list):
    for link_url in links_list:
        filename = link_url.split('/')[-1]
        add_to_list(Link(link_url, filename), links_store)

def add_to_list(link_obj: Link, storage: list):
    for tmp_link in storage:
        if tmp_link.url == link_obj.url:
            return

    storage.append(link_obj)

def create_tree(url: str, filename=None):
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    html_raw = response.text

    tree = html.fromstring(html_raw)

    return tree

def create_text(fragment, text_lines):
    for line in text_lines:
        text_fragment = ET.SubElement(fragment, 'text_line')
        text_fragment.text = line

def create_img(fragment, images):
    for img in images:
        img_fragment = ET.SubElement(fragment, 'img_url')
        img_fragment.text = img

def create_xml_tree_task(results: List[Result]):
    root = ET.Element('data')

    for result in results:
        page = ET.SubElement(root, 'page')
        page.set('url', result.url)

        text_fragment = ET.SubElement(page, 'fragment')
        text_fragment.set('len', str(len(result.text)))
        text_fragment.set('type', 'text')
        create_text(text_fragment, result.text)

        img_fragment = ET.SubElement(page, 'fragment')
        img_fragment.set('len', str(len(result.images)))
        img_fragment.set('type', 'image')
        create_img(img_fragment, result.images)

    tree = ET.ElementTree(root)
    return tree

def save_to_xml_file(filename, tree):
    return tree.write(filename, pretty_print=True, xml_declaration=True, encoding="utf-8")