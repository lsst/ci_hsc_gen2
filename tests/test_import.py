import unittest

import lsst.utils.tests
import lsst.ci.hsc.gen2.validate


class ImportTest(unittest.TestCase):
    def testImport(self):
        self.assertTrue(hasattr(lsst.ci.hsc.gen2.validate, "RawValidation"))


class TestMemory(lsst.utils.tests.MemoryTestCase):
    pass


def setup_module(module):
    lsst.utils.tests.init()


if __name__ == "__main__":
    lsst.utils.tests.init()
    unittest.main()
