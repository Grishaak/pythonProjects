url = "https://www.pippi.pi/giacomo-sorbi.php"


def generate_bc(url, separator):
    words = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]
    new_words = [".html", ".htm", ".php", ".asp"]
    comms = ["www.", ".com", "https", "http"]
    url = url.replace("/", " ").replace("?", " ").split()
    print(url)
    for i in comms:
        for j in range(len(url)):
            if i in url[j]:
                url.remove(url[j])
                break
    for i in url:
        if "=" in i:
            url.remove(i)
    print(url)
    new_url = url.copy()
    print(new_url)
    if len(new_url) < 1:
        return f'<span class="active">HOME</span>'
    for i in range(len(new_url)):
        new_url[i] = new_url[i].replace("-", " ")
        new_url[i] = new_url[i].split()
    new_list = []
    for j in new_url:
        for i in words:
            if i in j:
                j.remove(i)
        if len("".join(j)) >= 30:
            word = [i[0] for i in j]
            word = "".join(word).upper()
            new_list.append(word)
    # print(new_list)
    print(new_url)
    if "index" in url[len(url) - 1]:
        url.pop(len(url) - 1)
    for i in new_words:
        if i in url[len(url) - 1]:
            url[len(url) - 1] = url[len(url) - 1].replace(i, "")
    print(url)
    # print(new_list)
    # print(new_url)
    others_list = []
    other_word = ""
    word = ""
    if len(url[:len(url) - 1]) >= 2:
        for i in range(len(url[:len(url) - 1])):
            if i != 0:
                word += f'/{url[i]}'
                other_word = f'<a href="/{word}/">{url[i].upper()}</a>'
                others_list.append(other_word)
            else:
                other_word = f'<a href="/{url[i]}/">{new_list[0].upper() if new_list else url[i].upper()}</a>'
                others_list.append(other_word)
                word += f'{url[i]}'
    # print(len(url))
    # print(word)
    # print(other_word)
    # print(others_list)
    # if len(url) < 3:
    home = f'<a href="/">HOME</a>'
    if others_list:
        body = separator.join(others_list)
    # print(body)
    else:
        body = f'<a href="/{url[len(url) - 2]}/">{new_list[0].upper() if new_list else url[len(url) - 2].upper()}</a>'
    span = f'<span class="active">{url[len(url) - 1].upper().replace("-", " ")}</span>'

    list = [home, body, span]
    not_list = [home, span]
    # print('<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * <a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>')
    return separator.join(list) if not len(url) < 2 else separator.join(not_list)


print(generate_bc(url, " * "))
