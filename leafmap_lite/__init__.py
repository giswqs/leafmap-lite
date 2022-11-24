"""Top-level package for leafmap-lite."""

__author__ = """Qiusheng Wu"""
__email__ = 'giswqs@gmail.com'
__version__ = '0.0.4'

import asyncio


async def is_jupyterlite():
    """Check if the current environment is JupyterLite."""

    import sys
    import piplite

    if "pyodide" in sys.modules:

        await piplite.install('leafmap', deps=False)
        await piplite.install('shapely', deps=False)
        await piplite.install('pyproj', deps=False)
        await piplite.install('geopandas', deps=False)


asyncio.run(is_jupyterlite())

    
