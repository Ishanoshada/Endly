from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="endly",
    version="0.1.1",
    author="Ishan Oshada",
    author_email="ishan.kodithuwakku.offical@gmail.com",
    description="A lightweight Python web framework for building fast and scalable backend applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ishanoshada/endly",
    project_urls={
        "Bug Tracker": "https://github.com/ishanoshada/endly/issues",
        "Documentation": "https://github.com/ishanoshada/endly#readme",
        "Source Code": "https://github.com/ishanoshada/endly",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
    ],
    keywords=[
        "web framework",
        "backend",
        "seo",
        "web development",
        "api",
        "rest",
        "http",
        "wsgi",
        "lightweight",
        "fast",
        "scalable"
    ],
    install_requires=[],
    include_package_data=True,
)