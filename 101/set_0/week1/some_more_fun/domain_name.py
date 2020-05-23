def domain_name(dom):
    words = dom.split('.')
    if words[0] in ("http://www", "https://www"):
        print(words[1])
    elif words[0].startswith("http://") or words[0].startswith("https://"):
        print(words[0].split('//')[1])
    elif words[0] in ("www"):
        print(words[1])
    else:
        print(words[-2])
    pass


domain_name("http://github.com/carbonfive/raygun")
domain_name("http://www.zombie-bites.com")
domain_name("https://www.cnet.com")
domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("www.xakep.ru")
domain_name("https://youtube.com")
domain_name("www.something.net/index.com")
domain_name("https://shopping.online")
domain_name("sub.domain.example.com")


