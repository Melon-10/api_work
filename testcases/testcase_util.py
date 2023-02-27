import openpyxl


# 读取全局变量工作表
def get_variable(wb):
    sheet_data = wb["全局变量"]
    variable = {}  # 用来储存读到的变量，名称是key，值是value
    lines_count = sheet_data.max_row  # 获取总行数
    for l in range(2, lines_count+1):
        key = sheet_data.cell(l, 1).value
        value = sheet_data.cell(l, 2).value
        variable[key] = value
    return variable

# 读取接口默认参数
def get_api_default_params(wb):
    sheet_data = wb["接口默认参数"]
    api_default_params = {}  # 用来储存读到的变量，名称是key，值是value
    lines_count = sheet_data.max_row  # 获取总行数
    for l in range(2, lines_count + 1):
        key = sheet_data.cell(l, 1).value
        value = sheet_data.cell(l, 2).value
        api_default_params[key] = value
    return api_default_params


# 获取要执行的测试集合名称
def get_casesuitename(wb):
    sheet_data = wb["测试集合管理"]
    case_suite_name = []  # 用来储存读到的变量，名称是key，值是value
    lines_count = sheet_data.max_row  # 获取总行数
    for l in range(2, lines_count + 1):
        flag = sheet_data.cell(l, 2).value
        if flag == "y":
            key = sheet_data.cell(l, 1).value
            case_suite_name.append(key)
    return case_suite_name


if __name__ == '__main__':
    wb = openpyxl.load_workbook('../testcases/CRM系统接口测试用例.xlsx')
    print(get_variable(wb))
    print(get_api_default_params(wb))
    print(get_casesuitename(wb))