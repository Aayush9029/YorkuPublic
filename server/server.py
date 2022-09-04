import json
import fastapi
import uvicorn
from time import time
from fastapi.encoders import jsonable_encoder
from get_api.reddit_post import RedditAPI
from get_api.utils import ServiceEnums, log_info
from os.path import basename

AUTH_FILE = "server_auth.json"

app = fastapi.FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

reddit = RedditAPI()


async def get_reddit_posts():
    start = time()
    data = reddit.get_data(cache_enabled=True)
    json_data = jsonable_encoder(data, exclude_none=True)
    log_info(ServiceEnums.REDDIT, f"Time taken: {time() - start} seconds")
    return json_data


@app.get("/reddit")
async def get_youtube_data_async():
    log_info(ServiceEnums.REDDIT, "Getting reddit data")
    data = await get_reddit_posts()
    return data


def main():
    # start server
    app_name = "server"
    log_config = uvicorn.config.LOGGING_CONFIG
    # file is logs/logs.log
    log_config["formatters"]["access"][
        "fmt"
    ] = "%(asctime)s - %(levelname)s - %(message)s"

    uvicorn.run(
        app=f"{app_name}:app",
        host="0.0.0.0",
        port=53237,
        workers=1,
        reload=False,
        log_config=log_config,
    )


if __name__ == "__main__":
    main()
