from lxml import etree

def main():
    path='../task1/task1.xml'
    with open(path, 'r', encoding='utf-8') as xml_content:
        tree = etree.parse(xml_content)        
        page_url = tree.xpath(f"//page/@url")
        for url in page_url:
            print(url)
main()