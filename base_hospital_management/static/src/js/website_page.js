odoo.define('base_hospital_management.website_page', function (require) {
    'use strict';
    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');
    publicWidget.registry.doctorWidget = publicWidget.Widget.extend({
        selector: '#booking_form',
        events: {
            'change #booking_date': 'changeBookingDate',
            'change #doctor-department': 'updateDoctorOptions',
            'change #doctor-name': 'updateConsultationPrice',
        },
        start: function () {
            this.changeBookingDate();
        },
        changeBookingDate: function () {
            var self = this;
            var selectedDate = this.$('#booking_date').val();
            ajax.jsonRpc('/patient_booking/get_doctors', 'call', {
                selected_date: selectedDate, department:false
            }).then(function (data) {
                self.$('#doctor-name').empty();
                // Add the fetched doctors to the dropdown
                _.each(data['doctors'], function (doctor) {
                    self.$('#doctor-name').append($('<option>', {
                        value: doctor.id,
                        text: doctor.name,
                        'data-price': doctor.price_consultant // Updated field name
                    }));
                });
                self.$('#doctor-department').empty();
                // Add the fetched departments to the dropdown
                self.$('#doctor-department').append($('<option>'));
                _.each(data['departments'], function (dep) {
                    self.$('#doctor-department').append($('<option>', {
                        value: dep.id,
                        text: dep.name,
                    }));
                });
                // Update consultation price when doctors are loaded
                self.updateConsultationPrice();
            });
        },
        updateDoctorOptions: function () {
            var self = this;
            var selectedDate = this.$('#booking_date').val();
            var department = this.$('#doctor-department').val();
            ajax.jsonRpc('/patient_booking/get_doctors', 'call', {
                selected_date: selectedDate, department:department
            }).then(function (data) {
                self.$('#doctor-name').empty();
                // Add the fetched doctors to the dropdown
                 _.each(data['doctors'], function (doctor) {
                    self.$('#doctor-name').append($('<option>', {
                        value: doctor.id,
                        text: doctor.name,
                        'data-price': doctor.price_consultant // Updated field name
                    }));
                });
                // Update consultation price when doctors are loaded
                self.updateConsultationPrice();
            });
        },
        updateConsultationPrice: function () {
            // Update consultation price based on selected doctor
            var selectedDoctor = this.$('#doctor-name option:selected');
            var consultationPrice = selectedDoctor.data('price') || 0;

            // Format the price for display
            var formattedPrice = new Intl.NumberFormat('en-US', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }).format(consultationPrice);

            this.$('#price_consultant').val(formattedPrice);
        },
    });
    return publicWidget.registry.doctorWidget;
});