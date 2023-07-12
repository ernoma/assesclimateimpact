import unittest
import getpass
import re

class TestGetOutputTableName(unittest.TestCase):
    def setUp(self):
        self.connParams = {'user': 'test_user'}
        self.NameOfTheCO2EstimationRun = 'Test Run'
        self.sessionParams = {'uuid': '12345678-1234-1234-1234-123456789abc'}

    def test_getOutputTableName_with_connParams(self):
        outputTableName = getOutputTableName(self)
        expectedOutputTableName = 'o_test_user_t_test_run_12345678123412341234123456789abc'
        self.assertEqual(outputTableName, expectedOutputTableName)

    def test_getOutputTableName_without_connParams(self):
        self.connParams = None
        outputTableName = getOutputTableName(self)
        expectedOutputTableName = 'o_unknown_t_test_run_12345678123412341234123456789abc'
        self.assertEqual(outputTableName, expectedOutputTableName)


if __name__ == '__main__':
    unittest.main()
    