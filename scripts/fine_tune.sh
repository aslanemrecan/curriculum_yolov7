#!/bin/bash
datasets=("data/large.yaml" "data/medium.yaml" "data/small.yaml")
epochs=(40 35 25)
weight_names=("weights/yolov7-tiny.pt" "weights/large.pt" "weights/medium.pt" "weights/small.pt")

for i in "${!datasets[@]}"
do
    dataset="${datasets[i]}"
    epoch="${epochs[i]}"
    weights="${weight_names[i]}"

    echo "Training" $weights "on" $dataset 

    nohup python3 train.py \
    --epochs $epoch \
    --workers 8 \
    --device 5 \
    --batch-size 64 \
    --data $dataset \
    --img 480 480 \
    --entity "aslane84" \
    --name CL_yolov7_ \
    --cfg cfg/training/yolov7-tiny-drone.yaml \
    --weights $weights \
    --hyp data/hyp.drone.tiny.yaml \
    --multi-scale \
    --save_period 1 \
    | tee outputs/5.out

    save_weights_folder_name=$(ls -lt runs/train/ | grep '^d' | head -n 1 | awk '{print $9}')
    save_weights_file_name="runs/train/$save_weights_folder_name/weights/best.pt"
    cp $save_weights_file_name ${weight_names[i+1]}

done
