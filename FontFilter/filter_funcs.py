
def double_filter(data_list):
    r = filter(lambda x: x % 2 == 0, data_list)
    return list(r)
