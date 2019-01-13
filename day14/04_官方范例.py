
# 1).
# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")



# 2.
import sys
# /etc/passwd /etc/group
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        # 如果try语句中没有产生任何异常和错误， 才执行的语句；
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()