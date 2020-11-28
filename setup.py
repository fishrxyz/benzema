import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	# Here is the module name.
	name="benzema",

	# version of the module
	version="0.1.1",

	# Name of Author
	author="KC Fishr",

	# your Email address
	author_email="karim@fishr.xyz",

	#Small Description about module
	description="A straight forward and easy to use bencoding library written in Python 3",

	# Specifying that we are using markdown file for description
	long_description=long_description,
	long_description_content_type="text/markdown",

	# Any link to reach this module, ***if*** you have any webpage or github profile
	url="https://github.com/fishrxyz/benzema",

	packages=setuptools.find_packages(),

	license="WTFPL",

	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
)
