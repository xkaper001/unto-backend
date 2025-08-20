from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.exception import AppwriteException
import os
from portia import (
    Config,
    LLMProvider,
    Portia,
    example_tool_registry,
)

# This Appwrite function will be executed every time your function is triggered
def main(context):
    
    google_config = Config.from_default(
        llm_provider=LLMProvider.GOOGLE,
        default_model="google/gemini-2.5-flash",
        google_api_key=os.environ['GOOGLE_API_KEY']
    )

    portia = Portia(config=google_config, tools=example_tool_registry)
    
    req_path = context.req.path
    if (req_path == "/ping"):
        return context.res.text("Pong")
    
    if (req_path == "/add"):
        plan_run = portia.run('add 1 + 2')
        res = plan_run.model_dump_json(indent=2)
        print(res)
        return context.res.json(res)

    return context.res.text("hello")


    # try:
    #     response = users.list()
    #     # Log messages and errors to the Appwrite Console
    #     # These logs won't be seen by your end users
    #     context.log("Total users: " + str(response["total"]))
    # except AppwriteException as err:
    #     context.error("Could not list users: " + repr(err))

    # # The req object contains the request data
    # if context.req.path == "/ping":
    #     # Use res object to respond with text(), json(), or binary()
    #     # Don't forget to return a response!
    #     return context.res.text("Pong")

    # return context.res.json(
    #     {
    #         "motto": "Build like a team of hundreds_",
    #         "learn": "https://appwrite.io/docs",
    #         "connect": "https://appwrite.io/discord",
    #         "getInspired": "https://builtwith.appwrite.io",
    #     }
    # )
