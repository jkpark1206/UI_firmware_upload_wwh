import string
import random


def Ran_str(S):
    ran_str = ''.join(random.choices(string.ascii_letters + string.digits, k = S))
    return ran_str

def Random_num():
    random_number = random.randint(1, 10)
    return random_number

def Random_symbol():
    string = "!@#$%^&*()！@#￥%……&*"
    return random.choice(string)

def generate_random_number(n):
    return random.randint(10**(n-1), 10**n - 1)


def generate_random_email(n):
    domain = 'qq.com'
    """
    生成一个随机的电子邮箱地址。
    默认域名是 'example.com'，可以通过参数修改。
    """
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n))
    email = f"{username}@{domain}"
    return email


if __name__ == '__main__':
    print(generate_random_number(10))