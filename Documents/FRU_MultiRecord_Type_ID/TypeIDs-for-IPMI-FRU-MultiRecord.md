# Scope

This document contains the allocated Type ID in the IPMI FRU MultiRecord.

The Manufacturer ID shall be set to 0x00A76F.  The Manufacturer ID is the first 3 bytes of MultiRecord OEM payload definition.

| **Type ID**    | **OCP Specification** |
| :---           | :-----------          |
| [0xC0](#C0)    | [OCP NIC 3.0 v1.0](https://www.opencompute.org/wiki/Server/NIC) |
| [0xC1](#C1)    | [DC-SCM 2.0 for HPM FRU](https://www.opencompute.org/w/index.php?title=Server/MHS) |
| [0xC2](#C2)    | [MHS CRPS v1.05](https://www.opencompute.org/w/index.php?title=Server/MHS/DC-MHS-Specs-and-Designs) |
| [0xD0](#D0-D3) | [MHS CRPS v1.05](https://www.opencompute.org/w/index.php?title=Server/MHS/DC-MHS-Specs-and-Designs) |
| [0xD1](#D0-D3) | [MHS CRPS v1.05](https://www.opencompute.org/w/index.php?title=Server/MHS/DC-MHS-Specs-and-Designs) |
| [0xD2](#D0-D3) | [MHS CRPS v1.05](https://www.opencompute.org/w/index.php?title=Server/MHS/DC-MHS-Specs-and-Designs) |
| [0xD2](#D0-D3) | [MHS CRPS v1.05](https://www.opencompute.org/w/index.php?title=Server/MHS/DC-MHS-Specs-and-Designs) |



# C0

The OCP NIC specification defines a FRU as a way of detecting OCP NIC compliant card and it's configuration. 

# C1

The DC-SCM Specification defines HPM FRU entry as way to detect the HPM compliance with the DC-SCM Module during FRU-based Discovery Flow defined by the specification.

# C2

Identification of the CRPS capabities and version compliance. 

# D0-D3

OCP NIC 3.0 v1.5 adds support for DSFF Form Factor, FlexIO and PCIe Link Subdivision configuration options that need to be defined in separate FRU MultiRecord Entries.
