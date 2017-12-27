from setuptools import setup

setup(name='cw_msgpack_coder',
      version='1.1',
      description='Simple and fast Python any object serialization with use msgpack.',
      author='Cezary K. Wagner',
      license='MIT',
      packages=('cw_msgpack_coder',),
      install_requires='u-msgpack-python',
      classifiers=(
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'),
      keywords="msgpack serialization streaming object encoding decoding",
      test_suite="tests.test_umsgpack_coder")
