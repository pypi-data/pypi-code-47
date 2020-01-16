import os
import sys

from franklab_msdrift.p_anneal_segments import anneal_segments
from franklab_msdrift.p_concatenate_firings import concatenate_firings
from franklab_msdrift.p_extract_subfirings import extract_subfirings
from franklab_msdrift.p_handle_drift_in_segment import handle_drift_in_segment
from franklab_msdrift.p_join_segments import join_segments
from franklab_msdrift.p_reptrack import reptrack
from pyms.mlpy import ProcessorManager

parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PM = ProcessorManager()

PM.registerProcessor(concatenate_firings)
PM.registerProcessor(handle_drift_in_segment)
PM.registerProcessor(join_segments)
PM.registerProcessor(anneal_segments)
PM.registerProcessor(extract_subfirings)
PM.registerProcessor(reptrack)

if not PM.run(sys.argv):
    exit(-1)
