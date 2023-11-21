
import func.translate_name
import func.replace_name


print("File path Chinese raw:", end=' ')
file_input_path = input().strip('"')
print("File path Name:", end=' ')
file_name_path = input().strip('"')

# ===========read file
with open(file_input_path, "r") as file:
    lines = file.readlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    text_input = "\n".join(non_empty_lines)
# Create name
dic_na_cn, dic_na_vi = func.translate_name.readWords(file_name_path)

#=================thay tên người thành Lưu Bị
arr_name, text1 = func.replace_name.getNameList(text_input, dic_na_cn)
print(arr_name)
print(text1)

#=========API TRANSLATE=================
text_output = decoded_result['result']
#==================replace name
text_output = func.replace_name.replaceTextNames(text_output, arr_name, dic_na_cn, dic_na_vi)
print(text_output)