# egohands_datasets

**Dataset structure:**
- Download [Labeled Data](http://vision.soic.indiana.edu/projects/egohands/), get:

```
.
├── DEMO_1.m
├── DEMO_2.m
├── getBoundingBoxes.m
├── getFramePath.m
├── getMetaBy.m
├── getSegmentationMask.m
├── _LABELLED_SAMPLES
│   ├── CARDS_COURTYARD_B_T
│   │   ├── frame_0011.jpg
│   │   ├── frame_0036.jpg
│   │   ├── frame_0099.jpg
│   │   ├── frame_0113.jpg
│   │   ├── frame_0176.jpg
|
|
├── metadata.mat
├── README.txt
└── showLabelsOnFrame.m

```
Follow README.txt, get extract hand from image for creating hand_dataset.

Results: 
[sample1](img_sample/CHESS_OFFICE_H_T_frame_1548_2_hand.png)
[sample2](img_sample/PUZZLE_OFFICE_S_T_frame_1556_3_hand.png)
