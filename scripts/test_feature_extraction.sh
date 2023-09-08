#!/bin/bash

#test

python3 test_extract_feature_maps.py \
--data data/rw_small.yaml \
--device 5 \
--img 480 \
--batch 20 \
--conf 0.5 \
--iou 0.5 \
--weights "/home/aslane84/curriculum_yolov7/runs/train/CL_yolov7_112/weights/epoch_049.pt" \
--name   "CL_yolov7_"