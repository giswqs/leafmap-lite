"""Top-level package for leafmap-lite."""

__author__ = """Qiusheng Wu"""
__email__ = 'giswqs@gmail.com'
__version__ = '0.1.0'

# import sys


# async def install_pkgs():
#     """Check if the current environment is JupyterLite."""

#     import piplite

#     await piplite.install('leafmap', deps=False)
#     await piplite.install('shapely', deps=False)
#     await piplite.install('pyproj', deps=False)
#     await piplite.install('geopandas', deps=False)

    
# if "pyodide" in sys.modules:
#     # pyodide doesn't support numpy, so we need to install it separately
#     # and then import it.
#     import pyodide
#     pyodide.runPython("import piplite; piplite.install('leafmap', deps=False)")
