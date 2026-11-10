# Demonstration of “YANG-Based Modeling and Emulation of Experimental Network Topologies”

This artifact accompanies the paper *YANG-Based Modeling and Emulation of Experimental Network Topologies* by Eric Hauser, Johannes Späth, Kento Grüner, and Georg Carle. The artifact consists of three parts.

## Topology Files

The [YANG topology instances](topologies/README.md) describe Figures 1 and 2, the research testbed, and the PQ-TLS measurement setup used to reproduce Table 4a.

## Subtopology Search

The [search example](subtopology-search/README.md) shows how to find the Figure 1 setup in the testbed, first at any link speed and then with a 100 Gbit/s minimum. The folder includes the Python script and its output.

## Measurement Reproduction

To demonstrate the emulation backend of `net_topology`, we recreated the [post-quantum TLS measurement setup](topologies/table-4a-reproduction.json) of Sosnowski et al. in Containernet. For each key agreement and network scenario, we compared our median handshake latency with the value reported in Table 4a (“KAs combined with rsa:2048 as SA”) of their paper, *The Performance of Post-Quantum TLS 1.3*.

The explorable artifact is available at <https://tumi8.github.io/paper-yang-topologies-demonstration/reproduction>. It shows the scripts in execution order, the measurement results, and the hardware used for the experiment. The raw data is available in [docs/reproduction/2026-11-08_16-11-41_109142/](docs/reproduction/2026-11-08_16-11-41_109142/) and archived on [Zenodo](https://doi.org/10.5281/zenodo.24062011).

## Disclaimer

The artifact documentation and parts of the subtopology search script (`search.py`) were written with the help of AI coding tools.
