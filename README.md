# Applied Robotics (12224)

Course website for Robótica Aplicada at IBERO Puebla, maintained with MkDocs and the Material theme.

## Repository structure

| Path | Purpose |
|---|---|
| `docs/index.md` | Student starting point |
| `docs/Course_Overview/` | Syllabus, session schedule, project roadmap, Lab Log guide, resources |
| `docs/M0_Fundamentals_and_Tools/` | Robotics fundamentals and ROS 2 tutorials |
| `docs/M1_Manipulator_Kinematics/` | Manipulator kinematics and robot descriptions |
| `docs/M2_Dynamics_and_Control/` | Existing Jacobian and simulation integration material |
| `docs/M3_Trajectory_planning/` | Trajectory theory, exercises, and implementation tutorials |
| `docs/M4_Mobile_Fundamentals/` | Mobile kinematics, simulation, SLAM, and navigation |
| `docs/M6_Integration_and_validation/` | Existing project placeholders |
| `docs/css/` | Site styling |
| `mkdocs.yml` | Navigation and site configuration |
| `requirements.txt` | Site dependencies |
| `.github/workflows/ci.yml` | GitHub Pages deployment workflow |

Navigation labels describe teaching topics; existing file paths are retained to preserve links. The current folders do not yet contain every lesson in the revised syllabus. The course overview distinguishes the teaching schedule from available reference material.

## Local preview

From the repository root, create an environment and install the site dependencies:

```powershell
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

```bash
# Linux / macOS
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m mkdocs serve
```

Open the local URL printed by MkDocs. Start the student walkthrough at **Course**, then follow **Course Overview** in menu order.

To build a local copy, replace `serve` with `build`. Build output goes into the ignored `site/` directory. Review warnings as well as errors; unchanged teaching material has outstanding audit findings.

## Revision and review workflow

Course revisions are reviewed in bounded phases on `course-revision`.

1. Agree on the files and content included in the phase.
2. Make small, logically grouped commits that can be reviewed or reverted independently.
3. Check links, build the site, and review the rendered pages.
4. The instructor follows the content as a student and tests the flow.
5. Address feedback within that phase. Begin another segment only after the instructor explicitly authorizes it.

Phase 1 covers repository/site organization, the course landing page, and Course Overview. Module lessons, complete project specifications, laboratory authoring, technical corrections in other segments, and deployment require a subsequent explicit instruction.

Inspect `git status` and the diff before staging. Stage named files for each commit. Push only when explicitly authorized.

## Publishing

The existing workflow deploys to GitHub Pages when commits are pushed to `main` or `master`. Local preview and commits on `course-revision` do not publish the website. Review and approve a release before merging or pushing to a deployment branch.

## Student documentation

Students should use the [Lab Log guide](docs/Course_Overview/T0_2.md) and the separate [Lab Log website template](https://github.com/Gulden8ag/iberoP_Web). This repository contains the course website.
