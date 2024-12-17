from setuptools import setup ,find_packages

setup(
    name="QA_system",
    version="0.0.0",
    author="shubham",
    author_email="shubhammokal30@gmail.com",
    description="this is a simple QA system",
    packages=find_packages(),
    install_requires=["pinecone-haystack","haystack-ai","fastapi","uvicorn","python-dotenv","pathlib","django"]
)