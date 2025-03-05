from setuptools import setup, find_packages

setup(
    name="mlproject",
    version="0.0.1",
    description="Sample ML Project",
    author="Sunil",
    author_email="Sunil@gmail.com",
    packages=find_packages(),
    install_requires=[
            "seaborn==0.13.2",
            "pandas==2.2.3",
            "scikit-learn==1.6.1",
            "xgboost==2.1.4",
    ]
)