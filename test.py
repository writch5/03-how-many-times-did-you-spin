import pexpect
import sys
def test_north_facing():
    spin_process = pexpect.spawnu('python3 spin.py', logfile=sys.stdout)
    spin_process.expect('How many times did you spin?')
    spin_process.sendline('3')
    spin_process.expect('You are facing 0.0 degrees relative to north')

def test_south_facing():
    spin_process = pexpect.spawnu('python3 spin.py', logfile=sys.stdout)
    spin_process.expect('How many times did you spin?')
    spin_process.sendline('-2.5')
    spin_process.expect('You are facing 180.0 degrees relative to north')

def test_east_facing():
    spin_process = pexpect.spawnu('python3 spin.py', logfile=sys.stdout)
    spin_process.expect('How many times did you spin?')
    spin_process.sendline('-2.75')
    spin_process.expect('You are facing 90.0 degrees relative to north')

def test_west_facing():
    spin_process = pexpect.spawnu('python3 spin.py', logfile=sys.stdout)
    spin_process.expect('How many times did you spin?')
    spin_process.sendline('2.75')
    spin_process.expect('You are facing 270.0 degrees relative to north')