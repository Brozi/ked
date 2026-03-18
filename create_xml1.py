import xml.dom.minidom as md

"""
1. Stworzyć obiekt json (co najmniej 10 pól)
2. W skrypcie Pythona stworzyć słownik na podstawie tego obiektu json
3. Na podstawie słownika stworzyć obiekt xml (bezpośrednio lub klasą wrappera)
4. Zapisać obiekt xml do pliku
"""

class NewXMLDom:

    def __init__(self, main_tag: str):
        self.document = md.Document()
        self.main_tag = self.document.createElement(main_tag)
        self.document.appendChild(self.main_tag)

    def create_tag(self, tag_name: str, value: dict, parent_tag=None) -> None:
        tag = self.document.createElement(tag_name)
        if parent_tag is None:
            self.main_tag.appendChild(tag)
        else:
            parent_tag.appendChild(tag)
        if type(value) == dict:
            for key, val in value.items():
                self.create_tag(key, val, parent_tag=tag)
        elif type(value) == list:
            for val in value:
                extra_tag = self.document.createElement(f"list_tag")
                tag.appendChild(extra_tag)
                if type(val) == dict:
                    for key, v in val.items():
                        self.create_tag(key, v, parent_tag=extra_tag)
                else:
                    content = self.document.createTextNode(str(val))
                    extra_tag.appendChild(content)
        else:
            content = self.document.createTextNode(str(value))
            tag.appendChild(content)
