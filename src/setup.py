from setuptools import setup, find_namespace_packages

setup(
    name="restic-compose-backup",
    url="https://github.com/ZettaIO/restic-compose-backup",
    version="1.0.0",
    author="Einar Forselv",
    author_email="eforselv@gmail.com",
    packages=find_namespace_packages(include=['restic_compose_backup']),
    install_requires=[
        # 'docker==4.1.*',
        'docker~=6.0.0',
    ],
    entry_points={'console_scripts': [
        'restic-compose-backup = restic_compose_backup.cli:main',
        'rcb = restic_compose_backup.cli:main',
    ]},
)
