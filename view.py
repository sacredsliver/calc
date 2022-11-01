def view_data(data, title):
    print(f'{title} = {data}')

def get_value():
    return str(input('value = '))

def get_opert():
    return str(input('oper = '))

def try_cast(value, type):   
    try:
        return type(value)
    except:
        return None