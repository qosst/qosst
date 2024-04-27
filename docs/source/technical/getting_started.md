# Getting started

## Hardware requirements

### Operating System

The QOSST suite does not required a particular software and should work on Windows (tested), Linux (tested) and Mac (not tested).

The actual operating system requirement will come down to the hardware used for the experiment since some of them don't have interfaces with Windows.

### RAM requirements

QOSST software is not particularly improved for RAM consumptions and while `qosst-alice` will not create any issue, the Digital Signal Processing on Bob side will be way more demanding. The software was tested on our side on a system with 64 GB of RAM, without any issue. We believe that this value can be decreased since the {term}`DSP` was also able to run on a laptop with 20 GB of RAM (with no hardware). We however advise to go no less than 20 GB of RAM and we advise to go higher to take into account the required RAM for hardware (in particular the {term}`ADC`).

### Python version

QOSST if officially supporting any python version 3.9 or above.

## Installing the software

There are several ways of installing the software, either by using the PyPi repositories or using the source.

### Installing the whole suite at once

It is possible to install all the packages of QOSST (`qosst-core`, `qosst-hal`, `qosst-alice`, `qosst-bob` and `qosst-skr`) with the command

```{prompt} bash

pip install qosst
```

```{warning}

This method of installation is not recommended, since it is usually not useful to have `qosst-alice` and `qosst-bob` on the same system. For tests, or system with a single computer controlling both parties, we still recommend to install separately `qosst-alice` and `qosst-bob`.
```

### Installing the required software for Alice

To install the required software for Alice you can simply run the command

```{prompt} bash

pip install qosst-alice
```

This will automatically install `qosst-core`, `qosst-hal` and `qosst-alice` (along with other required dependencies).

Alternatively, you can clone the repository at [https://github.com/qosst/qosst-alice](https://github.com/qosst/qosst-alice) and install it by source.

### Installing the required software for Bob

To install the required software for Bob you can simply run the command

```{prompt} bash

pip install qosst-bob
```

This will automatically install `qosst-core`, `qosst-hal`, `qosst-skr` and `qosst-bob` (along with other required dependencies).

Alternatively, you can clone the repository at [https://github.com/qosst/qosst-bob](https://github.com/qosst/qosst-bob) and install it by source.

## Checking the version of the software

In whatever chosen method `qosst-core` should be installed in your systems. This packages provide the `qosst` command from which the whole documentation can be found on the `qosst-core` documentation (link of documentation).

You can check the version by issuing the command

```{command-output} qosst info
```

If the `qosst` command was not installed in the path, it also possible to run the following command:

```{prompt} bash
python3 -m qosst_core.commands info
```

or

```{prompt} bash
python3 -c "from qosst_core.infos import get_script_infos; print(get_script_infos())"
```

In the following we will assume that you have access to the qosst (and other) commands. If not you can replace the instructions similarly to above.

If this works and have the newest versions, you should be ready to go !
