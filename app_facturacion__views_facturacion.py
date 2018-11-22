
# @class_declaration vbarba_cash #
class vbarba_cash(vbarba_cabrera):
    FILE_UPLOAD_DIR = '/mnt/carros/CASH'
    # FILE_UPLOAD_DIR = '/var/www/images'

    def __init__(self, context=None):
        super(vbarba_cash, self).__init__(context)

