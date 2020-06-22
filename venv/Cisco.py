import re
import pexpect
ping = pexpect.spawn('ping -c 5 localhost')