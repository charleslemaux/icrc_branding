{
    "name": "ICRC Brand Theme",
    "version": "1.0.0",
    "summary": "Apply ICRC brand colors and typography to Odoo backend",
    "author": "Charles Le Maux",
    "website": "https://projekts.com",
    "category": "Theme/Backend",
    "license": "LGPL-3",
    "depends": ["web"],
    "data": [
        "views/assets.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # Load variable overrides BEFORE Odoo compiles its own SCSS variables.
            # Odoo's primary_variables uses !default, so our values win and cascade
            # through the full Odoo → Bootstrap SCSS pipeline.
            (
                "before",
                "web/static/src/scss/primary_variables.scss",
                "icrc_branding/static/src/scss/brand_variables.scss",
            ),
            # Runtime styles: typography, shapes, and component polish
            "icrc_branding/static/src/scss/brand.scss",
        ],
    },
    "installable": True,
    "application": False,
}
