from setuptools import setup

setup(name='OptigoUtils',
      version='3.2',
      author='P.S',
      author_email='a85571@alta.iai',
      url='#',
      description="Optigo Utils.",

      packages=['OptigoUtils', 'OptigoUtils/XVI', 'OptigoUtils/opptx'],

      package_data={'': ['**/*.json']},
      zip_safe=False)




