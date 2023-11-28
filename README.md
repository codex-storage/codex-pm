# Codex Project Management

For creating/tracking milestones, epics, and issues as well as populating/updating planning labels to all Codex organization repos.

## Sub-teams
The Codex team is currently split into the following sub-teams:
- Codex Client
- Codex Marketplace
- Codex Infrastructure
- Codex Testing
- Codex Research
- Codex BD [TBA]

with support from the following external Logos teams:
- Token Engineering (Vac)
- Smart-Contracts (Vac)
- Communications (Acid.Info)

## Work Tracking and Reporting Guidelines
1. Weekly Reporting
    - Each sub-team should have a weekly sync to discuss progress and blockers
    - Each sub-team should have a bi-weekly report to share with the Codex team
    - The project lead should have a weekly report to share with the Logos team
2. Monthly Reporting
    - Monthly reporting is done via the Program Lead/Owner via the Monthly Report that encompasses Codex updates inclusive of other Logos projects

### Terminology

| Name            | Number of                               | Timeframe                              | Team Scope                                   | Owner                       | Description                                                                 |
|-----------------|-----------------------------------------|----------------------------------------|----------------------------------------------|-----------------------------|-----------------------------------------------------------------------------|
| (Key) Milestone | 1-3 per year                            | Set yearly-ish/as needed               | Most subteams                                | Codex Lead                   | Key achievements for the Codex project, historical milestones.               |
| Epic            | Several per milestone                   | Set for a milestone, delivered monthly | Several subteams or external team (e.g. Commujnications) | Team Members                | Chunk of a _Milestone_ across all clients.                                  |
| Task            | Many per Epic                           | Set monthly-ish, delivered weekly      | One subteam or individual                    | Team Member                 | May be one or several piece of work, client specific.                       |  

### Epic Owner Responsibilities
Each epic should have an owner per affected subteam (e.g. Codex Client, Codex Marketplace, Codex Infrastructure, Codex Testing, Codex Research, Codex BD) who is responsible for:
- Capturing the problem statement
- Defining the scope
- Defining the success criteria
- Designing and implementing the PoC
- Creating unit & integration tests/simulations to confirm PoC performance meeting success criteria

For development teams, it is expected that design/break down is done by epic owner. But actual work can be picked up by other team member. Epic owner must:

- Understand the change and its implications
- Liaise with researcher for any doubt or questions or design issues related to specific client/use case
- Create issues (Tasks) to break down work in client repo, include an acceptance criteria in each issue to ensure that the objective/end goal/behaviour is clearly described

It is likely that the epic owner will do the core change or first change for a given epic. However, subsequent/other changes may be picked up in parallel or sequentially by other team members.
Hence:

- Dependencies must be clearly stated in Task issue description
- Team members must assign Task issues to themselves when work starts
- Team member must update issues to track progress

The program manager should ensure that epics are getting the right assignee in a timely fashion. For example, when research work starts for a given epic, epic owners from development team should be assigned, so they know to participate in discussions. Program manager should also ensure that issues are being created in a timely fashion, an is encouraged to use client PM call as a forum to check epics to be assigned. For example, when PoC is near completion then breaking down the work should be started.

### GitHub Usage
A _Milestone_:
- MUST have a matching GH issue in the https://github.com/codex-storage/codex-pm repo with `milestone` label assigned
- MUST have a GH Milestone in https://github.com/codex-storage/codex-pm repo, to which relevant _Epics_ are added
- SHOULD have a roadmap to delivery done at planning phase, the GH milestone is then used to track progress
An _Epic_:
- MUST have a matching GH issue in the https://github.com/codex-storage/codex-pm with `epic` label assigned.
- MUST have a label with format `E:<epic name>` created across all relevant https://github.com/codex-storage/ repos (see [labels.yml](./.github/labels.yml))
- SHOULD be added to a GH Milestone
- SHOULD have a `Planned Start` and `Due Date` set (these are GitHub projects fields you can find in the `Projects` section of the issue view sidebar)
- MAY list _Tasks_ present in other repos
- MUST have one assignee **per subteam**, who represent the epic owner

A _Task_:
- MAY be tracked as a todo item in a GH Issue (_Task_ or _Epic_),
- OR MAY be tracked as a single GH issue
  - that MUST be labelled with related _Epic_ label (`E:...`),
- OR MAY be tracked as a GH Pull Request
    - that MUST be labelled with related _Epic_ label (`E:...`),
- MUST have an _acceptance criteria_ and/or a list of _tasks_ (that can be other GH issues).

Finally, for _Tasks_ that do not belong to a given _Epic_ or _Milestone_:
- MUST have either labels:
  - `bug`: This is a bug, likely reported by a user
  - `enhancement`: This is an enhancement out of the scope of the technical roadmap, likely reported by a user
    - Major enhancements should be carefully reviewed and prioritized
  - `documentation`: Documentation improvement or correction
  - `dependencies`: Upgrade dependencies in a timely manner to avoid time wasting when the dependency upgrade becomes critical

Which means, in terms of _navigation_:

- Work for a Milestone is described in the related GitHub issue and tracked in the GitHub milestone.
- In the GitHub milestone, we have a list of _Epics_ to be achieved, the _Epics_ are being closed as the work is done across one or more sub-teams
- To look at remaining work for an _Epic_, one need to look at all issues/PRs (_Tasks_) with the corresponding _Epic_ label (`E:...`)

### Reporting

**Monthly**:

- Handled by Insights team

**Weekly**: Report progress on each **active** _Epic_ or _Task_ per sub-team.

- Every Friday, all team members must include a weekly summary of their work and progress in the #standups channel within the Codex Discord server inclusive of any links to relevant Epics/Issues/PRs.

- On Monday, project lead or responsible person for report can generate a report and post it in the Logos Discord server in the #leads-roundup channel.

## Milestones

https://github.com/codex-storage/codex-pm/milestones
