from pyes import facets


class GeohashFacet(facets.Facet):
    _internal_name = 'geohash'

    def __init__(self, name, **kwargs):
        self.field = kwargs.pop('field', None)
        self.factor = kwargs.pop('factor', 0)
        self.show_doc_id = (
            kwargs.pop('show_doc_id', False)
            or kwargs.pop('show_documents', False)
        )
        self.show_geohash_cell = kwargs.pop('show_geohash_cell', False)

        super(GeohashFacet, self).__init__(name, **kwargs)

    def _serialize(self):
        data = {}

        data['field'] = self.field
        data['factor'] = self.factor
        data['show_documents'] = self.show_doc_id
        data['show_doc_id'] = self.show_doc_id
        data['show_geohash_cell'] = self.show_geohash_cell

        return data
