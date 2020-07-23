## How to Install
```
pip install py_eth_pairing
```

## How to Use
Please check `test.py` as examples

```
from py_eth_pairing import curve_add, curve_mul, pairing2, curve_negate
from py_ecc.bn128 import G1, G2

curve_add(G1, G1)
sk = 100
g1_pk = curve_mul(G1, sk)
actual = pairing2(curve_negate(G1), G2, G1, G2)
```