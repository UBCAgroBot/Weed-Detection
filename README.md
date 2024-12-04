## **Weed Detection Specifications**

Weed object detection will be a crucial task involved in FRE 2025\. Please read more about the competition [here](https://fieldrobot.nl/event/). Our goal is to develop an object detection model capable of identifying various types of weeds, delivering bounding boxes and class probabilities to the extermination subteam. Since the competition has not specified which weed species will be used, our model should generalize across different types.

This project will be split into two teams: one-stage object detection and two-stage object detection (you can read about the differences between the two [here](https://viso.ai/deep-learning/object-detection/), scroll to One-Stage vs Two-Stage). The general idea is to create two different weed models so the competition team can choose between the two depending on the exact situation and task (the full competition specifications are yet to be released).

### **Expected/Targeted Skills:**

* Convolutional Neural Networks
* Image Segmentation
* One-Stage/Two-Stage Object Detection

### **Goals:**

* **Accuracy:** Accurately detect weeds, minimizing false positives and false negatives. Our used metric will be mean average precision (mAP). May also look into other metrics like Intersection over Union (IoU).
* **Real-Time Processing:** Ensure the processes images or video frames in real-time or near real-time to support timely decision-making. It is known that one-stage object detection is often faster than two-stage object detection – however, depending on exact conditions during the competition, having both models will increase our adaptability to handle different scenarios.
* **Can Generalize Well to Real Time Conditions:** Design the model to adapt to different environmental conditions and camera setups. One way to achieve this is to use data augmentation to simulate crops under different lighting conditions.

### **Miscellaneous:**

* **Potential Models:** Faster R-CNN, YOLOv8
* **Data Sources:** RoboFlow, Kaggle, agricultural image databases


### **Common Mistakes**

* when adding a dataset or a large file, make sure to add it to the .gitignore file so it is not uploaded to github


