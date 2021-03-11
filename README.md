SMPTE ST 2042-1 (VC-2) Constants and Data Tables
================================================

This Python package, `vc2_data_tables`, contains machine-readable versions of
the constants and data tables in the SMPTE ST 2042-series of standards relating
to the [VC-2 professional video codec](https://www.bbc.co.uk/rd/projects/vc-2).

To get started, read the [`vc2_data_tables`
manual](https://bbc.github.io/vc2_data_tables/) (also available in [PDF
format](https://bbc.github.io/vc2_data_tables/vc2_data_tables_manual.pdf)).


See also
--------

This package was produced to support the [VC-2 conformance
software](https://github.com/bbc/vc2_conformance), though it has been made
available under the hope that it may be useful to others.

The quantisation matrices in this module reproduce the default quantisation
matrices set out in the VC-2 specification (including the erroneous values for
the Fidelity filter). For tools and guidance on producing your own quantisation
matrices see [the `vc2_quantisation_matrices`
package](https://github.com/bbc/vc2_quantisation_matrices/).

For further information, please conatact [Jonathan
Heathcote](mailto:jonathan.heathcote@bbc.co.uk) or [John
Fletcher](mailto:john.fletcher@bbc.co.uk).


Developers
----------

For details on setting up a developer's installation of this software,
including instructions on building the associated documentation, see the
[developer installation instructions for the main `vc2_conformance`
repository](https://github.com/bbc/vc2_conformance).


License
-------

This software is distributed under the [GNU General Public License version
3](./LICENSE.txt), &copy; BBC 2021.
