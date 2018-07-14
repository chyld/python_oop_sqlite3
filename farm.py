import sqlite3
from dog import Dog


class Farm:
    def __init__(self, _id, name, dbname):
        self._id = _id
        self.name = name
        self.animals = Dog.find_by_farm_id(dbname, _id)
        self.dbname = dbname

    def teleport(self, to_fid, animal_id):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        sql = 'update dogs set farm_id = {} where id = {}'.format(to_fid, animal_id)
        cur.execute(sql)
        conn.commit()
        conn.close()

    @staticmethod
    def find(dbname):
        farms = []
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        for row in cur.execute('select * from farms'):
            farm = Farm(*row, dbname)
            farms.append(farm)
        conn.commit()
        conn.close()
        return farms

    def __str__(self):
        return "{} - {} has {} animals".format(self._id, self.name, len(self.animals))

    def __repr__(self):
        return self.__str__()
