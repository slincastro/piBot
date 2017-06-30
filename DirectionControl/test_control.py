import unittest
from mock import MagicMock
from control import Control


class TestControl(unittest.TestCase):

     def test_should_configure_bcm_mode(self):
        mock = Control()
        mock.setmode = MagicMock()
        mock.setUpValues()
        mock.setmode.assert_called_with()


if __name__ == '__main__':
  unittest.main()
