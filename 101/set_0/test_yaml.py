import yaml


def print_yaml(doc, n):
    for k, v in doc.items():
        if isinstance(v, dict):
            print("\t"*n, k)
            n += 1
            print_yaml(v, n)
            n -= 1
        else:
            print("\t"*n + f"{k} : {v}")


with open('data.yaml') as f:
    docs = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in docs:
        print_yaml(doc, 1)

