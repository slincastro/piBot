import unittest
from mock import MagicMock
from control import Control
from StubGPIO import StubGPIO

class TestControl(unittest.TestCase):

     def test_should_configure_bcm_mode(self):
        mock = StubGPIO()
        mock.setmode = MagicMock()

        subject = Control()
        subject.setUpValues(mock)
        mock.setmode.assert_called_with(123)


if __name__ == '__main__':
  unittest.main()
