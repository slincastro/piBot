import unittest
from mock import MagicMock
from control import Control
from mock import patch, sentinel

class TestControl(unittest.TestCase):

     @patch('control.Control')
     def test_should_configure_bcm_mode(self,mock):
        #mock = Control()
        #mock.setmode = MagicMock()
        mock.setUpValues()
        mock.setmode.assert_called_with()


if __name__ == '__main__':
  unittest.main()
