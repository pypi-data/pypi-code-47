"""OrderingItem

This package defines an OrderingItem base. The OrderingItem base should be subclassed in SQLAlchemy database models which are children of orderinglist relationships.

The OrderingItem subclass ensures that setting the child's parent attribute gives the child an appropriate `index` (the column on which the orderinglist is sorted).
"""

from sqlalchemy.inspection import inspect

class OrderingItem():
    _exempt_attrs_oi = [
        '_orderinglist_parent_indicator', '_orderinglist_parent_attrs'
    ]

    def __new__(cls, *args, **kwargs):
        """
        Set class orderinglist parent indicators and orderinglist parent 
        attributes.

        orderinglist_parent_indicator maps attribute name to indicator that 
        the attribute is a parent of an orderinglist relationship to self.

        orderinglist_parent_attrs maps parent name to (childlist, order_by) 
        tuple.
        """
        if not hasattr(cls, '_orderinglist_parent_indicator'):
            cls._orderinglist_parent_indicator = {}
            cls._orderinglist_parent_attrs = {}
        try:
            return super().__new__(cls, *args, **kwargs)
        except:
            return super().__new__(cls)

    def __setattr__(self, name, value):
        """Set attribute

        Before setting an attribute, determine if it is the parent of an 
        orderinglist relationship to self. If so, use append insead of set 
        to add self to the parent's list of children.
        """
        if name in self._exempt_attrs_oi:
            return super().__setattr__(name, value)
        is_parent = self._orderinglist_parent_indicator.get(name)
        if is_parent is None:
            is_parent = self._set_orderinglist_parent(name)
        if is_parent:
            childlist, order_by = self._orderinglist_parent_attrs[name]
            if value is None:
                super().__setattr__(name, None)
                super().__setattr__(order_by, None)
            else:
                getattr(value, childlist).append(self)
        else:
            super().__setattr__(name, value)
    
    @classmethod
    def _set_orderinglist_parent(cls, name):
        """
        Set the orderinglist parent status for a previously unseen attribute
        """
        if not hasattr(cls, name):
            is_parent = False
        else:
            mapper = inspect(cls).mapper
            rel = [r for r in mapper.relationships if r.key == name]
            if not rel:
                is_parent = False
            else:
                is_parent = cls._handle_relationship_ol(name, rel)
        cls._orderinglist_parent_indicator[name] = is_parent
        return is_parent

    @classmethod
    def _handle_relationship_ol(cls, name, rel):
        """Handle relationship 
        
        set_orderinglist_parent calls this method when setting the 
        orderinglist parent status for an attribute which has a relationship 
        to self.
        """
        reverse_rel = list(rel[0]._reverse_property)
        if not reverse_rel:
            return False
        reverse_rel = reverse_rel[0]
        cc = reverse_rel.collection_class
        if (
            hasattr(cc, '__module__') 
            and cc.__module__ == 'sqlalchemy.ext.orderinglist'
        ):
            cls._store_orderinglist_parent_attrs(name, reverse_rel)
            return True
        return False
    
    @classmethod
    def _store_orderinglist_parent_attrs(cls, name, reverse_rel):
        """Store attributes of a parent of an orderinglist relationship

        Key attributes are (childlist, order_by). This method expects the 
        zeroth order_by column is the index of the orderinglist collection 
        class.
        """
        cls._orderinglist_parent_attrs[name] = (
            reverse_rel.key, reverse_rel.order_by[0].name
        )