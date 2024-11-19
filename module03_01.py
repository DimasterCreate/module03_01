calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    string = str(string)
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result
def is_contains(string, list_to_search):    # 4
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Android'))
print(string_info('Macbook'))
print(string_info('WiNdows'))
print(string_info('APPle'))
print(is_contains('gArlIcK', ['lick', 'GarliCK', 'RaglI' ]))
print(is_contains('FoOtBaLl', ['Basketball', 'foot', 'TeNNIS']))

print(calls)