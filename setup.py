import setuptools
from setuptools_rust import Binding, RustExtension

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-eth-pairing", # Replace with your own username
    version="0.1.4",
    author="Lucien",
    author_email="lokm13@gmail.com",
    description="Use Ethereum precompiled pairing operations (BN128, specified in EIP196) in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    rust_extensions=[RustExtension("py_eth_pairing.eth_pairing_py", binding=Binding.PyO3)],
    url="https://github.com/Lucieno/py_eth_pairing",
    # packages=setuptools.find_packages(),
    packages=["py_eth_pairing"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
