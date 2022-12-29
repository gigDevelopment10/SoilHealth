import mrcnn.config
import mrcnn.model
class SimpleConfig(mrcnn.config.Config):
    NAME = "coco_inference"

    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    NUM_CLASSES = 81

model = mrcnn.model.MaskRCNN(mode="inference", 
    config=SimpleConfig(),
    model_dir=os.getcwd())
#print(model.keras_model.summary())
model.load_weights(filepath="mask_rcnn_coco.h5", 
                   by_name=True)