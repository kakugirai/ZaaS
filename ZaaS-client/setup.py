from setuptools import setup

setup(
    name="ZaaS-client",
    version="0.0.1",
    description="A CLI tool to help you register Zanryu in Delta",
    url="https://github.com/kakugirai/ZaaS",
    author="Girai Kaku",
    author_email="kakugirai@gmail.com",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules=[
        "zanryu",
    ],
    install_requires=[
        "click",
        "requests",
    ],
    entry_points='''
        [console_scripts]
        zanryu=zanryu:cli
    ''',
)
