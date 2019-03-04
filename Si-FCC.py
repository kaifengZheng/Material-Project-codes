from pymatgen import Lattice, Structure, Molecule
from json import dump, load
coords = [[0,0,0],[1,0,0],[1,0,1],
          [0,1,0],[0,1,1],[1,1,0],
          [0,0,1],[1,1,1],[0.5,0,0.5],
          [0.5,1,0.5],[0,0.5,0.5],[1,0.5,0.5],
          [0.5,0.5,0],[0.5,0.5,1]]
lattice = Lattice.from_parameters(a=1,b=1,c=1,alpha=90,beta=90,gamma=90)
struct = Structure(lattice,["Si" for n in range(14)],coords)
with open('structure.json','w') as f:
    dump(struct.as_dict(),f)
    f.close()
with open('structure.json','r') as f:
    d = load(f)
    structure = Structure.from_dict(d)
    f.close()

