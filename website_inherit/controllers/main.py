# controllers/main.py
from odoo import http
from odoo.http import request

class PublicHomepage(http.Controller):
    @http.route('/', auth='public', website=True)
    def homepage(self, **kw):
        employees = request.env['hr.employee'].sudo().search([], limit=10)
        data = [{
            'name': emp.name,
            'image_url': f'/web/image/hr.employee/{emp.id}/image_1920'
        } for emp in employees]
        return request.render('website_inherit.custom_homepage', {'contacts': data})
