from setuptools import setup, find_packages

setup(
    name='ai-fraud-detection-system',
    version='0.1.0',
    author='gaganatwork',
    author_email='your-email@example.com',
    description='An AI-based system for detecting fraudulent activities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gaganatwork/ai-fraud-detection-system',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',  # or 'pytorch', depending on your implementation
        'flask'        # or 'fastapi', depending on your web framework choice
    ],
)