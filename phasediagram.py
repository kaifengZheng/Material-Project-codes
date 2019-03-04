from pymatgen.core.periodic_table import Element
from pymatgen.ext.matproj import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram,PDPlotter
a = MPRester("Your API Key") #generate on Dashboard of MaterialProject
entries = a.get_entries_in_chemsys(['Ca', 'C','O'])
$generate a PhaseDiagram object
pd = PhaseDiagram(entries)
plotter = PDPlotter(pd)
plotter.show()

#show data using the pd, a PhaseDiagram object
#all_entries(type: list): 
#people who use it can query all information of the phase construction,
#which means they will get information about elements, 
#components made by those elements. Taking an example of Li-Fe-O system

pd.all_entries

#elements(type:list): generate a list of elements which using in phase diagram calculation.
#Notes that elements has Element type requiring Element type from pymatgen.core.periodic_table class

pd.elements

#qhull_data(type: numpy.array): matrix contains composition data and energy data

pd.qhull_data

#Simplexes: The list of stable compositional coordinates in the phase diagram, 
#which we can use to draw a phase diagram.

pd.Simplexes

