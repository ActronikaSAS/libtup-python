# Python LibTUP

[![Build Status](http://jenkins.actronika.com:8080/buildStatus/icon?job=libtup-python)](https://jenkins.actronika.com:8080/job/libtup-python/)

## About libtup

This library contains message definition for tactronik UART API and helpers to send/receive them.

More information on github project : [https://github.com/ActronikaSAS/libtup](https://github.com/ActronikaSAS/libtup)

## Dependency

To use this library need to have *libsmp* and `numpy`

```bash
git clone git@github.com:ActronikaSAS/libsmp-python.git libsmp
sudo -H pip3 install -r requirement.txt
```

To build unit test need to install dependencies in file `dev-requirement.txt`

```bash
sudo -H pip3 install -r dev-requirement.txt
```

## Example

```python
#!/usr/bin/env python3

import libtup

# Generate message to get version
message = libtup.tup_message_init_get_version()
print(message)
"""
<id:13,values:[]>
"""

# Generate message to get buildinfo
message = libtup.tup_message_get_buildinfo()
print(message)
"""
<id:19,values:[]>
"""

# Generate message to load effect 0x25 in slot 2
message = libtup.tup_message_init_load(0x25, 2)
print(message)
"""
<id:10,values:[<0x01,37>,<0x03,2>,]>
"""

# Generate message to bind effect from slot 2 to actuators 0x03
message = libtup.tup_message_init_bind(2, 0x03)
print(message)
"""
<id:16,values:[<0x01,2>,<0x01,3>,]>
"""

# Create message to set some parameters of effect in slot 2
parameters = [
    libtup.Parameter(0, 25),
    libtup.Parameter(1, 65),
    libtup.Parameter(2, 1337)
]
message = libtup.tup_message_init_set_parameter(2, parameters)
print(message)
"""
<id:15,values:[<0x01,2>,<0x01,0>,<0x05,25>,<0x01,1>,<0x05,65>,<0x01,2>,<0x05,1337>,]>
"""

# Generate message to play effect from slot 2
message = libtup.tup_message_init_play(2)
print(message)
"""
<id:11,values:[<0x01,2>,]>
"""

# Generate message to set some input of effect in slot 2
inputs = [
    libtup.Input(0, 0x42),
    libtup.Input(1,0x1337),
    libtup.Input(2,314)
]
message = libtup.tup_message_init_set_input(2, inputs)
print(message)
"""
<id:22,values:[<0x01,2>,<0x01,0>,<0x06,66>,<0x01,1>,<0x06,4919>,<0x01,2>,<0x06,314>,]>
"""

# Generate message to stop effect from slot 2
message = libtup.tup_message_init_stop(2)
print(message)
"""
<id:12,values:[<0x01,2>,]>
"""
```
