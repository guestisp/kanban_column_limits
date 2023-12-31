{
    "name": "Column limits for Kanban",
    "version": "1.0.0",
    "summary": "Add column limits for kanban colums",
    "license": "AGPL-3",
    "depends": ["project"],
    "sequence": 70,
    "data": [
        "views/project_stage_view_form.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "kanban_column_limits-main/static/src/views/*.js",
            "kanban_column_limits-main/static/src/views/*.xml"
        ]
    },
    "installable": True,
}
