# -*- coding: utf-8 -*-
"""
/***************************************************************************
 YKRTool
                                 A QGIS plugin
 Tampereen tulevaisuuden yhdyskuntarakenteen ilmastovaikutusten arviointityökalu
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-05-05
        copyright            : (C) 2019 by Gispo Ltd.
        email                : mikael@gispo.fi
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load YKRTool class from file YKRTool.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sources.ykr_tool import YKRTool
    return YKRTool(iface)
