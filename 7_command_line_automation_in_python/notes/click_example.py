import click

@click.command()
@click.option('--phrase', prompt='Enter a phrase', help='')
def tokenize(phrase):
	"""tokenize a phrase"""
	click.echo(f"toakenized phrase: {phrase.split()}")

if __name__ == "__main__":
	tokenize()