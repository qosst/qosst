# Tutorial

This tutorial will get through exchanging the first {term}`CV-QKD` frame.

```{warning}
There is not guarantee that will work, or will give results. {term}`CV-QKD` is a challenging task with a lot of tweaking parameters, that also have a high dependence on the actual hardware.
```

## Hardware

You will need standardised interface with the hardware you are using. This should be done by creating interface classes that are compatible with the abstract hardware classes.

Please refer to the {external+qosst-hal:doc}`tutorial on the qosst-hal documentation <introduction/implementing_hardware>` for more details.

```{note}
Some example of interfaces might be published, but not in the QOSST project.
```

## Preparing Alice

The first step is to initialize the configuration on Alice's side. This can be done using the following command

```{prompt} bash
qosst configuration create
```

This will create a default configuration file named `config.toml`. The configuration is written in the [TOML](https://toml.io/en/) language, and the whole documentation fo the configuration file can be found in the `qosst-core` documentation.

This default configuration file is the same for Alice and for Bob, so the first thing to do, although not mandatory, is to delete all the sections that are Bob related.

Once this is done, here are the parameters from which you have to change the default values:

* In `alice.network` set the bind address to the address that will be used for the classical channel. If the network port is not convenient, you should also change it.
* In `alice.dac` set the rate of the {term}`DAC` , the hardware class to use, the channels to use and eventually some extra arguments. You should also change the amplitude that will be given to the {term}`DAC` to match the linearity contraints of the modulator.
* In `alice.powermeter`, set the hardware class and location for the monitoring photodiode.
* If needed, set the {term}`VOA` in `alice.voa`
* In `alice` set the photodiode_to_output_conversion to the multiplying factor that allows to get the power at the output of Alice knowing the power at the monitoring photodiode. A script is available to characterize this value and more information can be found {external+qosst-alice:doc}`understanding/characterisation_conversion_factor`.

Then you need to configure the {term}`CV-QKD` frame:

* In `frame.pilots` set the number and the frequency of the pilots. If you are not sharing the local oscillator, you will need two of them. You also have to set the amplitude of the pilots. This parameter has to be optimized. The value of the amplitude is relative to the [-1, +1] interval and will be multiplied by the amplitude of the {term}`DAC`.
* In `frame.quantum` set the number of symbols, the frequency shift, the symbol rate, the roll off and the modulation parameters (type, size, variance). The variance is again relative to the [-1, +1] interval and also need to be optimized.


````{warning}
When setting the frequency parameter you have to check that you have enough bandwidth and that there is no overlapping. In particular, if you denoted {math}`\beta` the roll-off, {math}`R_s` the symbol rate, {math}`f_s` the frequency of the signal and {math}`f_1, f_2` the frequency of the pilots, you have that the bandwidth of the signal is 

```{math}
B_s = (1+\beta)R_s
```

and the signal is then comprised in the frequency interval


```{math}
\left[f_s - \frac{B_s}{2}, f_s + \frac{B_s}{2}\right]
```

and you want 

```{math}
f_1, f_2 \notin \left[f_s - \frac{B_s}{2}, f_s + \frac{B_s}{2}\right]
```


````

```{note}
To check that the software is working, you can use a PSKModulation with size 4 and with a high variance and check that the {term}`DSP` of Bob recovers the 4 symbols.
```

## Preparing Bob

On Bob side you will also be required to generate the configuration file with the command

```{prompt} bash
qosst configuration create
```

Again you can delete all all sections related to Alice and then modify the following information

* In `bob` set the value of eta. There is a script to characterize this value in `qosst-bob` and more information can be found {external+qosst-bob:doc}`here <understanding/calibration>`;
* In `bob.network` set the address and port of the server, _i.e._ the same that were put in Alice configuration;
* In `bob.adc`, set the location;
* In `bob.dsp`, set the DAC rate and choose the other parameters for the {term}`DSP`;
* In `bob.switch`, set the location and set a non-zero value for the switching time to have automatic shot noise calibration (as discussed {external+qosst-bob:doc}`here <understanding/calibration>`);
* In `frame` the configuration should be exactly the same as the one on Alice's side[^frame-config-same]

[^frame-config-same]: This is partly true, since some parameters are not used on Bob side, like the amplitudes of the pilots. It however remains good practice to have the exact same parameters.

## Start server and client

### Server

Start Alice with the following command

```{prompt} bash
qosst-alice -f config.toml -vv
```

If your configuration file is located elsewhere, please update the parameter accordingly.

The documentation of the `qosst-alice` command tool can be found {external+qosst-alice:doc}`here <cli/documentation>`

If the configuration is good, you should see the server loading the configuration, opening the hardware, initializing the socket and the line "Waiting for a client to connect" should be in the logs.

```{note}
The `-vv` option is optional but this option will print logs up to info logs, which is very useful.
```

### Client

The next step is to start the client. The easiest way to do this is to the Graphical User Interface ({term}`GUI`) that is provided with `qosst-bob`. The {term}`GUI` can be started with the following command:

```{prompt} bash
qosst-bob-gui -vv
```

More information on the {term}`GUI` can be found {external+qosst-bob:doc}`here <understanding/gui>` and for the command line {external+qosst-bob:doc}`here <cli/documentation>`.

After this command, the following window should be visible

```{figure} ../_static/gui.png
---
align: center
---
Screenshot of the graphical user interface
```

The first step is to load the configuration using the panel on the top left. Once the configuration is selected either by using the "Browse" button or by typing the path in th text field, the configuration is loaded byt clicking on the "Load configuration" button.

Then the hardware can be initialized by clicking on the "Init hardware button".

Then we need to calibrate the electronic noise. This is discussed in more detail {external+qosst-bob:doc}`here <understanding/calibration>` but the simplest for this tutorial is to make sure the signal input is switch off and the local oscillator is off and to click on "Acquire electronic noise samples". The shot noise doesn't need to be calibrated in this tutorial since we chose an automatic shot noise calibration by setting a non-zero value in `bob.switch.switching_time`.

## Initialization

Once the previous step is done, Bob can connect to Alice with the "Connect" button and perform the identification (start of authentication, verification of versions and configuration) and initialization (start a new {term}`CV-QKD` frame) with the corresponding button.

## Make the exchange

To actually make the exchange, click on the "QIE" button. The code will do all the action including classical communication, switching, starting and stop the acquisition and the emission.

At this moment, if one of "Temporal", "Frequential" or "FFT" autoplot checkbox was checked, the plots will update in accordance with the autoplot choice. It is also possible to manually plot by using the "Plot" button in the corresponding tab.


```{figure} ../_static/gui_freq.png
---
align: center
---
Screenshot of the graphical user interface, after the exchange
```


## DSP and Parameters Estimation

Once the exchange is finished, it's possible to run the Digital Signal Processing algorithm by clicking on the DSP button. Depending on the choice of parameters and the system, this operation could take a while.

Once this is done, the figures will update themselves (again according to the autplot choice). You will be able to see the recovered tone and quantum symbols. In general the latter won't have any particular feature since the number of photons in the coherent states is very low.

You can then run the Parameters Estimation step by clicking on the Parameters Estimation button, and the values should update themselves soon after. It will possible to see the estimated excess noise and transmittance, along with the key rate and other parameters.

At this point, you end up with an estimation of the key rate, which is as far as the QOSST software currently goes since there is no reconciliation or privacy amplification.