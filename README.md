# QOSST - Quantum Open Software for Secure Transmissions

<center>

![QOSST Logo](qosst_logo_full.png)

<a href='https://qosst.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/qosst/badge/?version=latest' alt='Documentation Status' />
</a>
<a href="https://github.com/qosst/qosst-core/blob/main/LICENSE"><img alt="Github - License" src="https://img.shields.io/github/license/qosst/qosst-core"/></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/pylint-dev/pylint"><img alt="Linting with pylint" src="https://img.shields.io/badge/linting-pylint-yellowgreen"/></a>
<a href="https://mypy-lang.org/"><img alt="Checked with mypy" src="https://www.mypy-lang.org/static/mypy_badge.svg"></a>
<a href="https://img.shields.io/pypi/pyversions/qosst-core">
    <img alt="Python Version" src="https://img.shields.io/pypi/pyversions/qosst-core">
</a>
</center>
<hr/>
This repo serves two purposes: the first is to explain how the code quality of QOSST and the second one is to give a general introduction to QOSST.

QOSST was initially developed in the [Quantum Information (QI) team](https://qi.lip6.fr) of the [LIP6 laboratory](https://lip6.fr) in Sorbonne Université.

## Article

The article associated to this publication can be found on the arXiv: [arXiv:2404.18637](https://arxiv.org/abs/2404.18637).

Here is the bibtex to cite this paper:

```
@misc{pietri2024qosst,
      title={QOSST: A Highly-Modular Open Source Platform for Experimental Continuous-Variable Quantum Key Distribution}, 
      author={Yoann Piétri and Matteo Schiavon and Valentina Marulanda Acosta and Baptiste Gouraud and Luis Trigo Vidarte and Philippe Grangier and Amine Rhouni and Eleni Diamanti},
      year={2024},
      eprint={2404.18637},
      archivePrefix={arXiv},
      primaryClass={id='quant-ph' full_name='Quantum Physics' is_active=True alt_name=None in_archive='quant-ph' is_general=False description=None}
}
```

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
