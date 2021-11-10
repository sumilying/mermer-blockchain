from setuptools import setup

dependencies = [
    "multidict==5.1.0",  # Avoid 5.2.0 due to Avast
    "blspy==1.0.6",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.6",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.15",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the mermer processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
    "watchdog==2.1.6",  # Filesystem event watching - watches keyring.yaml
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-setuptools",
]

kwargs = dict(
    name="mermer-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@mermer.net",
    description="Mermer blockchain full node, farmer, timelord, and wallet.",
    url="https://mermer.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="mermer blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "mermer",
        "mermer.cmds",
        "mermer.clvm",
        "mermer.consensus",
        "mermer.daemon",
        "mermer.full_node",
        "mermer.timelord",
        "mermer.farmer",
        "mermer.harvester",
        "mermer.introducer",
        "mermer.plotters",
        "mermer.plotting",
        "mermer.pools",
        "mermer.protocols",
        "mermer.rpc",
        "mermer.server",
        "mermer.simulator",
        "mermer.types.blockchain_format",
        "mermer.types",
        "mermer.util",
        "mermer.wallet",
        "mermer.wallet.puzzles",
        "mermer.wallet.rl_wallet",
        "mermer.wallet.cc_wallet",
        "mermer.wallet.did_wallet",
        "mermer.wallet.settings",
        "mermer.wallet.trading",
        "mermer.wallet.util",
        "mermer.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "mermer = mermer.cmds.mermer:main",
            "mermer_wallet = mermer.server.start_wallet:main",
            "mermer_full_node = mermer.server.start_full_node:main",
            "mermer_harvester = mermer.server.start_harvester:main",
            "mermer_farmer = mermer.server.start_farmer:main",
            "mermer_introducer = mermer.server.start_introducer:main",
            "mermer_timelord = mermer.server.start_timelord:main",
            "mermer_timelord_launcher = mermer.timelord.timelord_launcher:main",
            "mermer_full_node_simulator = mermer.simulator.start_simulator:main",
        ]
    },
    package_data={
        "mermer": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "mermer.util": ["initial-*.yaml", "english.txt"],
        "mermer.ssl": ["mermer_ca.crt", "mermer_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)  # type: ignore
