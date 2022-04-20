_base_ = './cascade_rcnn_r50_caffe_fpn_1x_coco.py'
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='checkpoints/cascade_rcnn_r50_fpn_dconv_c3-c5_1x_coco_20200130-2f1fca44.pth')))
