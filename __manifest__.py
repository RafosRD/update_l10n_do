{
    'name': 'Update l10n do',
    'version': '10.0',
    'summary': '',
    'description': 'Update daccount and fiscal position',
    'category': '',
    'author': 'Raul Ovalle',
    'website': '',
    'license': '',
    'depends': ['account'],
    'data': [
        # Basic accounting data
        'data/l10n_do_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_chart_template_data.xml',
        'data/account_account_tag_data.xml',
        'data/account.tax.template.xml',
        # Country States
        'data/l10n_do_state_data.xml',
        # Adds fiscal position
        'data/fiscal_position_template.xml',
        # configuration wizard, views, reports...
        'data/account_chart_template_data.yml',
    ],

    'installable': True,
    'auto_install': False,
}