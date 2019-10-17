CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the Katana version string in multiple ones.
string(REPLACE "." ";" KATANA_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET KATANA_VERSION_LIST 0 KATANA_MAJOR_VERSION)
list(GET KATANA_VERSION_LIST 1 KATANA_MINOR_VERSION)
list(GET KATANA_VERSION_LIST 2 KATANA_PATCH_VERSION)

set(KATANA_PRODUCT_VERSION ${KATANA_MAJOR_VERSION}.${KATANA_MINOR_VERSION}v${KATANA_PATCH_VERSION})

# Katana
rez_set_archive(
    KATANA_URL katana/Katana${KATANA_PRODUCT_VERSION}-linux-x86-release-64.tgz
    https://www.foundry.com/products/download_product?file=Katana${KATANA_PRODUCT_VERSION}-linux-x86-release-64.tgz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/katana/${REZ_BUILD_PROJECT_VERSION})

# We configure/build/install Katana through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_KATANA
    URL ${KATANA_URL}
    PREFIX katana
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${EXTRACT_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] Katana-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
