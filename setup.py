try:
    import multiprocessing
except ImportError:
    pass


from setuptools import setup

setup(
    name='Flask-Imagine-S3Adapter',
    version='0.2.1',
    description='Amazon AWS S3 adapter for Flask-Imagine extension.',
    url='https://github.com/FlaskGuys/Flask-Imagine-S3Adapter',

    author='Kronas',
    author_email='kronas.sw@gmail.com',
    license='MIT',

    packages=['flask_imagine_s3_adapter'],

    install_requires=[

        'Flask-Imagine>=0.2.1',
        'boto>=2.38.0',

    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    zip_safe=False,
)
