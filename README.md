# PySpectralRadar
Python 3 wrapper for Thorlabs SpectralRadar SDK C library using ctypes

This wrapper is intended for use with ThorLabs ThorImage and SpectralRadar
version 4.4.7.0.

It should work with most other 4.X versions with little
to no modification.

Dependencies: numpy, ctypes

NOT ALL FUNCTIONS FROM THE SPECTRALRADAR API ARE INCLUDED. Functions are
added as they become useful to the project this is being developed for.
Structs, functions, and enums can be easily added as Python classes or functions
following the format of those already implemented.

Where possible, wrapper objects and arguments share the name of the
prototype they wrap, as declared in the .h or found in the ThorLabs docs.

---------------------------------------------------------------------------

ThorImage and SpectralRadar SDK software are the intellectual property of
Thorlabs, Inc. This script is merely a wrapper for the functions and objects
exposed by the SDK they provide to licensed users of this software.
