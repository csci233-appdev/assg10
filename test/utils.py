import sqlite3


def file_has_line(file, search_line):
    """Helper function, to determine if a particular line appears in the
    given file
    """
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if search_line in line:
                return True
    return False

def table_exists(dbfile, table):
    """Helper test function, checks if indicated table exists and returns
    true if it does and false if not"""
    # we will need a database connection to test with
    conn = sqlite3.connect(dbfile)
    cur = conn.cursor()

    # check that Majors table exists, for some reason the type="table" is case sensitive here
    # but count should be 1 if the table is in the sqlite_master 
    sql = '''SELECT COUNT(*) FROM sqlite_master WHERE type="table" and name=?'''
    cur.execute(sql, (table,))
    res = cur.fetchone()[0]
    conn.close()

    return res == 1