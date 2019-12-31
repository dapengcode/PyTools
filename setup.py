
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTools", # Replace with your own username
    version="0.0.1",
    author="DaPeng",
    author_email="davidmaster@163.com",
    description="开发爬虫常用的工具类",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dapengcode/PyTools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)