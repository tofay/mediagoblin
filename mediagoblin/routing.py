# GNU MediaGoblin -- federated, autonomous media hosting
# Copyright (C) 2011, 2012 MediaGoblin contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging

from mediagoblin.tools.routing import add_route, mount, url_map
from mediagoblin.tools.pluginapi import PluginManager
from mediagoblin.admin.routing import admin_routes
from mediagoblin.auth.routing import auth_routes


_log = logging.getLogger(__name__)


def get_url_map():
    add_route('index', '/', 'mediagoblin.views:root_view')
    mount('/auth', auth_routes)
    mount('/a', admin_routes)

    import mediagoblin.submit.routing
    import mediagoblin.user_pages.routing
    import mediagoblin.edit.routing
    import mediagoblin.webfinger.routing
    import mediagoblin.listings.routing
    import mediagoblin.notifications.routing
    import mediagoblin.oauth.routing

    
    for route in PluginManager().get_routes():
        add_route(*route)

    return url_map
