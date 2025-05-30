from quart import Blueprint

from enums import SearchType
from search.handler import search_handler
from moderation.auth import web_usr_logged_in, web_usr_is_admin, load_web_usr_data
from quart_rate_limiter import rate_limit
from datetime import timedelta


bp = Blueprint("bp_web_index_search", __name__)


@bp.get("/fts")
@load_web_usr_data
@web_usr_logged_in
@web_usr_is_admin
@rate_limit(5, timedelta(minutes=1))
async def v_index_search_get(is_admin: bool, logged_in: bool):
    return await search_handler(SearchType.idx, logged_in=logged_in, is_admin=is_admin)


@bp.post("/fts")
@load_web_usr_data
@web_usr_logged_in
@web_usr_is_admin
@rate_limit(1, timedelta(minutes=5))
async def v_index_search_post(is_admin: bool, logged_in: bool):
    return await search_handler(SearchType.idx, logged_in=logged_in, is_admin=is_admin)
