#!/bin/bash

#test

python3 test_extract_feature_maps.py \
--data data/large.yaml \
--device 5 \
--img 480 \
--batch 1 \
--conf 0.5 \
--iou 0.5 \
--weights "/home/aslane84/curriculum_yolov7/weights/epoch_049.pt" \
--name   "CL_yolov7_"