#raise   assert 两种自定义异常的方法
#!/usr/bin/env python3
def set_age(name,age):
    if not 0 <age < 150:
        raise ValueError('age out of range')
    print(name,age)
def set_age2(name,age):
    assert 0<age<150, 'age out of range'
    print(name,age)
    pass
if __name__=='__main__':
    try:
        set_age2('bob',233)
    except ValueError:
        print('invalid input!')