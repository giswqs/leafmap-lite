"""Top-level package for leafmap-lite."""

__author__ = """Qiusheng Wu"""
__email__ = 'giswqs@gmail.com'
__version__ = '0.0.6'

import sys


async def install_pkgs():
    """Check if the current environment is JupyterLite."""

    import piplite

    await piplite.install('leafmap', deps=False)
    await piplite.install('shapely', deps=False)
    await piplite.install('pyproj', deps=False)
    await piplite.install('geopandas', deps=False)


if "pyodide" in sys.modules:
    install_pkgs()

    
