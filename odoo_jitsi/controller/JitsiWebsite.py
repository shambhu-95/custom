from odoo import http
from odoo.http import request

class JitsiWebsite(http.Controller):

    @http.route('/jitsi/meeting/<int:meeting_id>', type='http', auth='public', website=True)
    def jitsi_meeting_page(self, meeting_id, **kwargs):
        meeting = request.env['jitsi.meeting'].sudo().browse(meeting_id)
        if not meeting.exists():
            return request.not_found()
        return request.render('odoo_jitsi.jitsi_meeting_template', {
            'meeting': meeting
        })
