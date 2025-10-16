from odoo import http
from odoo.http import request

class HospitalWebsite(http.Controller):

    @http.route('/', type='http', auth="public", website=True)
    def hospital_homepage(self, **kw):
        banners = request.env['hospital.banner'].sudo().search([('active', '=', True)], order="sequence asc")
        return request.render('website_inherit.inherit_homepage', {
            'banners': banners
        })
