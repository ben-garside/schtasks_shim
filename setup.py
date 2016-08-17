"""
SCHTASKS_Shim
-----------
python SCHTASKS_Shim
Link
`````
* Source
  https://github.com/ben-garside/
"""
from distutils.core import setup

version = "0.1.1"

setup(
    name="schtasks_shim",
    version=version,
    author="Benjamin Garside",
    author_email="abgarside<at>gmail<dot>com",
    packages=[
        "schtasks_shim"
        ],
    include_package_data=True,
    url="http://github.com/ben-garside/schtasks_shim/dist/{}/".format(version),

    # license="LICENSE.txt",
    description="schtasks_shim",
    # long_description=open("README.txt").read() or just """ lots of text here too""",
    # Dependent packages (distributions)
    install_requires=[
    ],
)