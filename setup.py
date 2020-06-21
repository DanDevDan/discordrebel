from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='discordrebel',
    packages=['discordrebel'],
    version='0.0.2',
    license='MIT',
    description='An API Client to use Discord API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Signal',
    author_email='example@gmail.com',
    url='https://github.com/SignalDevX/discordrebel.py',
    keywords=['YTMC'],
    python_requires='>=3.4.0',
    install_requires=[
        'requests',
        'urllib3',
        'websocket_client'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)