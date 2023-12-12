import tkinter as tk

class TkJsonParser:
    def __init__(self, json, parent):      
        self._registry = {}
        self._element = self.parse_element(json, parent)

    def getItem(self, id) -> tk.Widget:
        return self._registry[id]

    def getElement(self) -> tk.Widget:
        return self._element

    def parse_element(self, json, parent) -> tk.Widget:
        item = None
        blockedKeys = [
            "type", "children", "id", "doLayout"
        ]

        if "_src" in json:
            args = {}
            if "args" in json:
                args = json["args"]
                json.pop("args")
            
            new = _parseJson(readFile(json["_src"]), args)
            json.pop("_src")
            new.update(json)
            return self.parse_element(new, parent)

        item = eval(f"tk.{json['type']}(parent)")
        
        for key in json.keys():
            if key not in blockedKeys:
                config = {}
                config[key] = json[key]
                try:
                    item.config(config)
                except Exception as e:
                    print(f"Erro: {e}")

        item.pack()

        if "doLayout" in json:
            doLayout = json["doLayout"]
            func = eval(f"item.{doLayout['type']}")
            doLayout.pop("type")
            func(doLayout)

        if "id" in json:
            self._registry[json["id"]] = item

        if "children" in json:
            for child in json["children"]:
                self.parse_element(child, item)

        return item


def _parseJson(source, args={}):
    true=True
    false=False
    return eval(source)

def readFile(path):
    file = open(path, mode="r",  encoding="utf-8")
    content = file.read()
    file.close()
    return content

def parseString(source, parent, args={}):
    return TkJsonParser(_parseJson(source, args), parent)

def parseFile(path, parent, args={}):
    return parseString(readFile(path), parent, args)

