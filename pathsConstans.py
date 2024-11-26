import os

class pathConstants:
    SELF_SHARE_NAME = 'rail_share'
    SELF_SHARE_PATH = 'C:\\rail_share'
    SELF_IMAGES_FOLDR = 'images'
    SELF_IMAGES_DIR = os.path.join(SELF_SHARE_PATH, SELF_IMAGES_FOLDR)
    SELF_UTILS_FOLDER = 'utils'
    SELF_UTILS_DIR = os.path.join(SELF_SHARE_PATH, SELF_UTILS_FOLDER)

    OTHER_SHARE_NAME= "rail_share"
    
    OTHER_IMAGES_SHARE_FOLDER = os.path.join(OTHER_SHARE_NAME,'images')
    OTHER_UTILS_SHARE_FOLDER = os.path.join(OTHER_SHARE_NAME,'utils')
    OTHER_LOGS_SHARE_FOLDER = os.path.join(OTHER_UTILS_SHARE_FOLDER,'logs')
    OTHER_CONFIG_SHARE_PATH = os.path.join(OTHER_UTILS_SHARE_FOLDER,'config.json')


