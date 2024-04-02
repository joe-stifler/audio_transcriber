from setuptools import setup, find_packages

setup(
    name="audio_transcriber",
    version="0.1.0",
    author="Joe",
    author_email="joseribeiro1017@gmail.com",
    packages=find_packages(),
    install_requires=[
        "openai-whisper",  # Add other dependencies as needed
    ],
    entry_points={
        "console_scripts": [
            "audio_transcriber=audio_transcriber.transcriber:main",
        ],
    },
    description="A simple audio/video transcriber tool.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
