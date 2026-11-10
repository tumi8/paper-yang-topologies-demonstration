"""Run with net_topology installed: python search.py > output.txt."""

from pathlib import Path

from net_topology import Topology


TOPOLOGIES = Path(__file__).resolve().parents[1] / "topologies"


def pretty_print_matches(testbed, query, title):
    matches = Topology.find_mapping(testbed, query)
    print(f"\n{title}: matching setups (distinct node sets) = {len(matches)}")
    # Each option is a set of testbed hosts. Each column is one way to assign
    # those hosts and their ports to the roles in Figure 1.
    for option_idx, r in enumerate(matches, start=1):
        rows = [
            ("",
             [f"#{i}" for i in range(1, len(r["variations"]) + 1)]),
        ]
        for n in r["nodes"]:
            rows.append((n, [p[n] for p in r["variations"]]))
            interfaces = [i for i in r["interfaces"] if f"{n}:" in i]
            for idx, x in enumerate(interfaces):
                interface_name = x.split(":")[1]
                pre = "├" if idx < len(interfaces) - 1 else "└"
                # A dot means this variation leaves the testbed port unused.
                interface_positions = [
                    p[x].split(":")[1] if x in p else "·"
                    for p in r["variations"]
                ]
                rows.append((f"{pre} {interface_name}", interface_positions))

        label_width = max(len(label) for label, _ in rows)
        pos_width = max(
            (len(p) for _, positions in rows for p in positions),
            default=0)
        total_width = label_width + 2 + (pos_width + 1) * len(rows[0][1])

        if option_idx > 1:
            print()
        print(f"Option {option_idx}")
        print("─" * total_width)
        for label, positions in rows:
            cols = " ".join(p.ljust(pos_width) for p in positions)
            print(f"{label.ljust(label_width)}  {cols}")


def main():
    testbed = Topology()
    testbed.load_topology_file(TOPOLOGIES / "subtopology-search-large-testbed.json")
    network_id, = testbed.networks()
    network = testbed.net.networks.network[network_id]
    print(f"{network_id}: {len(network.node)} nodes, {len(network.link)} directed links, "
          f"{len(network.optical_splitter)} optical splitter entries")
    print("Each option is one set of testbed hosts. Each numbered column shows one way")
    print("to assign those hosts and ports to Figure 1. A dot marks an unused port.")

    query = Topology()
    query.load_topology_file(TOPOLOGIES / "figure-1-bidirectional-splitter.json")
    pretty_print_matches(testbed, query, "Figure 1, no minimum speed")

    # The matcher treats each query link's speed as a minimum. Apply 100 Gbit/s
    # to both directions and both capture links, then repeat the search.
    query_id, = query.networks()
    for link_id in query.net.networks.network[query_id].link:
        query.update_link(query_id, link_id, speed=100_000_000_000)
    pretty_print_matches(testbed, query, "Figure 1, at least 100 Gbit/s on every link")


if __name__ == "__main__":
    main()
