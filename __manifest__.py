{
    "name": "ICRC Brand Theme",
    "version": "19.0.2.4.1",
    "summary": "Deep violet brand override for Odoo 19 Enterprise backend",
    "description": """
ICRC Brand Theme — Odoo 19 Enterprise
======================================

Replaces Odoo's default Enterprise purple (#714B67) with ICRC deep violet
(#120427 / rgb(18, 4, 39)) across the entire backend.

**Global color override**
    Injects brand variables *before* Enterprise's primary_variables.scss so
    that every Odoo and Bootstrap component — buttons, links, navbar, focus
    rings, badges, checkboxes, active states — inherits the brand color
    automatically.

**Typography**
    Body text uses Inter; headings, labels, buttons and nav tabs use Poppins.
    Both loaded via Google Fonts ``<link>`` tags (not CSS ``@import``, which
    breaks Odoo's asset pipeline).

**Component polish (brand.scss)**
    - Softer border-radius (0.5 rem default, pill badges)
    - Off-white page background (#fafafa) with white card surfaces
    - Subtle card shadows and hover-lift on kanban cards
    - Uppercase list/table column headers in Poppins
    - Pill-shaped progress bars, branded priority stars
    - Thinner scrollbars, branded text selection
    - Flat home menu (no gradient overlay)
    - Smooth 150 ms transitions on interactive elements
    """,
    "author": "Charles Le Maux",
    "website": "https://projekts.com",
    "category": "Theme/Backend",
    "license": "LGPL-3",
    "depends": ["web", "web_enterprise"],
    "data": [
        "views/assets.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # Load variable overrides BEFORE Enterprise's primary_variables.
            # Enterprise builds button maps & derived colors eagerly, so our
            # values must be set before that file is processed.
            (
                "before",
                "web_enterprise/static/src/scss/primary_variables.scss",
                "icrc_branding/static/src/scss/brand_variables.scss",
            ),
            # Global runtime styles: typography, shapes, and component polish
            "icrc_branding/static/src/scss/brand.scss",
            # Recruitment-specific view overrides (moved from search_tools so
            # that module stays purely data-focused with no styling concerns).
            "icrc_branding/static/src/scss/recruitment.scss",
        ],
    },
    "installable": True,
    "application": False,
}
