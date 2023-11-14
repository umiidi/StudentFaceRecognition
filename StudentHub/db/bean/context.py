def student_dao():
    from db.dao.student_dao import StudentDao
    return StudentDao()

def face_record_dao():
    from db.dao.face_record_dao import FaceRecordDao
    return FaceRecordDao()

def group_dao():
    from db.dao.group_dao import GroupDao
    return GroupDao()