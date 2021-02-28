import task1 as t1
from link_class import Link
from result_class import Result


def main():
    links = [
        Link('http://www.ostriv.in.ua', 'base')
    ]
    results = []
    while t1.parse_all_links(links, 20):
        try:
            link = t1.get_unparsed_link(links)
            tree = t1.create_tree(link.url, link.filename)

            available_links = t1.filter_for_available_links(tree.xpath('//a/@href'))

            unsorted_text_lines = \
                tree.xpath('body//*[not(self::script or self::style or self::img)]/text()')
            text = []
            for line in unsorted_text_lines:
                line = line.replace('\n', ' ').strip(', \n')
                if len(line):
                    text.append(line)

            images_url = tree.xpath('body//img/@src | body//img/@data-src')

            results.append(Result(link.url, text, images_url))

            link.set_parsed()
            t1.fill_links_list(available_links, links)
        except Exception as e:
            print(e)
            break

        xml_tree = t1.create_xml_tree_task(results)
        t1.save_to_xml_file('task1.xml', xml_tree)

main()