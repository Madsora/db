import lxml.etree as ET


def save_to_xml_file(filename, tree):
    return tree.write(filename, pretty_print=True, xml_declaration=True, encoding="utf-8")

def main():
    dom = ET.parse('../task3/task3.xml')
    xslt = ET.parse('task4.xsl')
    transform = ET.XSLT(xslt)
    html_dom = transform(dom)
    save_to_xml_file('task4.html' ,html_dom )

main()