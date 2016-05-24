The actual tests for the ADB/CDK. There will be used for testing ADB/CDK Vagrant Images using [Tunir](http://tunir.rtfd.org).


##How to run test cases


####Step:1 Setup Tunir

```
# #If you want to have libvirt as default provider else install virtualbox
# sudo dnf install python-paramiko vagrant-libvirt python-crypto
# sudo systemctl enable libvirtd
# git clone https://github.com/kushaldas/tunir.git
# cd tunir
# ./tunir -h (This should not show any traceback).
```

####Step:2 Create Job file as input to tunir. 
       **Note**: Make sure this file is the same directory where you are executing tunir

```
# cat default.json
{
  "name": "cdkv2",
  "type": "vagrant",
  "image": "http://cbs.centos.org/kojifiles/work/tasks/2891/92891/centos-7-adb-2.1-0.x86_64.vsphere.ova",
  "ram": 2096,
  "user": "vagrant",
  "password": "vagrant",
  "provider": "virtualbox",
  "vagrantfile":"/tmp/Vagrantfile"
}
```

####Step:3 Create command txt file which should consist of test case to be executed. 
       **Note**: Make sure this file is the same directory where you are executing tunir

```
# cat default.txt
curl -O https://kumarpraveen.fedorapeople.org/tunirtests.tar.gz
tar -xzvf tunirtests.tar.gz
sudo python -m unittest -v tunirtests.dockertests.TestBase
sudo python -m unittest -v tunirtests.dockertests.TestDocker
sudo python -m unittest -v tunirtests.openshifttests.TestOpenshift
sudo sccli kubernetes start
sudo python -m unittest -v tunirtests.kubernetestests.TestKubernetes
```

####Step:4 Run tunir with a specific job

```
# ./tunir --job default
```


###Sample run only for openshift test cases (All test case passed)

```
# cat default.txt
curl -O https://kumarpraveen.fedorapeople.org/tunirtests.tar.gz
tar -xzvf tunirtests.tar.gz
sudo python -m unittest -v tunirtests.openshifttests.TestOpenshift

# ./tunir --job default
...
command: sudo python -m unittest -v tunirtests.openshifttests.TestOpenshift
status: True

test_openshift_enabled (tunirtests.openshifttests.TestOpenshift) ... ok
test_openshift_running (tunirtests.openshifttests.TestOpenshift) ... ok
test_registry_container_running (tunirtests.openshifttests.TestOpenshift) ... ok
test_router_container_running (tunirtests.openshifttests.TestOpenshift) ... ok

----------------------------------------------------------------------
Ran 4 tests in 60.236s

OK
```

###Sample run only for openshift test cases (if test case failed) 

```
$ sudo python -m unittest -v tunirtests.openshifttests.TestOpenshift
test_openshift_enabled (tunirtests.openshifttests.TestOpenshift) ... FAIL
test_openshift_running (tunirtests.openshifttests.TestOpenshift) ... FAIL
test_registry_container_running (tunirtests.openshifttests.TestOpenshift) ... FAIL
test_router_container_running (tunirtests.openshifttests.TestOpenshift) ... FAIL

======================================================================
FAIL: test_openshift_enabled (tunirtests.openshifttests.TestOpenshift)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tunirtests/openshifttests.py", line 13, in test_openshift_enabled
    self.assertEqual('enabled', out)
AssertionError: 'enabled' != u'disabled'

======================================================================
FAIL: test_openshift_running (tunirtests.openshifttests.TestOpenshift)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tunirtests/openshifttests.py", line 19, in test_openshift_running
    self.assertEqual('active', out)
AssertionError: 'active' != u'unknown'

======================================================================
FAIL: test_registry_container_running (tunirtests.openshifttests.TestOpenshift)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tunirtests/openshifttests.py", line 25, in test_registry_container_running
    self.assertTrue(re.search(r"ose-docker-registry", out), True)
AssertionError: True

======================================================================
FAIL: test_router_container_running (tunirtests.openshifttests.TestOpenshift)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tunirtests/openshifttests.py", line 31, in test_router_container_running
    self.assertTrue(re.search(r"ose-haproxy-router", out), True)
AssertionError: True

----------------------------------------------------------------------
Ran 4 tests in 60.230s

FAILED (failures=4)
```
