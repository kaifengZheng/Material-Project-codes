from pymatgen import Lattice, Structure, Molecule
from json import dump, load
from pymatgen.io import xyz
coords = [[0,0,0],[1,0,0],[1,0,1],
          [0,1,0],[0,1,1],[1,1,0],
          [0,0,1],[1,1,1],[0.5,0,0.5],
          [0.5,1,0.5],[0,0.5,0.5],[1,0.5,0.5],
          [0.5,0.5,0],[0.5,0.5,1]]
lattice = Lattice.from_parameters(a=1,b=1,c=1,alpha=90,beta=90,gamma=90)
struct = Structure(lattice,["Si" for n in range(14)],coords)
#we need molecule type if we want to write data in a .xyz file
# using pymatgen.io.xyz
Si_FCC = Molecule(["Si" for n in range(14)],coords)
with open('structure.json','w') as f:
    dump(struct.as_dict(),f)
    f.close()
with open('structure.json','r') as f:
    d = load(f)
    structure = Structure.from_dict(d)
    f.close()
# xyz object
struct_xyz = xyz.XYZ(Si_FCC)
struct_xyz.write_file('structure.xyz')
# if you want to read this file please use:
# h = xyz.XYZ.from_file('structure.xyz')
# h.all_molecules



