/** @odoo-module **/
import { registry } from "@web/core/registry";
import { kanbanView } from "@web/views/kanban/kanban_view";
import { KanbanRenderer } from "@web/views/kanban/kanban_renderer";
import { KanbanHeader } from "@web/views/kanban/kanban_header";

class kanban_colum_limits_KanbanHeader extends KanbanHeader {
    static template = "kanban_column_limits-main.KanbanHeader";
    static components = {
        ...KanbanHeader.components,
        //....
    };
}

export class kanban_colum_limits_KanbanRenderer extends KanbanRenderer {}
kanban_colum_limits_KanbanRenderer.components = {
    ...KanbanRenderer.components,
    KanbanHeader: kanban_colum_limits_KanbanHeader,
};

export const kanban_colum_limits_KanbanView = {
    ...kanbanView,
    Renderer: kanban_colum_limits_KanbanRenderer,
};

registry.category("views").add("kanban_column_limits_kanban_view", kanban_colum_limits_KanbanView);