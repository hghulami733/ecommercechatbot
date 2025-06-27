from setuptools import find_packages, setup

setup(
    name="ECommercebot",
    version="0.0.1",
    author="Hamid",
    author_email="hgholami733@gmail.com",
    packages=find_packages(),
    install_requires=["langchain-astradb", "langchain", "langchain-openai", "datasets", "pypdf", "python-dotenv", "flask"]
)