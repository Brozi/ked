import xml.dom.minidom as md

"""
1. Stworzyć obiekt json (co najmniej 10 pól)
2. W skrypcie Pythona stworzyć słownik na podstawie tego obiektu json
3. Na podstawie słownika stworzyć obiekt xml (bezpośrednio lub klasą wrappera)
4. Zapisać obiekt xml do pliku
"""

myDict = {"a": [1, {"ba": [3, [4, 5]], "ve": {"x": 5, "y": 5}}], "b": 2}


myXML = md.Document()
myRoot = myXML.createElement("root")
myXML.appendChild(myRoot)


def create_tag(name, value, parent):

    def create_tags(tags, i_parent):
        for n, v in enumerate(tags):
            if type(v) == dict:
                create_tag(f"tag_{n}", v, i_parent)
                continue
            i_tag = myXML.createElement(f"tag_{n}")
            i_parent.appendChild(i_tag)
            if type(v) == list:
                create_tags(v, i_tag)
            else:
                i_content = myXML.createTextNode(str(v))
                i_tag.appendChild(i_content)

    tag = myXML.createElement(name)
    parent.appendChild(tag)
    if type(value) == dict:
        for v_key, v_val in value.items():
            create_tag(v_key, v_val, tag)
    elif type(value) == list:
        create_tags(value, tag)
    else:
        content = myXML.createTextNode(str(value))
        tag.appendChild(content)


for key, val in myDict.items():
    create_tag(key, val, myRoot)

print(myXML.toprettyxml())
fh = open("test.xml", "w")
myXML.writexml(fh, addindent="\t", newl="\n")
fh.close()
