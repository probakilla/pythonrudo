import unittest

from attr import attrs, attrib
from tests.test_dice import DiceTestCase


@attrs
class CustomTestSuite:
    suite = attrib(default=unittest.TestSuite())

    def run(self):
        self.suite.addTest(unittest.makeSuite(DiceTestCase))
        runner = unittest.TextTestRunner()
        runner.run(self.suite)


def main():
    CustomTestSuite().run()


if __name__ == "__main__":
    main()
