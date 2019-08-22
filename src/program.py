from generators import Generator
from parsers import split as split_req

if __name__ == "__main__":
    gen = Generator()
    [reqs, variable] = split_req(input())
    # print(reqs)
    for req in reqs:
        if req == ';':
            print()
            continue
        arg = gen.parse_request(req)
        # print(arg)
        data = gen.generate(**arg)
        print(data)
        if arg.get('var_name', False) is not False:
            gen.variables[arg['var_name']] = data
        


