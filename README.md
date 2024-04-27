# QOSST - Quantum Open Software for Secure Transmissions

<center>

![QOSST Logo](qosst_logo_full.png)

</center>

This repo serves two purposes: the first is to explain how the code quality of QOSST and the second one is to give a general introduction to QOSST.

QOSST was initially developed in the [Quantum Information (QI) team](https://qi.lip6.fr) of the [LIP6 laboratory](https://lip6.fr) in Sorbonne Université.

## Article

The link to the article will be added soon.

## Structure

The QOSST software is separated in 7 submodules:

* `qosst-core` for the configuration, control protocol, and common functions to Alice and Bob;
* `qosst-alice` for the digital signal processing (DSP), server, and interaction with the hardware for Alice;
* `qosst-bob` for the digital signal processing (DSP), client, interaction with the hardware, parameters estimation for Bob.;
* `qosst-hal` for hardware abstraction layer;
* `qosst-skr` for the secret key rate computations;
* `qosst-sim` for the simulations;
* `qosst-pp` for the post processing.

To operate Alice, it is only necessary to install the `qosst-alice` package. The other packages that are required will be automatically installed. The same applies for `qosst-bob`.

## Links and documentation

| Name          | URL                                                                          | Documentation                                                              |
| ------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `qosst-core`  | [https://github.com/qosst/qosst-core](https://github.com/qosst/qosst-core)   | [https://qosst-core.readthedocs.io/](https://qosst-core.readthedocs.io/)   |
| `qosst-hal`   | [https://github.com/qosst/qosst-hal](https://github.com/qosst/qosst-hal)     | [https://qosst-hal.readthedocs.io/](https://qosst-hal.readthedocs.io/)     |
| `qosst-alice` | [https://github.com/qosst/qosst-alice](https://github.com/qosst/qosst-alice) | [https://qosst-alice.readthedocs.io/](https://qosst-alice.readthedocs.io/) |
| `qosst-bob`   | [https://github.com/qosst/qosst-bob](https://github.com/qosst/qosst-bob)     | [https://qosst-bob.readthedocs.io/](https://qosst-bob.readthedocs.io/)     |
| `qosst-skr`   | [https://github.com/qosst/qosst-skr](https://github.com/qosst/qosst-skr)     | [https://qosst-skr.readthedocs.io/](https://qosst-skr.readthedocs.io/)     |
| `qosst-sim`   | [https://github.com/qosst/qosst-sim](https://github.com/qosst/qosst-sim)     | [https://qosst-sim.readthedocs.io/](https://qosst-sim.readthedocs.io/)     |
| `qosst-pp`    | Not released                                                                 | Not released.                                                              |

## Code quality

The code quality of the QOSST submodules are checked via three tools:

* [pylint](https://pypi.org/project/pylint/) for the static linting;
* [mypy](https://mypy-lang.org/) for the type hints checking;
* [docstr-coverage](https://pypi.org/project/docstr-coverage/) for checking the coverage of documentation.

The script `code_quality.py` automatically applies all the checks to all the submodules.

Additionally, the QOSST submodules are formatted with [black](https://github.com/psf/black).

## License

The submodules of QOSST are shipped under the [Gnu General Public License v3](https://www.gnu.org/licenses/gpl-3.0.html).

## Contributing

### Report issues

Reporting issues is the first way to contribute to the software.

You can report global issue with the software on the issues tracker of QOSST at [https://github.com/qosst/qosst/issues](https://github.com/qosst/qosst/issues).

It is however preferable to use the specialized repo for issues that are specific to a module:

| Module        | URL of the issues tracker                                                                  |
| ------------- | ------------------------------------------------------------------------------------------ |
| `qosst-core`  | [https://github.com/qosst/qosst-core/issues](https://github.com/qosst/qosst-core/issues)   |
| `qosst-hal`   | [https://github.com/qosst/qosst-hal/issues](https://github.com/qosst/qosst-hal/issues)     |
| `qosst-alice` | [https://github.com/qosst/qosst-alice/issues](https://github.com/qosst/qosst-alice/issues) |
| `qosst-bob`   | [https://github.com/qosst/qosst-bob/issues](https://github.com/qosst/qosst-bob/issues)     |
| `qosst-skr`   | [https://github.com/qosst/qosst-skr/issues](https://github.com/qosst/qosst-skr/issues)     |
| `qosst-sim`   | [https://github.com/qosst/qosst-sim/issues](https://github.com/qosst/qosst-sim/issues)     |

Please include the following information when reporting a bug

* description of the bug;
* versions of the QOSST software;
* configuration file;
* used hardware, if relevant;
* logs of the error.

When requesting new feature, please provide a detailed description of what you propose and any reference that could be relevant.

### Proposing code

You can propose code, either to solve issues or to propose new features directly.

If you want to solve an issue please comment on the issue on the issue tracker so we can assign the assign to you.

Here are the steps you should do:

1. Fork the repository on your github account;
2. Clone your forked repository;
3. Make the changes and commit;
4. Push to your forked repository;
5. Open a Pull Request on the associated repository.

We will then check the changes and merge when it's ready.

## Acknowledgments

We first thank the direct contributors of the code:
* Yoann Piétri
* Valentina Marulanda Acosta
* Matteo Schiavon
* Mayeul Chavanne
* Ilektra Karakosta - Amarantidou

We also thank all the persons that made comments and discussions that had a direct impact on this software:
* Luis-Trigo Vidarte
* Baptiste Gouraud
* Amine Rhouni
* Eleni Diamanti
* Philippe Grangier

And finally we thank the persons that participated in some ways to the development of QOSST:
* Thomas Liege
* George Crisan
* Damien Fruleux
* Sarah Layani
* Manon Huguenot
