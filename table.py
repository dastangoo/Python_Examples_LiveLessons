# table.py
def print_table(objects, colnames, formatter):
    '''
    Make a nicely formatted table showing attributes from a list of objects
    '''
    formatter.headings(colnames)

    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)

class TableFormatter(object):
    # Serves a design spec for making tables (use inheritance to customize)
    def headings(self, headers):
        raise NotImplementedError
    def row(self, rowdata):
        raise NotImplementedError

class TextFormatter(TableFormatter):
    def headings(self, headers):
        for header in headers:
            print('{:>10s}'.format(header), end=' ')
        print()

    def row(self, rowdata):
        for item in rowdata:
            print('{:>10s}'.format(item), end=' ')
        print()
        ...
class CSVFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>{}</th>'.format(h), end='')
        print('</tr>')
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>{}</td>'.format(d), end='')
        print('</tr>')
