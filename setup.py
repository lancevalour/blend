from setuptools import setup

setup(
    name='blend',
    version='1.0',
    packages=['blend'],
    include_package_data=True,
    license='MIT',
    author='Yicheng Zhang',
    url='https://github.com/lancevalour/blend', requires=['matplotlib', 'librosa', 'pytube']
)
