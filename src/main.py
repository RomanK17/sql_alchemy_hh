import os
import sys

from queries.core import create_table, insert_data
from models import metadata_obj

sys.path.insert(1, os.path.join(sys.path[0], '..'))


create_table(metadata_obj)
insert_data()