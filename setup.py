import os
import setuptools

optional_dev_tag = ''
if os.getenv('DEV_BUILD'):
    optional_dev_tag = '.dev' + os.getenv('DEV_BUILD')

<<<<<<< HEAD
setuptools.setup(
    author='Ben Busby',
    author_email='contact@benbusby.com',
    name='whoogle-search',
    version='0.7.1' + optional_dev_tag,
    include_package_data=True,
    install_requires=requirements,
    description='Self-hosted, ad-free, privacy-respecting metasearch engine',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/benbusby/whoogle-search',
    entry_points={
        'console_scripts': [
            'whoogle-search=app.routes:run_app',
        ]
    },
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
=======
setuptools.setup(version='0.7.2' + optional_dev_tag)
>>>>>>> 194ddc33f36e6955587816acd2347bbebeef7912
