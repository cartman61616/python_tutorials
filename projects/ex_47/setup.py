try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jonathan Davis',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'cartman61616@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex_47'],
    'scripts': [],
    'name': 'ex_47'
}

setup(**config)