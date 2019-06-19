import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='protecc',
    version='0.0.1',
    author='Avinash Shenoy',
    author_email='avi123shenoy@gmail.com',
    description='Access modifiers for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/avinashshenoy97/protecc',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
