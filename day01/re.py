# # 用来匹配字符串的
# # str.find()
#
#
# """
# 元字符 (通用的)
# 普通字符
# 特殊
# 限定符
# """
# import re
#
# content = 'fsfsg   fgfeg\n  sfetgfeg'
#
#
# # . 表示匹配除了\n 之外的任意字符
#
#
# def print_re(re_str):
#     print(re.findall(re_str, content))
#
#
# if __name__ == '__main__':
#     # ceshi  '.'
#     print_re('.')
