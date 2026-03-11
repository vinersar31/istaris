# GitHub Wiki Integration

The Markdown files in this directory (`docs/wiki/`) are designed to be published to this repository's GitHub Wiki.

## How to Deploy to the Wiki

GitHub Wikis are backed by their own separate Git repositories. To publish these files:

1.  **Clone the Wiki Repository:**
    Navigate to your repository on GitHub, click the **Wiki** tab, and look for the "Clone this wiki locally" URL at the bottom of the right sidebar. It usually looks like `https://github.com/YOUR_USERNAME/YOUR_REPO.wiki.git`.

    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO.wiki.git
    cd YOUR_REPO.wiki
    ```

2.  **Copy the Files:**
    Copy the `.md` files from this `docs/wiki/` directory into your cloned wiki repository.

    ```bash
    cp -r ../path/to/your/repo/docs/wiki/*.md .
    ```

3.  **Commit and Push:**
    Commit the changes and push them back to the wiki repository.

    ```bash
    git add .
    git commit -m "Update wiki documentation"
    # git push origin master
    ```

*Note: The `Home.md` file will serve as the main landing page of your GitHub Wiki.*
