from detectron2.data.datasets import register_coco_instances
from definitions import DATA_DIR, AUG_DATA_DIR
import os


DATASETS = {
    "Annotated-Images-for-Automated-Weed-Identification-and-Management--train": {
        "path": os.path.join(DATA_DIR, "Annotated-Images-for-Automated-Weed-Identification-and-Management"),
        "split": "train"
    },
    "Annotated-Images-for-Automated-Weed-Identification-and-Management--test": {
        "path": os.path.join(DATA_DIR, "Annotated-Images-for-Automated-Weed-Identification-and-Management"),
        "split": "test"
    },
    "kaggle-crop-and-weed-detection-data-with-bounding-boxes.coco": {
        "path": os.path.join(DATA_DIR, "kaggle-crop-and-weed-detection-data-with-bounding-boxes.coco"),
        "split": "train"
    },
    "weed_detection.v1i.yolov11.coco": {
        "path": os.path.join(DATA_DIR, "weed_detection.v1i.yolov11.coco"),
        "split": "train"
    },
    "Annotated-Images-for-Automated-Weed-Identification-and-Managements_AUGMENTED": {
        "path": os.path.join(AUG_DATA_DIR, "Annotated-Images-for-Automated-Weed-Identification-and-Managements_AUGMENTED"),
        "split": "train"
    },
    # "WeedCrop.v1i.yolov5pytorch.coco": {
    #     "path": os.path.join(DATA_DIR, "WeedCrop.v1i.yolov5pytorch.coco"),
    #     "split": "train"
    # },
    # "Weeds.v3-augmented_nottrained.yolov11": {
    #     "path": os.path.join(DATA_DIR, "Weeds.v3-augmented_nottrained.yolov11"),
    #     "split": "train"
    # },
}


def register_datasets() -> None:
    # TODO: rename datasets/WeedCrop.v1i.yolov5pytorch.coco/_annotations_coco_data_1.json
    for name, path in DATASETS.items():
        register_coco_instances(name, {}, os.path.join(path, "_annotations.coco.json"), path)
