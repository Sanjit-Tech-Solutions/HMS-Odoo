# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",
    'summary': "Hospital Management System with ICU Bed Booking",
    'description': """
    Complete Hospital Management System including:
    - Patient Management
    - Appointment Scheduling
    - ICU Bed Booking System
    - Medical History, Vital Signs, Medication Plans
    - Medical Billing
    """,
    'author': "Sanjit Tech",
    'website': "https://www.Sanjittechsolutions.com",
    'category': 'Healthcare',
    'version': '17.0.1.0.0',
    'sequence': 5,
    'depends': ['base'],
    'images':['static/description/banner.png'],

    'data': [
        # Security
        'security/ir.model.access.csv',
        # 'security/security.xml',

        # Core Views
        'views/menu_views.xml',
        'views/patient_view.xml',
        'views/appointment_views.xml',
        'views/doctor_note_views.xml',
        'views/medical_history_views.xml',
        'views/vital_sign_views.xml',
        'views/hospital_medication_plan_line_views.xml',
       # 'views/hospital_icu_booking_line_view.xml',

        # ICU Bed Booking System
        'views/icu_bed_views.xml',
        'views/icu_booking_views.xml',
        'data/icu_bed_data.xml',
        # 'data/icu_bed_cron.xml',

        # Dashboards and Logins
        'views/reception_dashboard_views.xml',
        'views/reception_login.xml',
        'views/doctor_login_views.xml',
        'views/icu_bed_login_view.xml',
        'views/medical_billing_login_view.xml',

        # Medical Billing
        'views/medicalbill_views.xml',
        'report/report_medical_bill.xml',
        # 'views/medicalbillreport_views.xml',

        # Test Types
        'data/test_type_data.xml',


        # Future/Optional Views
        # 'views/labtest_views.xml',
        # 'views/bloodtest_views.xml',
        # 'views/urinetest_views.xml',
        # 'views/cardiactest_views.xml',
        # 'views/rapiddiagnostic_views.xml',
        # 'views/imagingtest_views.xml',
        # 'views/billing_log_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            # Custom Styles
            'hospital_management_system/static/src/css/custom.css',
            'hospital_management_system/static/src/css/status_styles.css',
            'hospital_management_system/static/src/css/custom_buttons.css',
            'hospital_management_system/static/src/css/medical_bills_style.css',
         #  'hospital_management_system/static/src/js/form_back_button.js',
           'hospital_management_system/static/src/css/icu_bed.css',
           'hospital_management_system/static/src/css/bed.css',

            # Static Images
            'hospital_management_system/static/src/img/bed.png',
            'hospital_management_system/static/description/bed1.png',
          #  'hospital_management_system/static/src/js/medical_bill_header_style.js',
        ],
        # 'web.assets_frontend': [
        #     'hospital_management_system/static/src/js/reset_form.js',
        # ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
