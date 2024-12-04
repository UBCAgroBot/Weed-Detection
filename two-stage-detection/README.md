## Instructions

### Create the environment and activate it:
```
conda env create -f environment.yml -n two-stage-detection
conda activate two-stage-detection
```

### How to submit a job (note! change the email in the script.sh file to your own): 
```
cd two-stage-detection
sbatch script.sh
```

Model outputs will be saved in the `outputs` folder. Load it in a jupyter notebook to visualize the results and conduct error analysis. If you want to retrain or change the model parameters, you can modify the `detectron2_train.py` file or create a new config file in `detectron2/configs/`. After you run the job, you can sync Weights & Biases by running `wandb sync`.

*Note*: The `detectron2_train.py` file is modified from the original detectron2 repository. The original repository can be found [here](https://github.com/facebookresearch/detectron2).
