from statistics import mode
import model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_o = view.get_opert()
    
    if 'i' in value_a and 'i' in value_b:
        type_num = model.model_name_kmp
    else:
        type_num = model.model_name_rac

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