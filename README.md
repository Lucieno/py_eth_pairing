## How to Install
```
pip install py_eth_pairing
```

## How to Build from Source

- Install [Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html) for Rust
```
curl https://sh.rustup.rs -sSf | sh
```

- Install Maturin
```
pip install Maturin
```

- Compile it
```
maturin develop --release
```

## How to Use
Please check `test.py` as an example

```python
from py_eth_pairing import curve_add, curve_mul, pairing2, curve_negate
from py_ecc.bn128 import G1, G2

curve_add(G1, G1)
sk = 100
g1_pk = curve_mul(G1, sk)
actual = pairing2(curve_negate(G1), G2, G1, G2)
```

## Performance
The unit of time is second.
```
curve_add
6.985664367675781e-05
curev_mul
0.00014019012451171875
pairing2
0.0034821033477783203
```