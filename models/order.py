class Order():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id_, style_id, metal_id, size_id):
        self.id_ = id_
        self.style_id = style_id
        self.metal_id = metal_id
        self.size_id = size_id
        self. metal = None
        self. size = None
        self. style = None
