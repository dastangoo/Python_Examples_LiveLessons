# table.py
def print_table(objects, colnames):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    '''
    formatter.headings(colnames)

    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowd)

class TableFormatter(object):
    def headings(self, headers):
        raise NotImplementedError
    def row(self, rowdata):
        raise NotImplementedError
