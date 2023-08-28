dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
dansk = {"Danmark": "Köpenhamn"}
dic.update(dansk)
dic.pop("Finland")
print(dic)