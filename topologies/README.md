# Topology Files

These JSON files describe the paper’s network setups as YANG instance data.

| File | Role in the paper |
| --- | --- |
| [figure-1-bidirectional-splitter.json](figure-1-bidirectional-splitter.json) | In Figure 1, sniffer interface `ethC` captures traffic from `nodeA` to `nodeB`, and `ethD` captures the reverse direction. This topology is the query for the [search demo](../subtopology-search/README.md). |
| [figure-2-bidirectional-splitter-with-two-forward-taps.json](figure-2-bidirectional-splitter-with-two-forward-taps.json) | Figure 2 adds a second forward splitter. The `splitter-order` values show that traffic from `nodeA` to `nodeB` passes through `fwd0` first (0), then `fwd1` (1). |
| [table-4a-reproduction.json](table-4a-reproduction.json) | Client, server, and sniffer used to reproduce the TLS measurements in Table 4a. |
| [subtopology-search-large-testbed.json](subtopology-search-large-testbed.json) | Full research testbed used by the search demo, with 43 nodes, 234 directed links, and 12 optical splitter entries. |
