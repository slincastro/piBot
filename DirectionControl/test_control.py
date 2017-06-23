import unittest
from mock import MagicMock
from control import Control
from StubGPIO import StubGPIO

class TestControl(unittest.TestCase):

     def test_should_configure_bcm_mode(self):
        mock = Control()
        mock.setUpValues = MagicMock(return_value=3)
        var = mock.setUpValues()
        mock.setUpValues.assert_called()

if __name__ == '__main__':
  unittest.main()
