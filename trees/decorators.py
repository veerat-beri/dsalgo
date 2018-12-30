def set_default_node(func):
    """
    Assign tree root as default node in 'Tree' methods
    """
    def assign_default(self, node=None):
        if node is None:
            node = self.root()
        return func(self, node)

    return assign_default

