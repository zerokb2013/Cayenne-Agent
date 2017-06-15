import unittest
from myDevices.utils.logger import setInfo, info
from myDevices.os.hardware import Hardware, MAPPING, BOARD_REVISION, CPU_REVISION

class HarwareTest(unittest.TestCase):
    def setUp(self):
        setInfo()
        self.hardware = Hardware()

    def testGetManufacturer(self):
        manufacturer = self.hardware.getManufacturer()
        info(manufacturer)
        self.assertNotEqual(manufacturer, '')

    def testGetModel(self):
        model = self.hardware.getModel()
        info(model)
        self.assertNotEqual(model, 'Unknown')

    def testGetMac(self):
        mac = self.hardware.getMac()
        info(mac)
        self.assertRegex(mac, '^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$')

    def testMapping(self):
        info(MAPPING)
        self.assertTrue(MAPPING)

    def testBoardRevision(self):
        info(BOARD_REVISION)
        self.assertNotEqual(BOARD_REVISION, 0)

    def testCpuRevision(self):
        info(CPU_REVISION)
        self.assertNotEqual(CPU_REVISION, '0')

if __name__ == '__main__':
    unittest.main()