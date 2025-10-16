{
    'name': 'My Custom Website',
    'version': '1.0',

    'depends': ['base', 'website', 'hr','web',],

    'data': [
        'security/ir.model.access.csv',
        # 'views/homepage_inherit.xml',
        'views/website_home_inherit.xml',
        # 'views/website_banner_views.xml',
        # 'views/website_home_inherit_slider.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'website_inherit/static/src/css/banner.css',
            # 'website_inherit/static/src/css/custom.css',
            # 'website_inherit/static/src/js/custom.js',

        ],
    },
    'installable': True,
    'auto_install': False,
}
