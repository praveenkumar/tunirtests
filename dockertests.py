import unittest
import re
from .testutils import system


class TestBase(unittest.TestCase):

    def test_selinux(self):
        "Tests the SELinux"
        out, err, eid = system('sudo getenforce')
        out = out.strip()
        out = out.decode('utf-8')
        self.assertEqual(out, 'Enforcing')

    def test_logging(self):
        "Tests journald logging"
        out, err, eid = system('sudo journalctl -a --no-pager -r --since=$(date +%Y-%m-%d) -n1')
        out = out.decode('utf-8')
        self.assertGreater(len(out.split()), 3, "journalctl output is missing.")

    def test_services(self):
        "No service should fail in the startup."
        out, err, eid = system('systemctl --all --failed')
        out = out.decode('utf-8')
        self.assertIn('0 loaded units listed', out)


class TestDocker(unittest.TestCase):

    def test_docker_enabled(self):
        out, err, eid = system('sudo systemctl is-enabled docker')
        out = out.strip()
        out = out.decode('utf-8')
        self.assertEqual('enabled', out)

    def test_docker_running(self):
        out, err, eid = system('sudo systemctl is-active docker')
        out = out.strip()
        out = out.decode('utf-8')
        self.assertEqual('active', out)

    def test_docker_pull(self):
        out, err, eid = system('docker pull alpine')
        self.assertEqual(0, eid)

    def test_docker_run(self):
        out, err, eid = system('docker run --rm docker.io/alpine ls')
        self.assertEqual(0, eid)


if __name__ == '__main__':
    unittest.main()
