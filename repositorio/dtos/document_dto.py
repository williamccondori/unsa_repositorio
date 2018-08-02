class DocumentDto(object):
    def __init__(self, id=0, author_id=0, title='',
                 year=1900, summary='', document_file=None):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.year = year
        self.summary = summary
        self.document_file = document_file
