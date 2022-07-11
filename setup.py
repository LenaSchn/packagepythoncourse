from setuptools import find_packages, setup

setup(
    name="packagepythoncourse",
    version="0.1.0",
    description="A Minimal Template Python Package",
    url="https://github.com/RealityBending/TemplatePythonPackage",
    author="Lena Schneider",
    author_email="schneiderl@ethz.ch",
    license="MIT",
    install_requires=["numpy", "pandas", "scipy", "matplotlib"],
    packages=find_packages(),
    zip_safe=False,
)
