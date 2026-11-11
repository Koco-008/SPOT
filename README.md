# SPOT

SPOT is a thermal imaging camera designed for inspecting electronic assemblies. It combines a Raspberry Pi 5, a FLIR Lepton 3.5, a Raspberry Pi Camera Module 3, and a 5-inch touchscreen.

## Build Your Own SPOT

| Section | Documentation |
| --- | --- |
| Components | [Bill of Materials](BOM.md) |
| Assembly and wiring | [Assembly instructions](hardware/assembly.md) |
| Enclosure and CAD models | [CAD files](hardware/cad/) |
| Connector PCB and manufacturing files | [PCB files](hardware/pcb/) |
| Photos and illustrations | [Hardware images](hardware/images/) |
| Software installation | [Installation guide](software/installation.md) |
| Operation | [User guide](software/usage.md) |
| Troubleshooting | [Troubleshooting](software/troubleshooting.md) |

## Software and Source Code

- [SPOT App – Releases](https://github.com/Koco-008/SPOT-Releases/releases)
- [SPOT OS – Releases](https://github.com/Koco-008/SPOT-OS-Releases/releases)
- [SPOT OS – Source Code](https://github.com/Koco-008/SPOT-OS)
- [Lepton-Pi5 – Driver](https://github.com/Koco-008/Lepton-Pi5)

The `scripts/` directory contains the existing platform checks and release verification tools. Public signing keys are available in `keys/`.

## Documentation Status

Hardware files, assembly instructions, the illustrated user manual and installation steps are available. For a new build, start with the [Raspberry Pi OS image specified in the installation guide](software/installation.md) and check the required kernel version.

## License

[MIT](LICENSE). Third-party hardware and software remain subject to their respective licenses.
