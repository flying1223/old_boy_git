

import re

sum = 0
for i in range(0,101):
    sum = sum + i
print(sum)

str = '<div class="nam">中国</div>'
print(re.findall(r'(.*?)',str))