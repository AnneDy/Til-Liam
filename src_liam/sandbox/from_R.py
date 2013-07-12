# s'inspire fortee;ent de build_from_sources

import pandas.rpy.common as com 
import rpy2.rpy_classic as rpy
import pdb 

rpy.set_default_mode(rpy.NO_CONVERSION)
data = "T:/Myliam2/Patrimoine/ici.Rdata"

rpy.r.load(data)
pdb.set_trace()

menage = com.load_data('person')