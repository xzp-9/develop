# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_calc.py
import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    myid = datas['myid']

with open("./datas/calc1.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)['div']
    div_datas = datas['datas']
    print(div_datas)
    myid = datas['myid']


class TestCalc:
    def setup_class(self):
        print("【开始计算加法和除法】")
        self.calc = Calculator()


@pytest.mark.parametrize(
    'a, b, expect',
    add_datas,
    ids=myid
)
def test_add(self, a, b, expect):
    result = self.calc.add(a, b)
    if isinstance(result, float):
        result = round(result, 2)
    assert result == expect


@pytest.mark.parametrize(
    'a, b, expect',
    div_datas,
    ids=myid
)
def test_div(self, a, b, expect):
    result = self.calc.div(a, b)
    if isinstance(result, float):
        result = round(result, 2)
    assert result == expect


if __name__ == "__main__":
    pass
