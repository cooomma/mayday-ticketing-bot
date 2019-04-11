
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import mayday

from mayday.db.tables.events import EventsModel
from mayday.db.tables.tickets import TicketsModel
from mayday.helpers.feature_helpers import FeatureHelper
from mayday.helpers import chart_helper

event_table = EventsModel(mayday.engine, mayday.metadata)
ticket_table = TicketsModel(mayday.engine, mayday.metadata)


class EventHelper(FeatureHelper):

    @staticmethod
    def generate_keyboard(events: list) -> list:
        return InlineKeyboardMarkup(
            [[InlineKeyboardButton(event['name'], url=event['url'])] for event in events], one_time_keyboard=True)

    def list_all_events(self) -> list:
        return event_table.list_all_events()

    def generate_charts(self) -> list:
        stats = ticket_table.transform_tickets_stats(ticket_table.get_ticket_stats())
        return dict(
            # ticket_charts=chart_helper.generate_ticket_graphs(ticket_distribution=stats['ticket_distribution'], updated_at=stats['updated_at']),
            status_distribution=stats['status_distribution'],
            updated_at=stats['updated_at'])

    def reset_cache(self, user_id: int, username: str):
        pass

    def update_cache(self, user_id: int, value: (str, int)):
        pass
