# yapf:disable
log_config = dict(
    interval=100,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        #dict(type='MMSegWandbHook', by_epoch=False,
        #     init_kwargs={'entity': "xshadow",
        #                  'project': "VPA-FSS",
        #                  'config': dict(fold=0,backbone='resnet50',seg_head='deeplabv3+')
        #                 }
        #     )
        # dict(type='TensorboardLoggerHook')
        # dict(type='PaviLoggerHook') # for internal services
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
cudnn_benchmark = True
