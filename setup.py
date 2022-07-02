from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Information Technology',
  'Operating System :: Unix',
  'Operating System :: MacOS :: MacOS X',
  'Operating System :: Microsoft :: Windows',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='optipy',
  version='1.2.2',
  description='An API for getting Optifine VersionsList/Version/Download-URL.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/GoodDay360/OptiPy',  
  author='GoodDay360',
  author_email='istartgame31@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['optifine','api','optifine_api'], 
  packages=find_packages(exclude=["dist","git","optipy.egg-info"]),
  install_requires=[] 
)