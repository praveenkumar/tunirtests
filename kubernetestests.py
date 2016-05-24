import unittest
import re
import time
from .testutils import system


class TestKubernetes(unittest.TestCase):

    def test_kubernetes_status(self):
        out, err, eid = system('sudo sccli kubernetes status')
        self.assertEqual(0, eid)

    def test_kubernetes_node(self):
        time.sleep(2)
        out, err, eid = system('kubectl get nodes')
        out = out.decode('utf-8')
        self.assertTrue(re.search(r"Ready", out), True)


if __name__ == '__main__':
    unittest.main()
