import xml.dom.minidom as md
from pandas import read_csv, to_datetime
from math import nan as not_number


class MyXmlDom:
    def __init__(self, main_tag: str):
        self.document = md.Document()
        self.main_tag = self.document.createElement(main_tag)
        self.document.appendChild(self.main_tag)
        self.index = 0

    def create_row(self, tags: dict) -> None:
        row = self.document.createElement("row")
        row.setAttribute("id", str(self.index))
        self.main_tag.appendChild(row)
        self.index += 1
        if tags is None:
            return
        for key, value in tags.items():
            tag = self.document.createElement(key)
            content = self.document.createTextNode(str(value))
            tag.appendChild(content)
            row.appendChild(tag)

    def __str__(self) -> str:
        return self.document.toprettyxml()

    def write(self, file_handler) -> None:
        self.document.writexml(file_handler, addindent=" ", newl="\n")


def create_xml(source_file: str) -> None:
    document = MyXmlDom("data")

    frame = read_csv(source_file, header=0, usecols=[2, 3, 4], names=["d", "v", "q"], index_col=False)
    frame = frame.apply(lambda x: to_datetime(x, format="%Y%m%d") if x.name == "d" else x)
    frame = frame.apply(lambda x: x/10 if x.name == "v" else x)
    frame = frame.replace(-999.9, not_number)

    for id_row in range(len(frame)):
        date, value, quality = frame.iloc[id_row]
        document.create_row({"date": date.date(), "temperature": value, "quality": quality})

    print(document)
    output_file = f"{source_file.partition('.')[0]}.xml"
    with open(output_file, "w") as file:
        document.write(file)

