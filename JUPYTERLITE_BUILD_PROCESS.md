# JupyterLite Build Process

This document explains how JupyterLite is integrated into the Coding-For-MBA documentation site.

## Overview

JupyterLite provides an in-browser Python environment that allows users to run lesson notebooks without installing anything. The integration includes:

1. **Launch buttons** on all lesson pages that link to JupyterLite
2. **Complete JupyterLite distribution** in `site/jupyterlite/` with all lesson notebooks
3. **Automated build process** in GitHub Actions that regenerates everything on each push

## Build Process

The build follows this sequence:

### 1. Generate Lesson Pages
```bash
python tools/build_docs.py
```
- Reads `Day_*/README.md` files
- Generates `docs/lessons/day-*.md` files
- Updates navigation in `mkdocs.yml`

### 2. Add JupyterLite Buttons (First Pass)
```bash
python tools/integrate_jupyterlite.py
```
- Finds all notebooks in `Day_*/` directories
- Adds "Interactive Notebooks" section to each lesson page
- Builds JupyterLite distribution to `site/jupyterlite/`
- Creates `docs/jupyterlite-guide.md`

### 3. Build MkDocs Site
```bash
mkdocs build --strict
```
- Builds HTML from `docs/` directory
- **Cleans `site/` directory first** (removes previous build)
- Generates static site with JupyterLite buttons in lesson HTML

### 4. Rebuild JupyterLite (Second Pass)
```bash
python tools/integrate_jupyterlite.py
```
- Rebuilds JupyterLite distribution to `site/jupyterlite/`
- Skips adding buttons (already present from step 2)
- Ensures JupyterLite files exist after MkDocs cleaned the site directory

## Why Build JupyterLite Twice?

MkDocs cleans the `site/` directory before building, which removes the JupyterLite distribution created in step 2. We need to:

1. Build it **before MkDocs** to add buttons to lesson pages
2. Build it **after MkDocs** to restore the JupyterLite files

This ensures both the HTML pages have buttons AND the JupyterLite environment is available to serve.

## File Structure

After the build, the `site/` directory contains:

```
site/
├── jupyterlite/              # JupyterLite distribution (136MB)
│   ├── lab/                  # JupyterLab interface
│   │   └── index.html        # Main entry point
│   ├── files/                # All lesson content
│   │   ├── Day_01_Introduction/
│   │   │   ├── helloworld.ipynb
│   │   │   └── solutions.ipynb
│   │   ├── Day_02_*/
│   │   └── ... (67 day directories)
│   ├── build/                # Pyodide runtime and dependencies
│   ├── api/                  # Content API endpoints
│   └── index.html            # JupyterLite landing page
├── lessons/                  # Generated lesson HTML
│   ├── day-01-introduction/
│   │   └── index.html        # Contains JupyterLite launch buttons
│   └── ... (67 lesson pages)
└── index.html                # Site homepage
```

## Local Testing

To test the build locally:

```bash
# Clean start
rm -rf site/

# Run the build sequence
python tools/build_docs.py
python tools/integrate_jupyterlite.py
mkdocs build --strict
python tools/integrate_jupyterlite.py

# Verify
echo "Checking lesson page..."
grep -c "Interactive Notebooks" site/lessons/day-01-introduction/index.html

echo "Checking JupyterLite..."
test -f site/jupyterlite/lab/index.html && echo "✓ JupyterLite lab exists"
ls site/jupyterlite/files/Day_01_Introduction/*.ipynb | wc -l

# Test locally
mkdocs serve
# Visit http://127.0.0.1:8000/lessons/day-01-introduction/
# Click a "Launch in JupyterLite" button
```

## GitHub Actions Workflow

The `.github/workflows/docs.yml` workflow runs on every push to main:

```yaml
- name: Generate lesson pages
  run: python tools/build_docs.py

- name: Add JupyterLite buttons to lessons
  run: python tools/integrate_jupyterlite.py

- name: Build MkDocs site
  run: mkdocs build --strict

- name: Build JupyterLite distribution
  run: python tools/integrate_jupyterlite.py

- name: Upload artifact
  uses: actions/upload-pages-artifact@v4
  with:
    path: site
```

The entire `site/` directory (including `site/jupyterlite/`) is uploaded to GitHub Pages.

## Verification on GitHub Pages

After deployment, verify:

1. **Lesson page**: Visit any lesson (e.g., `https://saint2706.github.io/Coding-For-MBA/lessons/day-01-introduction/`)
   - Should see "Interactive Notebooks" section
   - Should see launch buttons for each notebook

2. **JupyterLite lab**: Click a launch button
   - Should redirect to `/jupyterlite/lab?path=...`
   - JupyterLite should load (may take 30-60 seconds first time)
   - Notebook should open and be executable

3. **Direct access**: Visit `https://saint2706.github.io/Coding-For-MBA/jupyterlite/lab/`
   - Should see JupyterLab interface
   - File browser should show all Day_* directories

## Troubleshooting

### Buttons don't appear in lesson pages
- **Cause**: `build_docs.py` was run after `integrate_jupyterlite.py`
- **Solution**: Follow the correct build order (see "Build Process" above)

### JupyterLite returns 404
- **Cause**: JupyterLite wasn't built after MkDocs
- **Solution**: Run `python tools/integrate_jupyterlite.py` after `mkdocs build`

### Notebooks not found in JupyterLite
- **Cause**: Notebooks aren't in the `jupyter_lite_config.json` content directories
- **Solution**: Verify `jupyter_lite_config.json` includes all Day_* directories

### First launch is slow
- **Expected**: First launch downloads ~50MB Pyodide runtime
- **Solution**: Wait patiently; subsequent launches will be fast

## Maintenance

### Adding New Lessons

When adding a new `Day_XX_*` directory:

1. Add directory to `jupyter_lite_config.json` in the `contents` list
2. Run the build process (or push to main - GitHub Actions will handle it)
3. New lesson notebooks will automatically be included

### Updating JupyterLite Version

To update JupyterLite version:

1. Update version in `docs/requirements.txt`:
   ```
   jupyterlite-core>=0.X.X
   jupyterlite-pyodide-kernel>=0.X.X
   ```
2. Run build process locally to test
3. Push changes - GitHub Actions will use new version

## Configuration

### jupyter_lite_config.json

Key configuration options:

- `LiteBuildConfig.contents`: List of directories to include in JupyterLite
- `LiteBuildConfig.output_dir`: Where to build (set to `site/jupyterlite`)
- `jupyter-config-data.appName`: Display name in JupyterLite UI

### .gitignore

The build cache is excluded:
```
.jupyterlite.doit.db
```

The `site/` directory (including `site/jupyterlite/`) IS committed to the repository.

## Performance

- **Build time**: ~2-3 minutes for complete build
- **JupyterLite size**: 136MB (includes Pyodide runtime)
- **Total site size**: 148MB
- **First load**: 30-60 seconds (downloads runtime)
- **Subsequent loads**: < 5 seconds (runtime cached)

## Resources

- [JupyterLite Documentation](https://jupyterlite.readthedocs.io/)
- [Pyodide Documentation](https://pyodide.org/)
- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
