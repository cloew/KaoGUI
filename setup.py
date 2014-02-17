from distutils.core import setup

setup(name='kao_gui',
      version='0.3',
      #description='Kao Tessur Cygwin Console Input Processor',
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['kao_gui', 'kao_gui/console', 'kao_gui/pygame', 'kao_gui/pygame/widgets'],
     )