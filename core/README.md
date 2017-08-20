# Core Module

## How to?
The only module which should be used by other applications/modules is the `supervisor.py`. 

### The basic appplication flow is this:

```
import supervisor.py

def loaded(supervisor): 
    pass # your code here e.g. supervisor.get_statistics()

supervisor.SuperVisor(loaded, force_training=False, max_files=-1) 
```
### Arguments
* **loaded:** callback after classifier has been loaded/trained
* **force_training:** True will force the classifier to be trained. If a saved classifier + statistics can be loaded the training is getting skipped if `force_training` is False. Training also starts if no saved classifier + statistics can be loaded.
* **max_files:** Maximal files for feature extraction. Can save time and memory but the classifier could be inaccurate.