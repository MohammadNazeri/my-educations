# Cookiecutter
* Cookiecutter is a tool that helps you quickly create project templates. So you don’t have to start from scratch every time.
* Cookiecutter is just a templating engine. You can use it to generate non-programming projects: documentation project, etc.
* Cookiecutter doesn’t care what’s inside the files. It just replaces placeholders and creates folder structures.
### How to work?
Template could be in repo (most common) or local.
1. pip install cookiecutter
2. Cookiecutter [repo address]
3. Created project after answering questions

# Programming Template
* Template is skeleton of a project which contain placeholders (like {{project_name}})

## Structure
```
cookiecutter-template/
├─ cookiecutter.json
├─ {{cookiecutter.project_name}}/
│  ├─ README.md
│  ├─ setup.py
│  ├─ {{cookiecutter.package_name}}/
│  │  └─ __init__.py
│  └─ tests/
│     └─ test_main.py
```
* cookiecutter.json: It defines variables and default values.
```
{
  "project_name": "MyProject",
  "package_name": "my_project",
  "author_name": "Your Name",
  "version": "0.1.0"
}
```
* {{cookiecutter.variable}}: Double curly braces denote variables to be replaced. They can be used as name or inside files.
* Hooks: Python scripts run before or after generation (pre_gen_project.py, post_gen_project.py).

# Top Helm Chart Template
* Top Helm Chart or Umbrella chart is a Helm chart whose main purpose is to include other charts as dependencies.
* It doesn’t usually contain application manifests itself and references other charts in Chart.yaml under the dependencies section.
```
my-chart/
├─ Chart.yaml
├─ values.yaml
├─ charts/
├─ [templates/]
└─ .helmignore

```
