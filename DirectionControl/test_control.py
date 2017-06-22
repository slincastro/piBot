import unittest
from control import Control

class TestControl(unittest.TestCase):

    def test_should_configure_bcm_mode(self):
        real = GPIO
        real.method = MagicMock(name='setmode')
        real.method('bcm')

        real.something.assert_called_once_with(1, 2, 3)
        Control.setUpValues(self,)
        self.assertTrue(false)

if __name__ == '__main__':
  unittest.main()
