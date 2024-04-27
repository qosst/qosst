# Goals and design

## Goals

The main goal of QOSST is to provide all the necessary functions to build a {term}`CV-QKD` system, while being agnostic to the hardware and not limiting to one specific use case.

## Design rules

Several design rules were established when coding this project, and are described below:

* A configuration file can be used to simply modify the parameters of the system;
* Functions are specialized and only top-level functions take the whole configuration object as a parameter, enabling functions to be used outside of specific cases;
* Alice and Bob software are partly independent, and a specific requirement of one of them should not be a requirement of the other;
* The software is agnostic of the hardware;
* The code uses [black](https://pypi.org/project/black/), [pylint](https://pypi.org/project/pylint/) and [poetry](https://python-poetry.org/).

## Protocol

While trying to be general, we still had to choice to design the Digital Signal Processing. In this example we detail the protocol and we present the choices for the {term}`DSP`.