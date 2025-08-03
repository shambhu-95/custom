from odoo import http
from odoo.http import request

class WebsiteHomepageController(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def homepage(self, **kwargs):
        contact = request.env['res.partner'].sudo().search([], limit=10)
        print(contact)
        return request.render('website_inherit.custom_homepage_template', {
            'contact': contact
        })
