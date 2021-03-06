from cffconvert.ZenodoObject import ZenodoObject
import unittest
import os
import ruamel.yaml as yaml
from test.contracts.ZenodoObject import Contract


class ZenodoObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.zo = ZenodoObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.zo.check_cff_object()
        self.assertTrue(str(context.exception).startswith('\'cff-version\':') and
                        str(context.exception).endswith('isn\'t a supported version.'))

    def test_creators(self):
        pass

    def test_doi(self):
        pass

    def test_keywords(self):
        pass

    def test_license(self):
        pass

    def test_print(self):
        pass

    def test_publication_date(self):
        pass

    def test_title(self):
        pass

    def test_version(self):
        pass