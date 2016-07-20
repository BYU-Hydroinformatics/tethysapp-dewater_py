from tethys_sdk.base import TethysAppBase, url_map_maker


class DewaterPy(TethysAppBase):
    """
    Tethys app class for dewater py.
    """

    name = 'Construction Dewatering Simulator'
    index = 'dewater_py:home'
    icon = 'dewater_py/images/icon.gif'
    package = 'dewater_py'
    root_url = 'dewater-py'
    color = '#1abc9c'
    description = 'Simple tool for simulating the water table drawdown due to a system of wells surrounding an excavation.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='dewater-py',
                           controller='dewater_py.controllers.home'),
                    UrlMap(name='get_generate_water_table_ajax',
                           url='dewater-py/generate-water-table',
                           controller='dewater_py.controllers.generate_water_table'),
        )

        return url_maps