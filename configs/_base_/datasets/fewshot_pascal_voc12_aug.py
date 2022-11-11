_base_ = './fewshot_pascal_voc12.py'
# dataset settings
data = dict(
    train=dict(
        ann_dir='SegmentationClassAug',
        split='trn'))
