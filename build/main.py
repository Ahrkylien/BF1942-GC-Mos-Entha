import os
from RFA import RefractorFlatArchive

map_name = "GC_Mos_Entha"

rfa = RefractorFlatArchive(f"{map_name}.rfa")
rfa.addDirectory("../src")
if not os.path.exists("client"):
    os.makedirs("client")
# rfa.write(f"client{os.sep}{map_name}.rfa")

rfa.deleteAllNonServerFiles()
if not os.path.exists("server"):
    os.makedirs("server")
rfa.write(f"server{os.sep}{map_name.lower()}.rfa")