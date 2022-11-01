import model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_o = view.get_opert()
    
    if 'i' in str(value_a) and 'i' in str(value_b):
        type_num = model.model_name_kmp
    elif view.try_cast(value_a, int) != None and view.try_cast(value_b, int) != None:
        type_num = model.model_name_rac
    else:
       raise Exception('Invalid operands!')    

    model.init(value_a, value_b, type_num)

    if value_o == '*':
        result = model.mult()
    elif value_o == '/':
        result = model.div()
    elif value_o == '+':
        result = model.sum()
    elif value_o == '-':
        result = model.sub()
    else:
        raise Exception('Operation not support!')            

    view.view_data(result, "result")