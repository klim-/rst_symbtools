# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 11:35:00 2014

@author: Carsten Knoll
"""

import unittest

import sympy as sp
from sympy import sin

import symb_tools as st
from IPython import embed as IPS


class SymbToolsTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_symbs_to_func(self):
        a, b, t = sp.symbols("a, b, t")
        x = a + b
        #M = sp.Matrix([x, t, a**2])

        f_x = st.symbs_to_func(x, [a, b], t)
        self.assertEquals(str(f_x), "a(t) + b(t)")

    def test_perform_time_deriv1(self):
        a, b, t = sp.symbols("a, b, t")
        f1 = a**2 + 10*sin(b)
        f1_dot = st.perform_time_derivative(f1, (a, b))
        self.assertEquals(str(f1_dot), "2*a*a_d + 10*b_d*cos(b)")

        f2 = sin(a)
        f2_dot2 = st.perform_time_derivative(f2, [a, b], t, order=2)
        f2_dot = st.perform_time_derivative(f2, [a], t)
        f2_ddot = st.perform_time_derivative(f2_dot, [a, sp.Symbol('a_d')], t)
        self.assertEqual(f2_ddot, f2_dot2)

    def test_match_symbols_by_name(self):
        a, b, c = abc0 = sp.symbols('a, b, c', real=True)
        a1, b1, c1 = abc1 = sp.symbols('a, b, c')

        self.assertFalse(a == a1 or b == b1 or c == c1)

        abc2 = st.match_symbols_by_name(abc0, abc1)
        self.assertEquals(abc0, tuple(abc2))

        input3 = [a1, b, "c", "x"]
        a3, b3, c3, x3 = st.match_symbols_by_name(abc0, input3)

        self.assertEquals(abc0, (a3, b3, c3))
        self.assertEquals(x3, sp.Symbol('x'))



def main():
    unittest.main()

if __name__ == '__main__':
    main()