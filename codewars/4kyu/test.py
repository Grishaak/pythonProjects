import datetime
import json
from json import JSONEncoder, JSONDecoder


class Product:
    def __init__(self, name: str, description: str, quantity: int):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.date = str(datetime.datetime.now())

    def __str__(self):
        return f"Название: {self.name}\n" \
               f"Описание: {self.description}\n" \
               f"Кол-во: {self.quantity}"


class ProductNote:
    def __init__(self):
        self.dict = dict()
        self.index = 0

    def add_prod(self, name, decr, quant):
        self.dict[self.index] = Product(name, decr, quant)
        self.index += 1

    def __str__(self):
        return "Okey you got it"


class ProductEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def from_json(json_object):
    if 'name' in json_object:
        return Product(json_object['name'], json_object["description"], json_object["quantity"])


# print(type(product_cheese))
# print(type(product_encoded))

exepl = ProductNote()
exepl.add_prod("Сыр", "козий сыр", 100)
exepl.add_prod("Мыр", "козий вкусный мыр", 200)

data = []
for v in exepl.dict.values():
    data.append(v)

print(data)

with open("file_json", "w") as fp:
    for product in exepl.dict.values():
        product_encoded = json.dumps(product, cls=ProductEncoder)
        print(product_encoded)
        fp.writelines(product_encoded)
        fp.writelines("\n")

with open("file_json", "r") as r:
    for i in range(len(data)):
        loaded_file = r.readline()
        print(loaded_file)
        product = JSONDecoder(object_hook=from_json).decode(loaded_file)
        exepl.dict[i] = product
data_loaded = exepl.dict
print(data_loaded)

# product = JSONDecoder(object_hook=from_json).decode(loaded_file)
# product_decoded = json.loads(data_loaded)
print(type(exepl.dict))
print(data_loaded)

end_text = []
text = "Меня зовут Иван Караван я из Перьми живу рядом в доме 34 на улиуе Роггожина Вени. Питаюсь морквой и всякими другими овощами."
count = 0
for i in text:
    if i == " " and count >= 40:
        end_text.append("\n")
        count = 0
    else:
        count += 1
        end_text.append(i)
x = "".join(end_text)
print(x)
