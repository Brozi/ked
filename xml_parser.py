from xml.dom.minidom import parse, Document, Element


def load_xml(filename: str) -> Document:
    try:
        dom = parse(filename)
    except Exception as e:
        dom = Document()
        print(f"{filename} nie jest poprawnym dokumentem XML. Błąd: {e}")
    return dom


def print_folder_tree(element: Element, indent: int = 0) -> None:
    attributes = ''
    if len(element.attributes) > 0:
        attributes = " ("
        for name, value in element.attributes.items():
            attributes += f"{name}='{value}', "
        attributes = attributes[:-2] + ")"
    tag_name = element.tagName
    text_content = element.firstChild.data.strip() if element.firstChild else ''
    if text_content != '':
        text_content = ": " + text_content
    print(" " * indent + f"{tag_name}{attributes}{text_content}")
    for child in element.childNodes:
        if child.nodeType == child.ELEMENT_NODE:
            print_folder_tree(child, indent=indent+4)


def count_nodes(element: Element) -> int:
    count = 1
    for child in element.childNodes:
        if child.nodeType == child.ELEMENT_NODE:
            count += count_nodes(child)
    return count


def count_attributes(element: Element) -> int:
    count = len(element.attributes)
    for child in element.childNodes:
        if child.nodeType == child.ELEMENT_NODE:
            count += count_attributes(child)
    return count


xml_file = "timetable.xml"  # Nazwę pliku należy zmienić na własną!
xml_dom = load_xml(xml_file)
root = xml_dom.documentElement
print(f"Liczba węzłów w dokumencie {xml_file}: {count_nodes(root)}")
print(f"Liczba wszystkich atrybudów w dokumencie {xml_file}: {count_attributes(root)}")
print_folder_tree(root)

