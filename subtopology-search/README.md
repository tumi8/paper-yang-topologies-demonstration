# Subtopology Search

[search.py](search.py) searches the [large testbed](../topologies/subtopology-search-large-testbed.json) for the [Figure 1 setup](../topologies/figure-1-bidirectional-splitter.json). It first finds two matching sets of hosts. Requiring at least 100 Gbit/s on all four directed links leaves one set: `avax`, `pact`, and `stoi`.

[output.txt](output.txt) contains the printed results. Each option is a set of testbed hosts. Its columns show the possible assignments of Figure 1 nodes and ports to those hosts and interfaces.

We plan to release the `net_topology` Python library with the camera-ready version of the paper. After the release, install the library and run the following command from this folder to regenerate `output.txt`.

```sh
python search.py > output.txt
```
