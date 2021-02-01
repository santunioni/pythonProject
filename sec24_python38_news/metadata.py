"""
New metadata for python 3.8
"""

from importlib import metadata
print(metadata.version('pip'))

pip_metadata = metadata.metadata('pip')
print(pip_metadata)

print(len(metadata.files('pip')))

print(metadata.requires('pip'))

print(metadata.requires('django'))
