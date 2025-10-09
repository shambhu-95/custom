from odoo import models, fields, api
import uuid

class JitsiMeeting(models.Model):
    _name = "odoo.jitsi.meeting"
    _description = "Jitsi Meeting"

    name = fields.Char("Meeting Title", required=True)
    room_name = fields.Char("Jitsi Room", readonly=True)
    url = fields.Char("Meeting URL", compute="_compute_url", store=True)

    @api.model
    def create(self, vals):
        if not vals.get("room_name"):
            vals["room_name"] = f"OdooRoom_{uuid.uuid4().hex[:8]}"
        return super().create(vals)

    @api.depends("room_name")
    def _compute_url(self):
        for rec in self:
            if rec.room_name:
                rec.url = f"https://meet.jit.si/{rec.room_name}"
