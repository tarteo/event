from odoo import fields, models


class EventEvent(models.Model):
    _inherit = "event.event"

    is_external = fields.Boolean(
        string="External Event",
        help="Indicates whether the event is external or not. "
        "External events are events that are not managed by Odoo, "
        "but are promoted on the website. If this field is checked, "
        "the registration button will redirect the user to the external URL.",
    )

    external_url = fields.Char(
        string="External URL",
        help="The URL of the external event. It will be used to "
        "redirect the user when clicking on the registration button.",
    )
