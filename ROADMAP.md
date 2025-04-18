# CRUD App Generator: Development Roadmap

## Phase 1: Core Enhancements & Stability

- [ ] **Database Setup & Connection Handling**
  - [x] Auto-generate a `database.py` for engine/session management
  - [x] Allow config-driven selection of DB backend (SQLite, Postgres, etc)
  - [ ] Integrate Alembic for migrations (optional)
- [ ] **Pydantic Schema Generation**
  - [ ] Auto-generate Pydantic models for each SQLAlchemy model
  - [ ] Use schemas for request validation and response serialization in routes
- [ ] **Config Validation & Error Reporting**
  - [ ] Implement schema validation for YAML configs (using Pydantic or similar)
  - [ ] Provide clear, actionable error messages for invalid configs

---

## Phase 2: Developer Experience & Testing

- [ ] **Testing Infrastructure**
  - [ ] Generate a `tests/` directory with example unit/integration tests for models and routes
  - [ ] Add tests for the generator itself (CLI, code output)
- [ ] **Improved CLI & UX**
  - [ ] Add `--dry-run` and `--diff` flags to preview changes
  - [ ] Support interactive mode for config creation (e.g., using Typer or Questionary)
  - [ ] Add verbosity flags for CLI output
- [ ] **Logging & Debugging**
  - [ ] Add structured logging to generator and CLI
  - [ ] Improve error handling throughout

---

## Phase 3: Extensibility & Customization

- [ ] **Plugin/Template System**
  - [ ] Refactor code generation into pluggable modules for models, routes, schemas, etc.
  - [ ] Organize Jinja2 templates by framework and allow user overrides
  - [ ] Prepare for multi-framework support (Flask, Django, Express)
- [ ] **Hooks & Customization**
  - [ ] Allow pre- and post-generation hooks for advanced users
  - [ ] Support user-provided custom templates or code snippets

---

## Phase 4: Production Readiness

- [ ] **Deployment Configs**
  - [ ] Optionally generate Dockerfile, docker-compose, and/or serverless configs
  - [ ] Provide sample deployment guides for FastAPI
- [ ] **Documentation & Examples**
  - [ ] Write comprehensive docs: YAML schema, CLI usage, extending the generator
  - [ ] Provide example configs and generated apps for common use cases

---

## Phase 5: Advanced Features & Community

- [ ] **Framework Support**
  - [ ] Add support for additional backends (Flask, Django, Express)
  - [ ] Abstract interfaces for models, routes, and schemas
- [ ] **API/Library Mode**
  - [ ] Expose the generator as a Python package with a public API for programmatic use
- [ ] **Community & Contribution**
  - [ ] Add contribution guidelines, issue templates, and a code of conduct
  - [ ] Gather feedback and iterate based on user needs
