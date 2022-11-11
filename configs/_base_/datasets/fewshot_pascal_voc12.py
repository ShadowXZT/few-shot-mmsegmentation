# dataset settings
dataset_type = 'FewShotCustomDataset'
data_root = '/home/xshadow/hsnet/Datasets_HSN/VOC2012/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='FewShotResize', img_scale=(400, 400)),
    dict(type='FewShotNormalize', **img_norm_cfg),
    dict(type='FewShotFormatBundle'),
    dict(type='FewShotCollect', keys=['query_img', 'query_mask']),
]
test_pipeline = [
    dict(
        type='MultiScaleFlipAug',
        img_scale=(2048, 512),
        # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],
        flip=False,
        transforms=[
            dict(type='FewShotResize', img_scale=(400, 400)),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='FewShotCollect', keys=['query_img']),
        ])
]
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        split='trn',
        fold=0,
        data_root=data_root,
        img_dir='JPEGImages',
        ann_dir='SegmentationClass',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        split='val',
        fold=0,
        data_root=data_root,
        img_dir='JPEGImages',
        ann_dir='SegmentationClass',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        split='val',
        fold=0,
        data_root=data_root,
        img_dir='JPEGImages',
        ann_dir='SegmentationClass',
        pipeline=test_pipeline))
