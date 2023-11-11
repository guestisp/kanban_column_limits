/** @odoo-module **/
import { KanbanRenderer } from "@web/views/kanban/kanban_renderer";
import { KanbanHeader } from "@web/views/kanban/kanban_header";

class kanban_colum_limitsKanbanHeader extends KanbanHeader {
    static template = "kanban_column_limits-main.KanbanHeader";
    static components = {
        ...KanbanHeader.components,
        //....
    };
}

export class kanban_colum_limitsKanbanRenderer extends KanbanRenderer {}
kanban_colum_limitsKanbanRenderer.components = {
    ...KanbanRenderer.components,
    KanbanHeader: kanban_colum_limitsKanbanHeader,
};