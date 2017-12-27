import unittest

from cw_msgpack_coder.umsgpack_coder import UmsgpackCoder


class TestUmsgpackCoder(unittest.TestCase):
    class EmptyClass:
        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            if self.__dict__ != other.__dict__:
                return False
            return True

    def test_encode_empty_class(self):
        coder = UmsgpackCoder()
        coder.set_default_coder_for_class(self.EmptyClass)
        o = self.EmptyClass()
        s = coder.dumps(o)
        o2 = coder.loads(s)
        self.assertEqual(o, o2)

    class DictClass:
        def __init__(self, a):
            self.a = a

        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            if self.__dict__ != other.__dict__:
                return False
            return True

    def test_encode_dict_class(self):

        coder = UmsgpackCoder()
        coder.set_default_coder_for_class(self.DictClass)
        o = self.DictClass(1)
        s = coder.dumps(o)
        o2 = coder.loads(s)
        self.assertEqual(o, o2)

    class SlotClass:
        __slots__ = 'ab'

        def __init__(self, ab):
            self.ab = ab

        def __eq__(self, other):
            if getattr(self, self.__slots__) != getattr(other, self.__slots__):
                return False
            return True

    def test_encode_single_slot_class(self):

        coder = UmsgpackCoder()
        coder.set_default_coder_for_class(self.SlotClass)
        o = self.SlotClass(1)
        s = coder.dumps(o)
        o2 = coder.loads(s)
        self.assertEqual(o, o2)

    class MultiSlotClass:
        __slots__ = 'a', 'b'

        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __eq__(self, other):
            for attr in self.__slots__:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            return True

    def test_encode_multi_slot_class(self):

        coder = UmsgpackCoder()
        coder.set_default_coder_for_class(self.MultiSlotClass)
        o = self.MultiSlotClass(1, 2)
        s = coder.dumps(o)
        o2 = coder.loads(s)
        self.assertEqual(o, o2)

    class FirstComponentClass:
        def __init__(self, a):
            self.a = a

        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            if self.__dict__ != other.__dict__:
                return False
            return True

    class SecondComponentClass:
        def __init__(self, a):
            self.a = a

        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            if self.__dict__ != other.__dict__:
                return False
            return True

    class CompoundClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __eq__(self, other):
            if type(self) is not type(other):
                return False
            if self.__dict__ != other.__dict__:
                return False
            return True

    def test_encode_compound_class(self):
        coder = UmsgpackCoder()
        coder.set_default_coder_for_class(self.CompoundClass)
        coder.set_default_coder_for_class(self.FirstComponentClass)
        coder.set_default_coder_for_class(self.SecondComponentClass)
        o = self.CompoundClass(self.FirstComponentClass(1), self.SecondComponentClass(2))
        s = coder.dumps(o)
        o2 = coder.loads(s)
        self.assertEqual(o, o2)

    def test_encode_compound_of_compound_class(self):
        coder = UmsgpackCoder()
        coder.set_default_coder_for_class(self.CompoundClass)
        coder.set_default_coder_for_class(self.FirstComponentClass)
        coder.set_default_coder_for_class(self.SecondComponentClass)
        a = self.CompoundClass(self.FirstComponentClass(1), self.SecondComponentClass(2))
        b = self.CompoundClass(self.FirstComponentClass(1), self.SecondComponentClass(2))
        o = self.CompoundClass(a, b)
        s = coder.dumps(o)
        o2 = coder.loads(s)
        self.assertEqual(o, o2)

