from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "mermer_harvester mermer_timelord_launcher mermer_timelord mermer_farmer mermer_full_node mermer_wallet".split(),
    "node": "mermer_full_node".split(),
    "harvester": "mermer_harvester".split(),
    "farmer": "mermer_harvester mermer_farmer mermer_full_node mermer_wallet".split(),
    "farmer-no-wallet": "mermer_harvester mermer_farmer mermer_full_node".split(),
    "farmer-only": "mermer_farmer".split(),
    "timelord": "mermer_timelord_launcher mermer_timelord mermer_full_node".split(),
    "timelord-only": "mermer_timelord".split(),
    "timelord-launcher-only": "mermer_timelord_launcher".split(),
    "wallet": "mermer_wallet mermer_full_node".split(),
    "wallet-only": "mermer_wallet".split(),
    "introducer": "mermer_introducer".split(),
    "simulator": "mermer_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
