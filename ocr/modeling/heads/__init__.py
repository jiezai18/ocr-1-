
__all__ = ['build_head']


def build_head(config):
    # det head
    from .det_db_head import DBHead
    from .det_east_head import EASTHead
    from .det_sast_head import SASTHead
    from .e2e_pg_head import PGHead

    # rec head
    from .rec_ctc_head import CTCHead
    from .rec_att_head import AttentionHead
    from .rec_srn_head import SRNHead

    # cls head
    from .cls_head import ClsHead
    support_dict = [
        'DBHead', 'EASTHead', 'SASTHead', 'CTCHead', 'ClsHead', 'AttentionHead',
        'SRNHead', 'PGHead', 'TableAttentionHead']

    #table head
    from .table_att_head import TableAttentionHead

    module_name = config.pop('name')
    assert module_name in support_dict, Exception('head only support {}'.format(
        support_dict))
    module_class = eval(module_name)(**config)
    return module_class
