import random

def random_list(n):
    result = []
    a1 = ['赵','钱','孙','李']
    a2 = ['丽','强','飞','']
    a3 = ['梦','晓','鑫','田','地','安','宁','','','']
    a4 = ['飞','天','亮','田','国','安','成','','','']
    a5 = ['丽','强','飞','','']
    a6 = ['梦','天','鑫','娇','民','安','成','','','']


    for i in range(n):
        name = random.choice(a1)+random.choice(a2)+random.choice(a3)+random.choice(a4)+random.choice(a5)+random.choice(a6)
        list = name
        result.append(list)
    print(result)
    return result

random_list(50)