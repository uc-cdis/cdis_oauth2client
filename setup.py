from setuptools import setup


setup(
    name='cdis_oauth2client',
    version='0.1.0',
    description='Flask blueprint and utilities for oauth2 client',
    url='https://github.com/uc-cdis/cdis_oauth2client',
    license='Apache',
    packages=[
        'cdis_oauth2client',
    ],
    install_requires=[
        'Flask==0.10.1',
        'requests==2.5.2',
    ],
    dependency_links=[
        "git+https://git@github.com/uc-cdis/cdis-python-utils.git@0.1.3#egg=cdispyutils",  # noqa
    ],
)
