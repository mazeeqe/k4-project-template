import ROOT
from pathlib import Path

# Get path to file inside input_files folder relative to the script
file_path = Path(__file__).parent / "input_files" / "/afs/desy.de/user/b/bortolet/code/k4-project-template/k4ProjectTemplate/options/input_files/Dirac-Dst-E250-e2e2h_inv.eL.pR_bg-00002.root"

reader = ROOT.podio.EventStore()
reader.open(str(file_path))

for collection in reader.getCollectionNames():
    print(collection)
