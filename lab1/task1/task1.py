from link_class import Link
import requests
from lxml import html
from typing import List
from lxml import etree
from result_class import Result

def parse_all_links(links_list, max_links):
    counter = 0

    for tmp_link in links_list:
        if tmp_link.is_parsed:
            counter += 1
    if counter < max_links:
        return True
    else:
        return False

def get_unparsed_link(list_of_links):
    for link in list_of_links:
        if not link.is_parsed:
            return link

    raise Exception("There are no links to parse")

def filter_for_available_links(links_list: list):
    filtered_links_list = list(filter(lambda url: url.startswith('http') and 'ostriv.in.ua' in url, links_list))
    return filtered_links_list

def fill_links_list(links_list: list, links_store: list):
    for link_url in links_list:
        filename = link_url.split('/')[-1]
        link = Link(link_url, filename)
        for tmp_link in links_store:
            if tmp_link.url == link.url:
                return
            links_store.append(link)

def create_tree(url: str, filename=None):
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    html_raw = response.text
    tree = html.fromstring(html_raw)
    return tree

def create_text(fragment, text_lines):
    for line in text_lines:
        text_fragment = etree.SubElement(fragment, 'text')
        text_fragment.text = line

def create_img(fragment, images):
    for img in images:
        img_fragment = etree.SubElement(fragment, 'image')
        img_fragment.text = img

def create_xml_tree_task(results: List[Result]):
    root = etree.Element('data')

    for result in results:
        page = etree.SubElement(root, 'page')
        page.set('url', result.url)

        text_fragment = etree.SubElement(page, 'fragment')
        text_fragment.set('type', 'text')
        create_text(text_fragment, result.text)

        img_fragment = etree.SubElement(page, 'fragment')
        img_fragment.set('type', 'image')
        create_img(img_fragment, result.images)

    tree = etree.ElementTree(root)
    return tree

def save_to_xml_file(filename, tree):
    return tree.write(filename, pretty_print=True, xml_declaration=True, encoding="utf-8")