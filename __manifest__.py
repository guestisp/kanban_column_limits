{
    "name": "Column limits for Kanban",
    "version": "1.0.0",
    "summary": "Add column limits for kanban colums",
    "license": "AGPL-3",
    "depends": ["project"],
    "data": [
        "views/project_stage_view_form.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "kanban_column_limits-main/static/src/view/kanban/kanban_header.xml"
        ]
    },
    "installable": True,
}
