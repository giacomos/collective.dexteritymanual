from setuptools import setup, find_packages
#
# Note: This file does not really serve any purpose
# it just keeps some tools happy
# 
import os

version = '1.0'

setup(name='collective.dexteritymanual',
      version=version,
      description="Plone community maintained developer documentation in Sphinx format",
      #long_description=open("README.txt").read() + "\n",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Plone Community',
      author_email='',
      url='http://plone.org',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      #namespace_packages=['gomobiletheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
