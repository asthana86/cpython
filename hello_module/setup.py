from distutils.core import setup, Extension

hello_world_module = Extension('hello_module',
                           sources = ['hello_module.c'])

setup(name = 'lesson_one',
      version = '1.0',
      description = 'Python Package with Hello World C Extension',
      ext_modules = [hello_world_module],

      url='http://deadfish.com',
      author='',
      author_email='')
