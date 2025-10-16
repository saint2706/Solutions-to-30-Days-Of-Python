# Contributing to Coding for MBA

Thank you for your interest in shaping the Coding for MBA curriculum! This guide is written for external contributors who want to improve lessons, documentation, tooling, or community resources.

- 🧭 [Ways to contribute](#ways-to-contribute)
- 🛠️ [Development environment](#development-environment)
- 🔄 [Contribution workflow](#contribution-workflow)
- ✅ [Quality checklist](#quality-checklist)
- 💬 [Community and support](#community-and-support)

## Ways to Contribute

We welcome contributions that help business-focused learners succeed:

| Area | Examples |
| ---- | -------- |
| **Curriculum & Content** | Clarify lesson explanations, fix typos, expand business scenarios, add exercises or solution walkthroughs. |
| **Code Enhancements** | Improve sample scripts, add tests, refactor utilities, or expand data-loading helpers. |
| **Documentation** | Update guides in `docs/`, add troubleshooting steps, or improve onboarding materials. |
| **Community** | Share learning tips, provide feedback, or propose roadmap ideas in GitHub Discussions. |

If you have a new idea, open a [GitHub Discussion](https://github.com/saint2706/Coding-For-MBA/discussions) in the **Feedback & Ideas** category to align on direction before building.

## Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/saint2706/Coding-For-MBA.git
   cd Coding-For-MBA
   ```
2. **Create a virtual environment** (Python 3.12+ recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # for linting and tests
   ```
4. **Optional extras**: Use `make format`, `make lint`, and `mkdocs serve` to work with formatting and documentation locally.

## Contribution Workflow

1. **Discuss** – Search existing [issues](https://github.com/saint2706/Coding-For-MBA/issues) and [discussions](https://github.com/saint2706/Coding-For-MBA/discussions). Open a new thread or issue if needed to gather context.
2. **Fork & branch** – Fork the repository and create a feature branch (`git checkout -b feature/your-feature`).
3. **Make focused changes** – Follow the project structure; update or add tests and documentation that reflect the change.
4. **Run checks locally**
   ```bash
   make format  # optional but recommended
   make lint
   pytest
   ```
5. **Commit with context** – Write clear commit messages summarizing the change and reference related issues.
6. **Submit a pull request** – Provide:
   - A concise summary of changes
   - Testing evidence (commands run)
   - Screenshots or recordings if you modified visual output
   - Links to related discussions or issues
7. **Collaborate on review** – Be ready to answer questions, iterate on feedback, and keep discussions respectful. Once approved, maintainers will merge your pull request.

## Quality Checklist

Before requesting a review, ensure you have:

- [ ] Added or updated automated tests when touching executable code.
- [ ] Confirmed `pytest` passes locally (or explained why it fails).
- [ ] Run `make lint` to satisfy formatting and linting standards.
- [ ] Updated relevant documentation (`README`, lesson guides, or MkDocs pages).
- [ ] Verified links and relative paths for any new Markdown content.
- [ ] Included attribution for external datasets or resources where required.

## Community and Support

- **GitHub Discussions:** Join the learner community, ask for feedback, and help triage questions in the [Help Desk](https://github.com/saint2706/Coding-For-MBA/discussions/categories/help-desk) and **Show and Tell** categories.
- **Issues:** Use GitHub issues for actionable tasks or bug reports once requirements are clear.
- **Code of Conduct:** Practice empathy and inclusivity. Be constructive, stay on topic, and respect privacy when sharing business data examples.

Need help getting started? Open a [Discussion](https://github.com/saint2706/Coding-For-MBA/discussions/new) and a maintainer or community host will respond.
