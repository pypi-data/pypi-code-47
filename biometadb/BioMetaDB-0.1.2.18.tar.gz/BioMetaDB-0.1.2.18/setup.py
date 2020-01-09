import os
from Cython.Build import cythonize
from setuptools import setup, Extension
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), "r") as f:
    long_description = f.read()

# with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "requirements.txt"), "r") as fp:
#     install_requires = fp.read().strip().split("\n")

extensions = [
    Extension("BioMetaDB.Accessories.arg_parse", ["BioMetaDB/Accessories/arg_parse.pyx"]),
    Extension("BioMetaDB.Accessories.bio_ops", ["BioMetaDB/Accessories/bio_ops.pyx"]),
    Extension("BioMetaDB.Accessories.ops", ["BioMetaDB/Accessories/ops.pyx"]),
    Extension("BioMetaDB.Accessories.program_caller", ["BioMetaDB/Accessories/program_caller.pyx"]),
    Extension("BioMetaDB.DataStructures.record_list", ["BioMetaDB/DataStructures/record_list.pyx"]),
    Extension("BioMetaDB.DBManagers.class_manager", ["BioMetaDB/DBManagers/class_manager.pyx"]),
    Extension("BioMetaDB.DBManagers.integrity_manager", ["BioMetaDB/DBManagers/integrity_manager.pyx"]),
    Extension("BioMetaDB.DBManagers.update_manager", ["BioMetaDB/DBManagers/update_manager.pyx"]),
    Extension("BioMetaDB.Models.functions", ["BioMetaDB/Models/functions.pyx"]),
    Extension("BioMetaDB.Serializers.count_table", ["BioMetaDB/Serializers/count_table.pyx"]),
    Extension("BioMetaDB.Serializers.fix_file", ["BioMetaDB/Serializers/fix_file.pyx"]),
    Extension("BioMetaDB.Serializers.tsv_joiner", ["BioMetaDB/Serializers/tsv_joiner.pyx"]),
]

setup(
    name='BioMetaDB',
    version='0.1.2.18',
    description='Use biological data to generate SQL database schema',
    url="https://github.com/cjneely10/BioMetaDB",
    author="Christopher Neely",
    author_email="christopher.neely1200@gmail.com",
    license="GNU GPL 3",
    install_requires=[
        "SQLAlchemy==1.3.7",
        "biopython==1.74",
        "configparser==3.8.1",
        "Cython==0.29.13"
    ],
    entry_points={
        "console_scripts": [
            "dbdm = BioMetaDB:main"
        ]
    },
    python_requires='>=3.6',
    ext_modules=cythonize(extensions),
)

