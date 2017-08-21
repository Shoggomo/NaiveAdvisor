# IsysNaive

A Naive-Bayes-Classifier trained with subreviews from TripAdvisor to calculate a overall rating based on given subratings.

## Install

Before using the Application dependencies have to be installed.
These can be installed with the following command over pip.

```
$ pip install -r requirements.txt
```

## Usage

The Server can be started running the `__init__.py` file.

```
$ python __init__.py
```

The web interface can be accessed over the ``index.html`` file in the ``web_interface`` folder.

## Credits

The training data can be pulled from ``http://times.cs.uiuc.edu/~wang296/Data/``, have to be in json format and need to be in a ``json`` directory in the project root.
To force training ``supervisor.SuperVisor(supervisor_ready)`` in ``__init__.py`` has to be changed to ``supervisor.SuperVisor(supervisor_ready, force_training=True)``.

## License

[MIT License](LICENSE)
