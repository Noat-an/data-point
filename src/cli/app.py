import click
import uvicorn


@click.command(help="Command to launch app")
@click.option(
    "-prod",
    help="If specified, the application is launched as prod without reload.",
    is_flag=True,
    default=False,
)
def app_start(prod: bool) -> None:
    uvicorn.run(
        "src.manage:app",
        host="0.0.0.0",
        port=7000,
        workers=2,
        reload=(not prod))
