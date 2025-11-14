thonimport json
import pandas as pd
from xml.etree.ElementTree import Element, SubElement, tostring

class Exporter:
    @staticmethod
    def to_json(data, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def to_csv(data, path):
        df = pd.DataFrame(data)
        df.to_csv(path, index=False)

    @staticmethod
    def to_xml(data, path):
        root = Element("profiles")
        for item in data:
            entry = SubElement(root, "profile")
            for k, v in item.items():
                child = SubElement(entry, k)
                child.text = str(v)
        xml_string = tostring(root, encoding="unicode")
        with open(path, "w", encoding="utf-8") as f:
            f.write(xml_string)

    @staticmethod
    def to_html(data, path):
        df = pd.DataFrame(data)
        df.to_html(path, index=False)