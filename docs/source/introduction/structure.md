# Structure

QOSST is separated in seven packages, in order to have more manageable projects.

## Presentation of the structure

The seven packages are listed in the table below:

| Name          | URL                                                                          | Documentation                                                              |
| ------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `qosst-core`  | [https://github.com/qosst/qosst-core](https://github.com/qosst/qosst-core)   | [https://qosst-core.readthedocs.io/](https://qosst-core.readthedocs.io/)   |
| `qosst-hal`   | [https://github.com/qosst/qosst-hal](https://github.com/qosst/qosst-hal)     | [https://qosst-hal.readthedocs.io/](https://qosst-hal.readthedocs.io/)     |
| `qosst-alice` | [https://github.com/qosst/qosst-alice](https://github.com/qosst/qosst-alice) | [https://qosst-alice.readthedocs.io/](https://qosst-alice.readthedocs.io/) |
| `qosst-bob`   | [https://github.com/qosst/qosst-bob](https://github.com/qosst/qosst-bob)     | [https://qosst-bob.readthedocs.io/](https://qosst-bob.readthedocs.io/)     |
| `qosst-skr`   | [https://github.com/qosst/qosst-skr](https://github.com/qosst/qosst-skr)     | [https://qosst-skr.readthedocs.io/](https://qosst-skr.readthedocs.io/)     |
| `qosst-sim`   | [https://github.com/qosst/qosst-sim](https://github.com/qosst/qosst-sim)     | [https://qosst-sim.readthedocs.io/](https://qosst-sim.readthedocs.io/)     |
| `qosst-pp`    | Not released                                                                 | Not released.                                                              |

The first six have been released as part of the QOSST software and the last one, that was judged to be not mature enough has not been released.

The relations between the different modules is represented in the figure below:

In the following we give a description of each packages.

## Released

In this section, we present the released modules of QOSST.

### qosst-core

`qosst-core` holds several functionalities that are common to both Alice and Bob, including filters, synchronisation sequence, modulation.

It also implements the network protocol that is used for classical communications, the authentication algorithms and the configuration object.

```{seealso}
The documentation of the qosst-core module can be consulted at the following link: 
```

### qosst-hal

`qosst-hal` holds all the interfaces for hardware connections. HAL stands for _Hardware Abstraction Layer_ and is composed of two main parts:

* The abstraction part, which is defining abstract classes for different hardware connections ({term}`ADC`, {term}`DAC`, laser, modulator control, powermeters, {term}`VOA`, optical switch) and fake classes (_i.e._ not interacting with actual hardware) to be used as default hardware;
* The `ext` part that provides specialized classes for a set of hardware material and the list of the implemented hardware interfaces can be found in the documentation of `qosst-hal`.

```{seealso}
The documentation of the qosst-hal module can be consulted at the following link: 
```


### qosst-alice

`qosst-alice` is the endpoint for usage for Alice. It uses both `qosst-hal` and `qosst-core` to provide:

* A Digital Signal Processing algorithm for the preparation of the signal;
* Hardware instructions to generate the signal in the physical domain;
* A server, using the network protocol in `qosst-core` to respond to Alice's requests.

It also provides some script for calibration.

```{seealso}
The documentation of the qosst-alice module can be consulted at the following link: 
```

### qosst-bob

`qosst-bob` is the endpoint for usage for Bob. It uses `qosst-hal`, `qosst-core` and `qosst-skr` to provide:

* Hardware instructions to acquire the signal received by Alice;
* A Digital Signal Processing algorithm for recovering the symbols sent by Alice;
* A client, using the network protocol in `qosst-core` to send requests to Alice;
* Functions to estimate the parameters for {term}`CV-QKD`;
* A Graphical User Interface to use the client;
* Optimization scripts to optimize the {term}`DSP` parameters.

It also provides some script for calibration.

```{seealso}
The documentation of the qosst-bob module can be consulted at the following link: 
```

### qosst-skr

`qosst-skr` provides functions to compute the Secret Key Rate of {term}`CV-QKD` depending on  the security assumption and the setup of the experiment. It used by `qosst-bob` but can also be used outside to compute the secret key rate.

```{seealso}
The documentation of the qosst-skr module can be consulted at the following link: 
```

### qosst-sim

`qosst-sim` (sim for simulation) should have held simulations to test the different part of the software without interacting with any hardware.

## Not released

When the `qosst` software was first planned, one additional module was planned but is currently not released due to its lack of maturity.

### qosst-pp

`qosst-pp` (pp for Post-Processing) should have held the functions for Error Correction and Privacy Amplification, which are essential steps for an actual {term}`CV-QKD` systems. However, research-wise, the key rate can be computed after the parameters estimation part.

