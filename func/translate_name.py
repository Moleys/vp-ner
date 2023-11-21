
def readWords(path):
    file1 = open(path, 'r')
    lines = file1.readlines()
    arr0= []
    arr1= []
    arr2= []
    for line in lines:
        temp1 = line.split("=")
        temp2 = temp1[1].split("/")
        arr1.insert(len(arr1),temp2[0].rstrip())
        arr0.insert(len(arr0),temp1[0].rstrip())
    arr2.insert(len(arr2),arr0)
    arr2.insert(len(arr2),arr1)
    return arr2


def replaceWords(dic_vp_cn, dic_vp_vi, text_input, text_output):
    for i in range(len(dic_vp_cn)):
        if text_input is None:
            break
        if dic_vp_cn[i] in text_input:
            text_input = text_input.replace(dic_vp_cn[i], "_________")
            text_output = text_output.replace(dic_vp_cn[i], dic_vp_vi[i] + " ")
    return text_input, text_output


path_na = 'dictionary/Names.txt'

path_cpaw = 'dictionary/ChinesePhienAmWords.txt'
path_dt = 'dictionary/DanhTu.txt'
path_dx = 'dictionary/DanhXung.txt'
path_hn = 'dictionary/HoNguoi.txt'


dic_na_cn, dic_na_vi = readWords(path_na)

dic_cpaw_cn, dic_cpaw_vi = readWords(path_cpaw)
dic_dt_cn, dic_dt_vi = readWords(path_dt)
dic_dx_cn, dic_dx_vi = readWords(path_dx)
dic_hn_cn, dic_hn_vi = readWords(path_hn)




def translateName(text_input):
    if text_input in dic_na_cn:
        index = dic_na_cn.index(text_input)
        text_output = dic_na_vi[index]
        return text_output
    text_output = text_input
    text_input, text_output = replaceWords(dic_dx_cn, dic_dx_vi, text_input, text_output)
    text_input, text_output = replaceWords(dic_hn_cn, dic_hn_vi, text_input, text_output)
    text_input, text_output = replaceWords(dic_dt_cn, dic_dt_vi, text_input, text_output)
    text_input, text_output = replaceWords(dic_cpaw_cn, dic_cpaw_vi, text_input, text_output)

    text_output = text_output.strip()
    return text_output

