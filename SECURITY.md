# Security Policy

## Supported Versions

Branches follow Odoo major versions. Security fixes are provided for the latest
release of each supported branch.

| Odoo version | Branch | Supported          |
| ------------ | ------ | ------------------ |
| 19.x         | `19.0` | :white_check_mark: |
| 18.x         | `18.0` | :white_check_mark: |
| 17.x         | `17.0` | :white_check_mark: |
| < 17.0       | —      | :x:                |

## Scope

This repository contains the maesn Odoo module, which adds a menu entry linking
to [maesn](https://www.maesn.com/integrations/odoo). It does not store
credentials, call external APIs, or process business data inside Odoo.

In scope:

- Code and data files in this repository (`maesn/`)
- Issues in how the module integrates with Odoo (e.g. menu, access rights, XML data)

Out of scope (report via the channels below, but not handled here):

- The maesn platform
- Vulnerabilities in Odoo core or third-party Odoo modules — report those to
  [Odoo](https://www.odoo.com/security-report)

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues,
pull requests, or discussions.**

Instead, email **support@maesn.com** with the subject line `[SECURITY] Odoo module`.

Please include:

- Affected branch / module version
- Description of the issue and its potential impact
- Steps to reproduce or a proof of concept
- Any suggested fix, if available

