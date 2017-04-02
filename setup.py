from setuptools import setup

setup(name='mtp30apitest1',
      version='1.0',
      description='OpenShift App',
      author='Maya Petranova',
      author_email='mayapetranova@gmail.com',
      url='http://mtp30apitest1-mtp30apitest1.apps.devcloud.eecs.qmul.ac.uk/',
      ##install_requires=['Flask>=0.7.2', 'MarkupSafe'],
      install_requires=['Flask','flask-wtf', 'unirest', 'wtforms','NumPy', 'Six', 'Jinja2', 'Requests', 'Tornado >= 4.0', 'PyYaml', 'DateUtil', 'bokeh==0.12.4', 'Futures', 'Flask-PyMongo', 'Navigation'],
      )
