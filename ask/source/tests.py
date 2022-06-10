from source.models import index_update


def generate_indexes():

    index_list = ['SP100', 'SP500']
    
    for index in index_list:
        index_update(index)

