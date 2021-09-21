# Guide for Contributors

*Please note that this is a pre-alpha version of the site and we are not currently accepting contributions from the public.*

We are always seeking contributions and testers for all sections of the site. See our [list of open issues](https://github.com/agully1/ca-knowledgebase/issues) for places where contributions are required, or suggest your own.

:::{note}
You must have a [GitHub](https://github.com/) account to make suggestions or contributions. Create one [here](https://github.com/signup). You can find a simple tutorial on using basic GitHub functionality [here](https://guides.github.com/activities/hello-world/).
:::

## Making suggestions

If you have a suggestion or issue to raise, please use the GitHub issues feature. To create a new issue, click the GitHub icon at the top of any page and select 'Open Issue'. This will open an issue in the associated GitHub repository.

Please provide as much detail as possible to allow the issue to be addressed.

## Contributing to the site

If you choose to contribute, you may want to look at [How to Contribute to an Open Source Project on GitHub](https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github). In brief:

1. The published copy of the knowledgebase is in the main branch of the repository (so that GitHub will regenerate it automatically). Please create all branches from that, and merge the main repository's main branch into your main branch before starting work. Please do not work directly in your main branch, since that will make it difficult for you to work on other contributions.

2. We use [GitHub flow](https://guides.github.com/introduction/flow/) to manage changes:
    1. Create a new branch in your desktop copy of this repository for each significant change.
    2. Commit the change in that branch.
    3. Push that branch to your fork of this repository on GitHub.
    4. Submit a pull request from that branch to the main repository.
    5. If you receive feedback, make changes on your desktop and push to your branch on GitHub: the pull request will update automatically.
	
The site has maintainers who review issues and pull requests or encourage others to do so. The maintainers are community volunteers, and have final say over what gets merged into the knowledgebase.

```{warning}
If making changes via pull requests, only changes to markdown (`.md`) and Jupyter notebook (`.ipynb`) files will be accepted. Do not make edits to HTML content as this will be automatically overwritten whenever the book is edited and rebuilt. 
```

By contributing, you agree that we may redistribute your work under our license. In exchange, we will address your issues and/or assess your change proposal as promptly as we can, and help you become a member of our community. Everyone involved in the Computational Acoustics Knowledgebase agrees to abide by our [code of conduct](code-of-conduct).

## For maintainers

This site runs using [Jupyter Books](https://jupyterbook.org/intro.html). If you have not used Jupyter Books before, please complete their [tutorial on creating your first book](https://jupyterbook.org/start/your-first-book.html) before contributing. Note that Windows users will need to use Python 3.7 not 3.8.

First ensure you have Jupyter Books and `ghp-import` installed:

```
pip install -U jupyter-book
pip install ghp-import
```

In order to build the book, create your own fork of the ca-knowledgebase repository. Then clone this repository to a local repository on your machine (N.B. if you are new to git on the command line, consider completing the [Software Carpentry lesson on version control with git](https://swcarpentry.github.io/git-novice/)):

```
cd myreponame
git clone https://github.com/<your-username>/ca-knowledgebase
```

Then build the Jupyter Book (if you make multiple builds, it is recommended to clean up before each new build):

```
jupyter-book clean ca-knowledgebase/
jupyter-book build ca-knowledgebase/
```

You can inspect the created book by opening the local HTML files in `ca-knowledgebase/_build`. Once you're happy with them, push the new source files to the online repository:

```
cd ca-knowledgebase
git add ./*
git commit -m "add your message here"
git push
```

Now create a pull request from your repo to the main repo. Once accepted, the lead maintainer will use `ghp-import` to publish the build artifact via GitHub Pages (see [Jupyter Books documentation](https://jupyterbook.org/start/publish.html) for more details):

```
ghp-import -n -p -f _build/html
```