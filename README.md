# Social Data and Visualization

To preview the site locally:
```sh
quarto preview
```

To deploy the site to GitHub pages:
```sh
quarto publish
```

## Development

This project uses Poetry to manage the environment and dependencies.
```sh
# bootstrap the environment
poetry install --with dev

# activate the python virtualenv
poetry shell

# alternatively we can activate the virtualenv like so
source .venv/bin/activate
```
