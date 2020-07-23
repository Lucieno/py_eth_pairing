from time import time

from py_eth_pairing import curve_add, curve_mul, pairing2, curve_negate
from py_ecc.bn128 import G1, G2, add, multiply, curve_order, pairing

print("curve_add")
t0 = time()
actual = curve_add(G1, G1)
print(time() - t0)
expected = add(G1, G1)
assert actual == expected

print("curve_mul")
sc = curve_order - 10
g1_pk = multiply(G1, sc)
t0 = time()
actual = curve_mul(g1_pk, sc)
print(time() - t0)
expected = multiply(g1_pk, sc)
assert actual == expected

print("pairing2: expect true")
sc = 123
g1_pk = multiply(G1, sc)
g2_pk = multiply(G2, sc)
t0 = time()
actual = pairing2(curve_negate(g1_pk), G2, G1, g2_pk)
print(time() - t0)
expected = True
assert actual == expected

print("pairing2: expect false")
g1_pk = multiply(G1, 123)
g2_pk = multiply(G2, 1234)
t0 = time()
actual = pairing2(curve_negate(g1_pk), G2, G1, g2_pk)
print(time() - t0)
expected = False
assert actual == expected