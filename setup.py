import setuptools
import gic

with open("README.md") as f:
    long_desc = f.read()


setuptools.setup(
        name="gic",
        version=gic.version,
        description="Group Image Compressor (GIC)",
        long_description=long_desc,
        long_description_content_type="text/markdown",
        url="https://github.com/poyynt",
        author="Parsa Torbati",
        author_email="parsa@programmer.net",
        packages=setuptools.find_packages(),
        python_requires=">=3.2",
        install_requires=[
            "opencv-python",
            ],
        entry_points={
            "console_scripts": [
                "gic=gic.main:run",
                ],
            },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Operating System :: OS Independent",
            "Development Status :: 5 - Production/Stable",
            "Natural Language :: English",
            "Topic :: Utilities",
            ],
        )
