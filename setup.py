from setuptools import setup, find_packages

setup(
    name='fb_messenger',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Simple Python facebook messenger API',
    long_description=open('README.md').read(),
    install_requires=['flask', 'requests'],
    url='https://github.com/juliennassar/fb_messenger',
    author='Julien Nassar',
    author_email='julien.nassar@gmail.com'
)
