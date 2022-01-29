desc = "My secret stuff 👨‍⚕️"
long_desc = f"""
My secret stuff 👨‍⚕️
"""


import setuptools

setuptools.setup(
    name="doctorsecret",
    version="0.9.9",
    url="https://github.com/doctor-jebaited/secret1234",

    author="DR Jebait",
    author_email="jebaited@example.com",

    description=desc,
    long_description=long_desc,
    long_description_content_type='text/markdown',
    keywords=[],
    packages=setuptools.find_packages(),
    install_requires=['pytest'],
    setup_requires=[],
    tests_require=[],
    classifiers=[],
    entry_points={},
)
