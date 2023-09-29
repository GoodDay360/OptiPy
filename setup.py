from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Information Technology',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

with open('./requirements.txt', "r", encoding='utf-16') as f:
  required_packages = f.read().splitlines()

setup(
  name='optipy',
  version='2.0.1',
  description='Web Scraping API for getting Optifine VersionsList/Versions/Download-URL.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/GoodDay360/OptiPy',  
  author='GoodDay360',
  author_email='istartgame31@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['optifine','api','optifine_api'], 
  packages=find_packages(exclude=["dist","git","optipy.egg-info","venv"]),
  install_requires=required_packages,
  python_requires='>=3.6',
)