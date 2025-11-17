# Face-RF-DETR
Real time detection rf-detr finetuned for face detection.

## Intro
RF-Detr medium trained over Wideface validation dataset split into train , test and validation sets respecting coco format , finetuned over 10 epochs.

## Technical challenges 
The model was trained on kaggle P100 GPU which was successful after several OOM (Out of memory) with both colab T4 and even kaggle 2 x T4 using distributed training (hyperparameter tuning for effecient VRAM management failed for T4, yet the P100 worked first try , according to documentation and gpu specs P100 is optimized for training wheras T4 for inference , additionally it has extra memory 16GB vs 15GB (respectively P100 vs T4)).

The OOM accures with relatively high epochs count (in the case described above 10) for less it doable such as 9, 7 or 5.(tuning hyperparameter such grad_accum_steps still required).

## Results 
<img width="1800" height="1200" alt="image" src="https://github.com/user-attachments/assets/184d8fe3-035e-483b-b956-91bacf3ca659" />
