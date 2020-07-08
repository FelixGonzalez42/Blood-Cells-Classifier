import numpy as np
import os


CLASES = ['NEUTROPHIL', 'LYMPHOCYTE', 'BASOPHIL', 'PLATELET', 'MONOCYTE',
 'EOSINOPHILS', 'ERYTROBLAST', 'IG']


def prediction(directorio, clases = CLASES):
     """ Random classification function"""

     filenames = os.listdir(directorio)
     clases_a = np.array(clases)
     ind = np.random.randint(0,7,len(filenames))    
     labels = clases_a[ind].tolist()
     

     return filenames, labels

