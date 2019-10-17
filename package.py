name = "katana"

version = "3.2.1"

authors = [
    "Foundry"
]

description = \
    """
    Katana is an asset-based approach to VFX look development and lighting for 3D computer generated scenes,
    providing scalability to your pipeline.
    """

requires = [
    "cmake-3+",
    "license_manager"
]

variants = [
    ["platform-linux"]
]

tools = [
    "katana"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "katana-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}")

    # We setup the license server.
    if "FOUNDRY_LICENSE_SERVER" in env.keys():
        env.foundry_LICENSE.set(str(env.FOUNDRY_LICENSE_SERVER))

    # Helper environment variables.
    env.KATANA_BINARY_PATH.set("{root}/bin")
    env.KATANA_INCLUDE_PATH.set("{root}/plugin_apis/include")
    env.KATANA_LIBRARY_PATH.set("{root}/bin")
