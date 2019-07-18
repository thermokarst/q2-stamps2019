from setuptools import find_packages, setup


setup(
    name='q2-stamps2019',
    version='2019.4.0',
    packages=find_packages(),
    url='https://github.com/qiime2/q2-stamps2019',
    entry_points={
        'qiime2.plugins':
        ['q2-stamps2019=q2_stamps2019:plugin']
    },
    install_requires=['qiime2', 'q2-types', 'pandas'],
)
