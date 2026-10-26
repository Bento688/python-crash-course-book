"""Build a person"""


def build_person(first_name: str, last_name: str, age = None):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix")
musician2 = build_person("Michael", "Jackson", 32)
print(musician)
print(musician2)
