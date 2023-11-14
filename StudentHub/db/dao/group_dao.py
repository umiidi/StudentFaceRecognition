from db.dao.abstract_dao import AbstractDao
from db.entity.groups import Group

class GroupDao(AbstractDao):
    def get_all_groups(self):
        connection = self.connect()
        cursor = connection.cursor()
        query = "SELECT * FROM allgroup AS g"
        cursor.execute(query)
        group_records = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        groups = []
        for group in group_records:
            id = group[field_names.index('id')]
            name = group[field_names.index('name')]
            groups.append(Group(id=id, name=name))
        cursor.close()
        connection.close()
        return groups

    def get_group_by_id(self, group_id):
        connection = self.connect()
        cursor = connection.cursor()
        query = "SELECT g.id, g.name FROM allgroup AS g WHERE id = %s"
        cursor.execute(query, (group_id, ))
        group = cursor.fetchone()
        cursor.close()
        connection.close()
        if group:
            id, name = group
            return Group(id, name)
        else:
            return None

    def add_group(self, group):
        connection = self.connect()
        cursor = connection.cursor()
        query = "INSERT INTO allgroup (name) VALUES (%s)"
        cursor.execute(query, (group.name,))
        connection.commit()
        cursor.close()
        connection.close()
        return cursor.lastrowid
    
    def update_group(self, group):
        connection = self.connect()
        cursor = connection.cursor()
        query = "UPDATE allgroup SET name = %s WHERE id = %s"
        cursor.execute(query, (group.name, group.id))
        connection.commit()
        cursor.close()
        connection.close()

    def remove_group(self, group_id):
        connection = self.connect()
        cursor = connection.cursor()
        query = "DELETE FROM allgroup WHERE id = %s"
        cursor.execute(query, (group_id,))
        connection.commit()
        cursor.close()
        connection.close()