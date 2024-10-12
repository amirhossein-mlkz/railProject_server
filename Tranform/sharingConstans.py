class STRUCT_PARTS:
    TRAIN = 'train'
    CAMERA = 'camera'
    YEAR = 'year'
    MONTH = 'month'
    DAY = 'day'
    HOUR = 'hour'
    MINUTE = 'minute'
    FILE = 'file'

DIRECTORY_TREE = [STRUCT_PARTS.TRAIN, 
                  STRUCT_PARTS.CAMERA, 
                  STRUCT_PARTS.YEAR,
                  STRUCT_PARTS.MONTH,
                  STRUCT_PARTS.DAY,
                  STRUCT_PARTS.HOUR,
                  STRUCT_PARTS.MINUTE,
                  STRUCT_PARTS.FILE
                ]



class StatusCodes:
    class findFilesStatusCodes:
        DIR_NOT_EXISTS = 0
        SUCCESS = 1

    class copyStatusCodes:
        DISCONNECT = 10
        SUCCESS=11

    class pingAndConnectionStatusCodes:
        NOT_CONNECT = 20
        SUCCESS = 21
