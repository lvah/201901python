age = int(input("Age:"))


# try....except...finally  ===== 捕获异常
# raise ======   抛出异常
class AgeError(Exception):
    pass

if age < 0 or age > 120:
    raise  AgeError
else:
    print(age)
