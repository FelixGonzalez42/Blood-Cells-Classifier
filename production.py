from fastai.vision import load_learner, ImageList, DatasetType
import os

# Detecting and/or making the current image path
CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
DIRECTORY = os.path.join(CURRENT_FOLDER, 'models')

# modelo = "export-cells ResNet18.pkl"
modelo = "export-cells_EfficientNet.pkl"


learn = load_learner(DIRECTORY, modelo) # Load the full model

# learn.to_fp16() # It's necessary for the efficient model (exported as fp16)
learn.to_fp32()

def prediction(directorio, num_batch = 8):
    
    data = ImageList.from_folder(directorio) # build the ImageList from the folder
    learn.data.add_test(data) # add data to the test set of learn
    
    # get the probabilities of images
    preds,_ = learn.get_preds(ds_type=DatasetType.Test, n_batch=12)
    
    # Get the predictions (intenger indexes)
    y_pred = preds.argmax(dim=1).tolist() # using the arguments of the max probabilities
    
    D_pred = {n.name:learn.data.classes[y] for n,y in zip(data.items, y_pred)}   
                
    return D_pred 