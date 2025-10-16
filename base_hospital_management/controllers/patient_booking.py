# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from odoo import fields, http
from odoo.http import request
import base64






from odoo import http, fields
from odoo.http import request
import base64

class PatientBooking(http.Controller):

    @http.route('/patient_booking', type='http', auth="public", website=True)
    def patient_booking(self):
        """First form for patient info"""
        if request.env.user._is_public():
            return request.redirect('/web/login')
        values = {
            'user': request.env.user.name,
            'date': fields.date.today()
        }
        return request.render("base_hospital_management.patient_booking_form", values)

    @http.route('/patient_booking/success', type='http', auth="public", website=True, csrf=False)
    def patient_booking_step2(self, **kw):
        """Second form for payment screenshot"""
        # Temporarily store form 1 data in session
        request.session['patient_form_data'] = kw
        return request.render("base_hospital_management.patient_booking_form_step2", {})

    @http.route('/patient_booking/final_submit', type='http', auth="public", website=True, csrf=False)
    def patient_booking_final_submit(self, **kw):
        """Final submission with payment screenshot"""
        form_data = request.session.get('patient_form_data', {})

        # Process payment file
        payment_file = kw.get('payment_screenshot')
        payment_screenshot = False
        filename = False
        if payment_file:
            payment_screenshot = base64.b64encode(payment_file.read())
            filename = payment_file.filename

        # Create Outpatient record
        op = request.env['hospital.outpatient'].sudo().create({
            'patient_id': request.env.user.partner_id.id,
            'doctor_id': int(form_data.get("doctor-name")),
            'op_date': form_data.get("date"),
            'reason': form_data.get("reason"),
            'date_of_birth': form_data.get("date_of_birth"),
            'age': form_data.get("age"),
            'gender': form_data.get("gender"),
            'mobile': form_data.get("mobile"),
            'email': form_data.get("email"),
            'payment_screenshot': payment_screenshot,
            'payment_screenshot_filename': filename,
        })

        op.sudo().action_confirm()
        request.session.pop('patient_form_data', None)
        return request.redirect('/my/home')







#
# class PatientBooking(http.Controller):
#     """Class for patient booking"""
#
#     @http.route('/patient_booking', type='http', auth="public", website=True)
#     def patient_booking(self):
#         """Function for patient booking from website."""
#         if request.env.user._is_public():
#             return request.redirect('/web/login')
#         values = {
#             'user': request.env.user.name,
#             'date': fields.date.today()
#         }
#         return request.render(
#             "base_hospital_management.patient_booking_form", values)
#
#     @http.route('/patient_booking/success', type='http',
#                 website=True, csrf=False)
#     def patient_booking_submit(self, **kw):
#         """Function for submitting the patient booking"""
#         if request.env.user.partner_id.patient_seq in ['New', 'User',
#                                                        'Employee']:
#             request.env.user.partner_id.sudo().write(
#                 {'patient_seq': request.env['ir.sequence'].sudo().next_by_code(
#                     'patient.sequence')}) or 'New'
#         payment_file = kw.get('payment_screenshot')
#         payment_screenshot = False
#         filename = False
#         if payment_file:
#             payment_screenshot = base64.b64encode(payment_file.read())
#             filename = payment_file.filename
#
#         op = request.env['hospital.outpatient'].sudo().create({
#             'patient_id': request.env.user.partner_id.id,
#             'doctor_id': int(kw.get("doctor-name")),
#             'op_date': kw.get("date"),
#             'reason': kw.get("reason"),
#             'date_of_birth': kw.get("date_of_birth"),
#             'age': kw.get("age"),
#             'gender': kw.get("gender"),
#             'mobile': kw.get("mobile"),
#             'email': kw.get("email"),
#             'payment_screenshot': payment_screenshot,
#             'payment_screenshot_filename': filename,
#         })
#         op.sudo().action_confirm()
#         return request.redirect('/my/home')

    # @http.route('/patient_booking/get_doctors', type='json', auth="public",
    #             website=True)
    # def update_doctors(self, **kw):
    #     """Method for fetching doctor allocation for the selected date"""
    #     domain = [('date', '=', kw.get('selected_date'))]
    #     departments = []
    #     doctors = []
    #     if kw.get('department'):
    #         domain.append(
    #             ('doctor_id.department_id.id', '=', kw.get('department')))
    #     allocation = request.env['doctor.allocation'].sudo().search(domain)
    #     for rec in allocation:
    #         if request.env.user.partner_id not in rec.mapped(
    #                 'op_ids.patient_id'):
    #             doctors.append({'id': rec.id, 'name': rec.name})
    #             if ({'id': rec.department_id.id, 'name': rec.department_id.name}
    #                     not in departments):
    #                 departments.append({'id': rec.department_id.id,
    #                                     'name': rec.department_id.name})
    #     return {'doctors': doctors, 'departments': departments}

    @http.route('/patient_booking/get_doctors', type='json', auth="public", website=True)
    def update_doctors(self, **kw):
        """Method for fetching doctor allocation for the selected date"""
        domain = [('date', '=', kw.get('selected_date'))]
        departments = []
        doctors = []
        if kw.get('department'):
            domain.append(
                ('doctor_id.department_id.id', '=', kw.get('department')))
        allocation = request.env['doctor.allocation'].sudo().search(domain)
        for rec in allocation:
            if request.env.user.partner_id not in rec.mapped(
                    'op_ids.patient_id'):
                doctors.append({
                    'id': rec.id,
                    'name': rec.name,
                    'price_consultant': rec.price_consultant or 0.0  # Updated field name
                })
                if ({'id': rec.department_id.id, 'name': rec.department_id.name}
                        not in departments):
                    departments.append({'id': rec.department_id.id,
                                        'name': rec.department_id.name})
        return {'doctors': doctors, 'departments': departments}