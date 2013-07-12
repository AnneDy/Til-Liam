# -*- coding:utf-8 -*-

# on dit à la fonction main (qui est ce qui est appelé avec f5 ou f6 d'être utilisée avec les paramètres que l'on donne à sys.argv

import sys
import main #je laisse le main parce que je ne veux pas travailler sur le import, je laisse celui de LIAM2
from simulation import Simulation



chemin = 'C:\\Users\\a.eidelman\\Desktop\\GenIPP_Pyth\\liam\\'
chemin = 'M:\\Myliam2\\'
chemin = 'C:\\Myliam2\\'


#import
sys.argv.append('import')
fichier= chemin + 'model\\import_patrimoineR.yml'
sys.argv.append(fichier)  
#main.main()


#demo01
fichier=chemin+'test\\examples\\demo01.yml'
fichier= chemin + 'tests\\functional\\simulation.yml'
fichier= chemin+'Genebios\\vieillissement_genebios.yml'

fichier= chemin+'Patrimoine\\duplication\\expand.yml'


fichier= chemin+'Genebios\\console_test_marriage.yml'
fichier= chemin+'Genebios\\console_genebios.yml'


fichier= chemin+'Patrimoine\\lien_parent_enfant\\match_par_enf.yml'
fichier= chemin+'Patrimoine\\lien_parent_enfant\\expand.yml'
fichier= chemin+'Patrimoine\\lien_parent_enfant\\match_par_enf.yml'
fichier= chemin+'Patrimoine\\lien_parent_enfant\\match_score.yml'

#fichier= chemin+'Model\\expand.yml'

fichier= chemin+'Model\\console.yml'
fichier= chemin+'Model\\retro_marit.yml'
fichier= chemin+'Model\\console.yml'
#fichier= chemin + 'tests\\functional\\simulation.yml'

simulation= Simulation.from_yaml(
                                 fichier,
                     input_dir=None,
                    input_file=None,
                    output_dir=None,                    
                    output_file=None)

# simulation.run(False)

import cProfile
command = """simulation.run(False)"""
cProfile.runctx( command, globals(), locals(), filename="OpenGLContext.profile" )
