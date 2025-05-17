"""dict1 = {
    "hassan": "toufeeq",
    "jan": "khan",
    "age": 23

}
print(dict1)





dict2 = {
    "name": "hassan",
    "subjict": ["math", "coputer", "science"],
    "topic": ("writing", "mobale")

}
print(dict2)
print(type(dict2))
print(dict2["topic"])
print(dict2["subjict"])
print(dict2["name"])
dict2["name"] = "jan"
print(dict2)





null_dic = {
    "name": "khan"

}
print(null_dic)




dict3 = {
    "name": "hassan",
    "subject": {
        "phy": 45,
        "english": 89,
        "math": 78

    }
}
print(dict3)
print(dict3["subject"]["phy"])
print(dict3.keys())
print(list(dict3.keys()))
print(dict3.values())
print(dict3.items())
print(dict3.get("subject"))
dict3.update({"city": "hungu"})
print(dict3)



dict4 = {
    "table": ["hassan", "jan", "khan"],
    "subject": "phy"

}
print(dict4)

dict5 = {
    "class": ["python", "javascip", "c++", "c", "java"]
}
print(len(dict5))"""


marks = {}
x = int(input("enter phy:"))
marks.update({"phy": x})
x = int(input("enter math:"))
marks.update({"math": x})
x = int(input("enter che:"))
marks.update({"che": x})
print(marks)
