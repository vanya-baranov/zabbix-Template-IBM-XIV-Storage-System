# zabbix-Template IBM XIV Storage System
Template IBM XIV Storage System works through external script checks

In the json unloading example.txt file, you can view sample script output and make your data items

## Step 1

You must install munch to run this script.

```bash
pip3 install munch
```

## Step 2

Optional, your must install pyxcli

https://github.com/IBM/pyxcli

It must be added to -

/usr/lib/python3/dist-packages/

# Patch pyxcli for python 3.11

patch in file  transport.py  on
 ```  timeout=60.0 ```

patch in file client.py

 ```
  def _populate_commands(self):
        #for info in self.execute("ups_list"):
        #    invoker = getattr(self.cmd, info.name)
        #    invoker.__doc__ = info.description + "\nUsage: " + info.syntax
        #    invoker.syntax = info.syntax
        #    setattr(self.cmd, info.name, invoker)
        pass
 ```

## Step 3

Import template




