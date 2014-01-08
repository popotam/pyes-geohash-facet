from pyes import facets


class GeohashFacet(facets.Facet):
    _internal_name = 'geohash'

    def __init__(self, name, **kwargs):
        self.field = kwargs.pop('field', None)
        self.factor = kwargs.pop('factor', 0)
        self.show_documents = kwargs.pop('show_documents', False)

        super(GeohashFacet, self).__init__(name, **kwargs)

    def _serialize(self):
        data = {}

        data['field'] = self.field
        data['factor'] = self.factor
        data['show_documents'] = self.show_documents

        return data
