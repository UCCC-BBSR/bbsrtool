import click
from .datamodel import Project
import hypothesis
from hypothesis import given
from hypothesis_jsonschema import from_schema


@click.group()
def cli():
    pass


@cli.command()
def make_example():
    p = Person()
    print(p.dict())


@cli.command()
def dump_model():
    """Dump out the json schema of the model"""
    print(Project.schema_json(indent=2))

if __name__ == '__main__':
    cli()