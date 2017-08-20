# Core Module

## How to?
The only module which should be used by other applications/modules is the `supervisor.py`. 

The basic appplication flow is this:

```
import supervisor.py

def loaded(supervisor): 
    pass # your code here e.g. supervisor.get_statistics()

supervisor.SuperVisor(loaded, force_training=False) # True will force training
```