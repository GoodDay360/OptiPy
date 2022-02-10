from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Information Technology',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.9'
]
 
setup(
  name='optipy',
  version='1.1.0',
  description='An API for getting Optifine VersionsList/Version/Download-URL.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/GoodDay360/Optifine-API',  
  author='GoodDay360',
  author_email='istartgame31@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='optifine api', 
  packages=find_packages(),
  install_requires=['requests','requests-html'] 
)