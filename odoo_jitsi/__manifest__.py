{
    'name': "Odoo Jitsi Integration",
    'summary': "Embed Jitsi Meet video calls inside Odoo",
    'description': "Start and join Jitsi video calls from Odoo backend.",
    'author': "Your Name",
    'category': 'Tools',
    'version': '16.0.1.0.0',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/meeting_views.xml',
        'views/jitsi_website_templates.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_jitsi/static/src/js/jitsi_widget.js',
        ],
    },
    'installable': True,
    'application': True,
}
