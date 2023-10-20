def to_camel_case(text: str):
    # if not text:
    #     return ""
    text = text.replace("_", " ").replace("-", " ").split(" ")
    return "".join([text[i].capitalize() if i != 0 else text[i] for i in range(len(text))])


print(to_camel_case(""))
