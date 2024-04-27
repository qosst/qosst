# Quantum Key Distribution

Quantum Key Distribution {term}`QKD` is one of the most prominent task of Quantum Cryptography, where two users, usually referred to as Alice and Bob, sharing a public quantum channel and a public but authenticated classical channel, exchange a cryptographic key (a string of random bits, that must remain secret) with a security based on the laws of Quantum Physics, that outrun any computational-security based key exchange.

```{todo}

Plop
```

The following assumptions are usually made in {term}`QKD` protocols[^1]

1. Alice and Bob are trusted users;
2. Alice and Bob share a quantum channel, that can be subject to eavesdropping (passive and active);
3. Alice and Bob share an authenticated classical channel, that can be subject to passive eavesdropping;
4. Alice and Bob have a trusted random number generator;
5. Alice and Bob are in secure physical locations
6. Alice has a trusted source, Bob has a trusted measurement device;
7. Alice and Bob have trusted classical devices.

Usually {term}`QKD` protocols are based on conjugate bases and the Heisenberg uncertainty relation by exploiting the fact that any interaction with the quantum states by the eavesdropper can be detected by Alice and Bob by sharing a part of their choices and measurements results, giving abound on the amount of information gained by an eavesdropper that can later be used to extract the secret key.

{term}`QKD` protocols can be separated into two families:

* {term}`DV-QKD` where the information is encoded on discrete degrees of freedom such as the polarisation of single photons;
* {term}`CV-QKD` where the information is encoded on continuous degrees of freedom such as the quadratures of the electromagnetic space.

The first {term}`QKD` protocol that was ever proposed, in 1984 by Bennett and Brassard {cite:p}`Bennett1984`, and was a {term}`DV-QKD` protocol, in particular exploiting the polarisation of single photons. It is far beyond the scope of this introduction to fully explain {term}`DV-QKD` protocols but the interested reader can find good resources in {cite:p}`AdvancesInQuaPirand2020`.

In the next section we will discuss {term}`CV-QKD` in more details, present the protocol and discuss its implementation.

[^1]: Some protocols actually try to remove some assumptions to get stronger {term}`QKD` protocols.
