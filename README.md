# tk-json
Create tkinter interfaces by a json file 

# Use Examples

## Hello World

[main.py]
```
import tkjson
import tkinter as tk

root = tk.Tk();

parser = tkjson.parseFile("./interface.json", root);

parser.getItem("MyLabel").config("text" = "Hello from Python");

root.mainloop();

```

[interface.json]

```
{
  "type": "Frame",
  "doLayout": {
    "type": "pack",
    "fill": tk.BOTH
  },
  "children": [
    {
      "type": "Button",
      "text": "Hello World"
    },
    {
      "id": "MyLabel",
      "type": "Label"
    }
  ]
}
```
