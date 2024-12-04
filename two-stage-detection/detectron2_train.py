import os
from detectron2.utils.logger import setup_logger
from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.data.datasets import register_coco_instances
from detectron2.engine import DefaultTrainer
import wandb

setup_logger()
LOG_DIR = "./logs"

os.environ["WANDB__SERVICE_WAIT"] = "300"
wandb.tensorboard.patch(root_logdir=LOG_DIR)
wandb.init(
    project="two-stage-weed",
    mode="offline",
    sync_tensorboard=True
)

class FasterRCNN():
    
    TRAIN_DIR = "../datasets/Annotated-Images-for-Automated-Weed-Identification-and-Management/train"
    TEST_DIR = "../datasets/Annotated-Images-for-Automated-Weed-Identification-and-Management/test"
    TRAIN_FILENAME = "weed_detection_train"
    TEST_FILENAME = "weed_detection_test"
    CONFIG_FILEPATH = "COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml"

    def register_datasets(self):
        register_coco_instances(self.TRAIN_FILENAME, {}, self.TRAIN_DIR + "/_annotations.coco.json", self.TRAIN_DIR)
        register_coco_instances(self.TEST_FILENAME, {}, self.TEST_DIR + "/_annotations.coco.json", self.TEST_DIR)

    def configure_training(self):
        cfg = get_cfg()
        cfg.merge_from_file(model_zoo.get_config_file(self.CONFIG_FILEPATH))
        cfg.DATASETS.TRAIN = (self.TRAIN_FILENAME,)
        cfg.DATASETS.TEST = (self.TEST_FILENAME,)
        cfg.DATALOADER.NUM_WORKERS = 2
        cfg.MODEL.WEIGHTS = "./pretrained_weights/model_final_68b088.pkl"
        # cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(self.CONFIG_FILEPATH) # Note: needs to be online

        cfg.SOLVER.IMS_PER_BATCH = 2
        cfg.SOLVER.BASE_LR = 0.00025
        cfg.SOLVER.MAX_ITER = 1200
        cfg.MODEL.ROI_HEADS.NUM_CLASSES = 2
        cfg.MODEL.DEVICE = "cpu" # TODO: Change to GPU
        return cfg

    def train_model(self, cfg):
        os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
        trainer = DefaultTrainer(cfg) 
        trainer.resume_or_load(resume=False)
        trainer.train()


if __name__ == "__main__":
    faster_rcnn = FasterRCNN()
    faster_rcnn.register_datasets()
    cfg = faster_rcnn.configure_training()
    faster_rcnn.train_model(cfg)
