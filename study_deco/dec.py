# -*- coding: utf-8 -*-

fail = []

def plus(score):
    score = score +10
    return score


def tdeco1(func):
    def _tdeco1(name2, score2):
        if score2 >= 60:
            score2 = plus(score2)

        func(name2, score2)
    return _tdeco1

def tdeco2(func):
    def _tdeco2(name2, score2):
        if score2 < 60:
            fail.append(name2)
        func(name2, score2)
    return _tdeco2

@tdeco1
@tdeco2
def exam(name,score):
    if score>=60:
        print name,'合格:',score
    else :
        print name,'不合格'


if __name__ == '__main__':
    exam('张三',80)
    exam('李四',50)
    exam('李1四',20)
    print '不合格名单：',fail
