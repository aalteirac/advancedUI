import json
import streamlit as st

from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event
from types import SimpleNamespace

from dashboard import Dashboard, Editor, Card, DataGrid, Radar, Pie, Player


def main():
    st.write(
        """
       ✨ Based on streamlit-elements custom component [![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]
        =====================

        [github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
        [github_link]: https://github.com/okld/streamlit-elements

        [pypi_badge]: https://badgen.net/pypi/v/streamlit-elements?icon=pypi&color=black&label
        [pypi_link]: https://pypi.org/project/streamlit-elements
        """
    )
    # st.title("")
    if "w" not in state:
        board = Dashboard()
        w = SimpleNamespace(
            dashboard=board,
            card=Card(board, 0, 0, 3, 7, minW=2, minH=4),
            card2=Card(board, 3, 0, 3, 7, minW=2, minH=4),
            card3=Card(board, 6, 0, 3, 7, minW=2, minH=4),
            card4=Card(board, 9, 0, 3, 7, minW=2, minH=4),
            data_grid=DataGrid(board, 0, 7, 6, 6, minH=4),
            player=Player(board, 7, 7, 6, 6, minH=5),
            editor=Editor(board, 0, 23, 12, 5, minW=3, minH=3),
            # pie=Pie(board, 6, 0, 6, 7, minW=3, minH=4),
            # radar=Radar(board, 12, 7, 3, 7, minW=2, minH=4),
        )
        state.w = w

        w.editor.add_tab("Card content", Card.DEFAULT_CONTENT, "plaintext")
        w.editor.add_tab("Data grid", json.dumps(DataGrid.DEFAULT_ROWS, indent=2), "json")
        # w.editor.add_tab("Radar chart", json.dumps(Radar.DEFAULT_DATA, indent=2), "json")
        # w.editor.add_tab("Pie chart", json.dumps(Pie.DEFAULT_DATA, indent=2), "json")
    else:
        w = state.w

    with elements("demo"):
        event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

        with w.dashboard(rowHeight=57):
            w.editor()
            w.card(w.editor.get_content("Card content"))
            w.card2(w.editor.get_content("Card content"))
            w.card3(w.editor.get_content("Card content"))
            w.card4(w.editor.get_content("Card content"))
            w.player()
            # w.pie(w.editor.get_content("Pie chart"))
            # w.radar(w.editor.get_content("Radar chart"))
            w.data_grid(w.editor.get_content("Data grid"))


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
