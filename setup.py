import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="ezFraction",
    version="0.0.1",
    author="Jasur Yusupov",
    author_email="jasuryusupov14@gmail.com",
    description="Fractions made easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/GooDeeJaY/ezFraction",
    project_urls={
        "Bug Tracker": "https://github.com/GooDeeJaY/ezFraction/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)