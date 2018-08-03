#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-30 20:54:34
# @Author  : flying

import re

res = re.match('^song\d+','song521xiaofei')
print(res)  #>>><_sre.SRE_Match object; span=(0, 2), match='song521'>
print(res.group())  #>>>song521

# '.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
print(re.match('.','fly12ing23'))   #>>><_sre.SRE_Match object; span=(0, 1), match='f'>
print(re.match('.+','fly12ing23'))  #>>><_sre.SRE_Match object; span=(0, 10), match='fly12ing23'>
# '^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
# '$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以,匹配的字符串结尾
print(re.search('i.+g','fly12ing23'))   #>>><_sre.SRE_Match object; span=(5, 8), match='ing'>
print(re.search('i[a-z]+f','fly12ingf23f')) #>>><_sre.SRE_Match object; span=(5, 9), match='ingf'>
print(re.search('i[a-zA-Z]+f','fly12inLTXgf23f'))   #>>><_sre.SRE_Match object; span=(5, 12), match='inLTXgf'>
print(re.search('i[a-z]+f$','fly12ingf23f'))    #>>>none 匹配以f为结尾的字符串
# '*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
# '+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
# '?'     匹配?前一个字符1次或0次
print(re.search('fff?','fly12inLTXgf23fff'))    #>>><_sre.SRE_Match object; span=(14, 17), match='fff'>
print(re.search('fff?','ffly12inLTXgf23fff'))    #>>><_sre.SRE_Match object; span=(0, 2), match='ff'>
print(re.search('ffl?','ffly12inLTXgf23fff'))    #>>><_sre.SRE_Match object; span=(0, 3), match='ffl'>
print(re.search('ffl?','ffy12inLTXgf23fff'))    #>>><_sre.SRE_Match object; span=(0, 2), match='ff'>
# '{m}'   匹配前一个字符m次
print(re.search('[0-9]{3}','fl0yi1ng223'))  #>>><_sre.SRE_Match object; span=(8, 11), match='223'>
print(re.search('[0-9]{1,3}','fl0yi1ng223'))  #>>><_sre.SRE_Match object; span=(2, 3), match='0'>
print(re.findall('[0-9]{1,3}','fl0yi1ng223'))  #>>>['0', '1', '223']
# '{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
# '|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
print(re.search('abc|ABC','ABCBabcCD').group()) #>>>ABC
print(re.findall('abc|ABC','ABCBabcCD')) #>>>['ABC', 'abc']
# '(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
print(re.search('abc{2}','flyingabaabcc'))  #>>><_sre.SRE_Match object; span=(9, 13), match='abcc'>
print(re.search('(ab){2}\|','flyingabab|cc|'))  #>>><_sre.SRE_Match object; span=(6, 11), match='abab|'>
print(re.search('(ab){2}(\|\|=){2}','flyabab||=||=cc|'))  #>>><_sre.SRE_Match object; span=(6, 16), match='abab||=||='>


# '\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的,同 '^'
# '\Z'    匹配字符结尾，同$
print(re.search('\A[0-9]+[a-z]\Z','520f'))  #>>><_sre.SRE_Match object; span=(0, 4), match='520f'>
# '\d'    匹配数字0-9
# '\D'    匹配非数字
print(re.search('\D+','520f*y ('))  #>>><_sre.SRE_Match object; span=(3, 8), match='f*y ('>
# '\w'    匹配[A-Za-z0-9]
print(re.search('\w+','520f*y ('))  #>>><_sre.SRE_Match object; span=(0, 4), match='520f'>
# '\W'    匹配非[A-Za-z0-9]
print(re.search('\W+','520f* ('))   #>>><_sre.SRE_Match object; span=(4, 7), match='* ('>
# '\s'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
print(re.search('\s+','520f* \t\n\r(')) #>>><_sre.SRE_Match object; span=(5, 9), match=' \t\n\r'>

#'(?P<name>...)'
print(re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city"))
#   >>>{'province': '3714', 'city': '81', 'birthday': '1993'}
print(re.search('(?P<id>[0-9]+)','abcd1234af&af'))  #>>><_sre.SRE_Match object; span=(4, 8), match='1234'>
print(re.search('(?P<id>[0-9]+)','abcd1234af&af').group())  #>>>1234
print(re.search('(?P<id>[0-9]+)','abcd1234af&af').groupdict())  #>>>{'id': '1234'}