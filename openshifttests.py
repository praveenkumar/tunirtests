import unittest
import re
import time
from .testutils import system


class TestOpenshift(unittest.TestCase):

    def test_openshift_enabled(self):
        out, err, eid = system('sudo systemctl is-enabled openshift')
        out = out.strip()
        out = out.decode('utf-8')
        self.assertEqual('enabled', out)

    def test_openshift_running(self):
        out, err, eid = system('sudo systemctl is-active openshift')
        out = out.strip()
        out = out.decode('utf-8')
        self.assertEqual('active', out)

    def test_registry_container_running(self):
        time.sleep(30)
        out, err, eid = system('docker ps --filter "name=k8s_registry.*"')
        out = out.decode('utf-8')
        self.assertTrue(re.search(r"ose-docker-registry", out), True)

    def test_router_container_running(self):
        time.sleep(30)
        out, err, eid = system('docker ps --filter "name=k8s_router.*"')
        out = out.decode('utf-8')
        self.assertTrue(re.search(r"ose-haproxy-router", out), True)


if __name__ == '__main__':
    unittest.main()
