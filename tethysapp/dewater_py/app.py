from tethys_sdk.base import TethysAppBase, url_map_maker


class DewaterPy(TethysAppBase):
    """
    Tethys app class for dewater py.
    """

    name = 'dewater py'
    index = 'dewater_py:tool'
    icon = 'dewater_py/images/icon.gif'
    package = 'dewater_py'
    root_url = 'dewater-py'
    color = '#1abc9c'
    description = 'Using python script only, create a dewatered zone using wells with a fixed, combined pumping rate (for excavation scenarios).'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='tool',
                           url='dewater-py/tool',
                           controller='dewater_py.controllers.tool'),
                    UrlMap(name='license',
                           url='dewater_py/license',
                           controller='dewater_py.controllers.license'),
                    UrlMap(name='user',
                           url='dewater_py/user',
                           controller='dewater_py.controllers.user'),
                    UrlMap(name='tech',
                           url='dewater_py/tech',
                           controller='dewater_py.controllers.tech'),
                    UrlMap(name='verify',
                           url='dewater_py/verify',
                           controller='dewater_py.controllers.verify'),
                    UrlMap(name='get_generate_water_table_ajax',
                           url='dewater-py/tool/generate-water-table',
                           controller='dewater_py.controllers.generate_water_table'),
        )

        return url_maps
