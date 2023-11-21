
def getNameList(text_input, dic_na_cn):
    arr = []
    for index, value in enumerate(dic_na_cn):
        while value in text_input:
            start_index = text_input.find(value)
            end_index = start_index + len(value)
            arr.append((value, start_index, end_index))
            text_input = text_input[:start_index] + "刘备" + text_input[end_index:]
    arr.sort(key=lambda x: x[1])
    return arr, text_input

def replaceTextNames(text_input, arr_name, dic_na_cn, dic_na_vi):
    text_output = text_input
    for name in arr_name:
        translated_name = dic_na_vi[dic_na_cn.index(name[0])]
        text_output = text_output.replace("Lưu Bị", translated_name,1)
    return text_output