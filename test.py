from DAGs.DAG_base import Node
from DAG import DAG
import random
from sys import argv

dag = DAG()
dag.read_file_tgff(argv[1])
dag.record_pre_suc()
dag.record_src_snk()

dag.find_critical_path()
#dag.print_critical_path()

dag.rta_fcp(65536)
#dag.checksum()

for node in dag.nodes:
    print(node.p)