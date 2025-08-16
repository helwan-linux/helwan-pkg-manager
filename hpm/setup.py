from setuptools import setup, find_packages

setup(
    name="hpm",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer>=0.9.0",  # لأنك تستخدم Typer
        # أضف أي مكتبات أخرى يحتاجها المشروع
    ],
    entry_points={
        'console_scripts': [
            'hpm = hpm.main:main',  # يشير مباشرة لدالة main في hpm/main.py
        ],
    },
    author="Saeed Badrelden",
    author_email="helwanlinux@gmail.com",
    description="Helwan Package Manager: A simple and powerful frontend for pacman",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires='>=3.11',
)

