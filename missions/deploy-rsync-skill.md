# Mission: Create deploy-rsync Skill

## Status: READY

<!--
Status rules:
- DRAFT: Has [OPEN] decisions. Cannot be executed.
- READY: All decisions [RESOLVED]. Can be picked up by an agent.
- IN_PROGRESS: Agent is executing.
- DONE: Verification passed.

EXECUTION GATE: If status is DRAFT, the executing agent MUST refuse to start
and instead list the unresolved decisions.
-->

## Goal
Codify the rsync+SSH deployment pattern into a reusable skill for VPS-based projects.

## Problem
portfolio-system has a scripts/deploy.sh that works but is project-specific. The pattern (rsync with excludes, env var verification, remote health check, notification) repeats for any VPS deployment.

## Source
`/Users/omrilorch/portfolio-system/scripts/deploy.sh`

## What the skill should do
1. Verify required env vars exist locally and on remote
2. Rsync project to VPS with standard excludes (.git, __pycache__, .env, data/, node_modules/, venv/)
3. Run remote setup commands (pip install, migrations, restart services)
4. Health check (curl endpoint or process check)
5. Send Telegram notification on success/failure (optional)
6. Rollback hint if health check fails

### Inputs
- Project path (local)
- Remote host + user + path
- Custom excludes (added to standard list)
- Post-deploy commands
- Health check command
- Telegram notification (on/off)

### Skill location
operator-kit/meta-tools/deploy-rsync/SKILL.md

## Open Decisions

### Decisions:

- **[RESOLVED] Output format**: What does the skill produce?
  - Option A: A standalone bash script file (e.g., `scripts/deploy.sh`) that gets saved to the project
  - Option B: A SKILL.md that, when invoked, runs the deploy commands directly via Claude Code bash tool
  - Option C: Both — generates the script file AND can execute it on demand
  - Resolution: Option C. Generate a `scripts/deploy.sh` bash script file saved to the project AND the SKILL.md can execute it on demand. The script is the version-controlled artifact; the skill is the interface. Matches existing portfolio-system pattern.

- **[RESOLVED] Rollback mechanism**: The mission says "rollback hint if health check fails" — how deep does rollback go?
  - Option A: Print a hint message only (e.g., "Run: ssh vps 'cd /path && git checkout HEAD~1'") — no automated rollback
  - Option B: Keep one previous version on VPS (rsync to deploy-prev/ before overwrite), script offers restore command
  - Option C: Git-based rollback — require the remote to be a git repo, use `git revert` on failure
  - Resolution: Option B. Rsync current deployment to `deploy-prev/` before overwrite. Print restore command on health check failure. No git dependency on remote.

- **[RESOLVED] Env var verification depth**: How thoroughly to check env vars?
  - Option A: Check existence only (`[ -z "$VAR" ]`) — fast, catches missing vars
  - Option B: Check existence AND validate format (e.g., URL format for API endpoints, port range)
  - Option C: Check existence on local AND remote via SSH — catches deployment env mismatches
  - Resolution: Option C. Verify env vars exist on both local machine and remote VPS via SSH. Catches the most common deploy failure: var missing on server.

- **[RESOLVED] Service restart strategy**: How to handle systemd service restarts during deploy?
  - Option A: Always restart all services listed in post-deploy commands
  - Option B: Only restart services whose files changed (requires tracking changed files from rsync output)
  - Option C: Configurable per-service: "always restart" vs "restart if changed" vs "never restart"
  - Resolution: Option A. Always restart all listed services after deploy. Single-VPS deploys are infrequent enough that unnecessary restarts cost seconds. Simplicity over optimization.

## Acceptance Criteria
- Generates a complete deploy script from parameters
- Standard excludes cover all common patterns
- Health check is mandatory with clear fail/pass output
- Works for both Python and Node.js projects

## Out of Scope
- NOT Docker, NOT CI/CD pipelines — rsync+SSH only
- Does NOT manage remote server provisioning or initial setup (assumes VPS is configured)
- Does NOT handle database migrations beyond running a provided command
- Does NOT support multi-server / load-balanced deployments — single VPS target only
- Does NOT replace existing deploy scripts — generates new ones (migration is manual)

## Verification
- Generate a deploy script for portfolio-system with its known parameters (Hetzner VPS, Python/FastAPI, systemd services)
- Diff generated script against portfolio-system/scripts/deploy.sh — should cover the same steps with parameterized values
- Verify standard excludes list contains: .git, __pycache__, .env, data/, node_modules/, venv/
- Verify health check section is present and exits non-zero on failure
- Verify generated script is valid bash (bash -n script passes)

## Reference Implementation
- `meta-tools/deploy-rsync/SKILL.md` — the skill itself (if already built; validate against this mission requirements)
- Source pattern: portfolio-system/scripts/deploy.sh

## Effort: S (1-2 hours)
