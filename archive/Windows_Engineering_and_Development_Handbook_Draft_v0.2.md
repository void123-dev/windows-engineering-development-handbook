# Windows Engineering & Development Handbook

Building a Modern Development Environment for Software Engineers

Draft Edition 0.2

# **Preface**

This handbook is intended to become a long-term engineering reference rather than a one-time installation guide. Every chapter explains not only how to configure a tool, but also why a particular approach is recommended, alternative solutions, best practices and common pitfalls.

# **Engineering Principles**

* Single Source of Truth  
* Environment Parity  
* Automation First  
* Project Isolation  
* Infrastructure as Code  
* Reproducible Development Environments  
* Documentation as Code

# **Book Structure**

## **Part I. Operating System & Development Environment**

* Windows configuration  
* WSL2  
* Docker Desktop  
* Linux toolchain  
* AI development environment  
* Project directory layout

## **Part II. IDE & Development Tools**

* PhpStorm  
* VS Code  
* Remote Development  
* Quality Tools  
* Debugging

## **Part III. Technology Profiles**

* WordPress  
* Laravel  
* Docker-first  
* Remote Development

## **Part IV. Engineering Best Practices**

* Composer  
* Git  
* Docker  
* Code Quality  
* AI-assisted development  
* Performance  
* Security

## **Part V. Infrastructure**

* NGINX  
* Redis  
* MariaDB

### **Cloudflare**

* APO Cache Everything: [https://onlinemediamasters.com/cloudflare-apo-wordpress/](https://onlinemediamasters.com/cloudflare-apo-wordpress/)  
* Page Rules For WordPress  
  * [https://onlinemediamasters.com/cloudflare-page-rules-for-wordpress/](https://onlinemediamasters.com/cloudflare-page-rules-for-wordpress/)  
  * WooCommerce  
    * [https://blog.cloudflare.com/ecommerce-best-practices/\#method2populatingviajavascriptajax](https://blog.cloudflare.com/ecommerce-best-practices/#method2populatingviajavascriptajax)  
* Workers  
  * https://www.maxivanov.io/how-to-password-protect-your-website-with-cloudflare-workers/

* EasyEngine

## **Part VI. New Machine Checklist**

* Complete workstation provisioning checklist

## **Appendices**

* Recommended software  
* Templates  
* Reference configurations  
* Useful commands

# **Part I. Operating System & Development Environment**

## **Chapter 1\. Windows Preparation**

* Windows Update  
* Virtualization  
* Windows Terminal  
* PowerShell 7  
* Developer Mode

## **Chapter 2\. WSL2**

* Install Ubuntu LTS  
* Configure Linux user  
* Filesystem layout  
* SSH keys  
* Shell configuration

### **Dev Toolchain**

✅ Git

✅ PHP

✅ Composer

✅ Node.js

✅ wp-env

✅ WP-CLI

✅ Codex CLI

## **Chapter 3\. Docker Desktop**

* Install Docker Desktop  
* Enable WSL backend  
* Resource allocation  
* Docker Compose

## **Chapter 4\. Linux Development Toolchain**

* Git  
* PHP  
* Composer  
* Node.js LTS  
* npm / pnpm  
* WP-CLI  
* wp-env  
* Laravel Installer

## **Chapter 5\. AI Development Environment**

* Codex Desktop  
* Codex CLI  
* GitHub Copilot  
* AGENTS.md

## **Chapter 6\. Project Layout**

* \~/development/php/wordpress  
* \~/development/php/laravel  
* \~/development/docker  
* \~/development/scripts

# **Part II. IDE & Development Tools**

## **PhpStorm Professional Setup**

### **Global IDE settings**

#### ***PHP***

##### Claude Code plugin

##### Debug

##### Servers

##### Composer

##### Quality Tools

#### ***Appearance & Behavior***

##### Appearance 

**Themes**

* High Contrast  
* Dracula  
* Gerry Themes  
* Material Theme UI (+Lite)  
* Gradianto  
* Cyan Light theme  
* Sakura Theme  
* Catppuccin \++  
* Obsidian  
* Cobalt 2

**Color Schemes**

* All hallow’s eve  
* Blackboard  
* Cobalt \++  
* Solarized Dark  
* Vibrantink \++

#### ***Editor***

##### Code Style

##### Inspection

##### Intentions

#### ***Plugins***

##### Git

* Ignore

##### AI

* GitHub Copiot  
* DeepSeek Assistant

##### Frameworks

* Symfony  
* Laravel Idea

##### File Manager

* Tree Gen

##### Quality Tools

* PHPStan Toolbox  
* Php Inspections

##### Documentation

* PHP Annotation

##### Terminal

* IdeaVim

##### Syntaxis

* Rainbow Brackets

##### Translation

* Easy l18n

##### Web Servers

* NGINX Configuration  
* Nginx Support 

##### Tools

* I Love DevToys  
* String Manipulation

##### CSS

* TailWind CSS Smart Completions

##### HTTP

* HTTP Client Fallback  
* gRPC  
* Endpoints  
* GraphQL  
* HTTPX Request

#### ***Version Control***

* GitHub Account

#### ***Directories***

#### ***Build, Execution, Deployment***

#### ***Languages & Frameworks***

##### JavaScript

##### JavaScript Runtime

* [Node.js](http://Node.js) install \-\> Docker Image

#### ***Tools***

##### AI Assistance

* Markdown разметка (GitHub Flavored Markdown)

###### [*AGENTS.md*](http://AGENTS.md)

\#\# AI Instructions

When making changes:

1\. Reuse existing project architecture.

2\. Keep changes minimal and focused.

3\. Do not refactor unrelated code.

4\. Preserve public APIs unless explicitly requested.

5\. Explain significant architectural decisions.

6\. Prefer readability over clever code.

**AI Documentation**

* Project Overview  
* Technology Stack  
* Development Environment  
* Repository Structure  
* Architecture  
* Coding Standards  
* WordPress Best Practices  
* Security Guidelines  
* Performance Guidelines  
* Development Workflow  
* Git Workflow  
* Testing Workflow  
* AI Instructions  
* AI Review Checklist

###### *Additional AI instructions*

* Create .ai/ folder  
  * architecture.md  
  * coding-standards.md  
  *  self-review.md  
  *  workflows.md  
  *  project-map.md

###### *Agents*

* Install

###### *MCP*

###### *Project Settings (internal [AGENTS.md](http://AGENTS.md))*

Как AI должен вести себя именно внутри текущего проекта

* Create .aiignore  
  * vendor/  
  * node\_modules/  
  * .idea/  
  * .git/  
* AI Self-Review (аналог CI Checklist after code generating)

  \# Self Review

  Before completing the task verify:

  \- No syntax errors

  \- WordPress Coding Standards followed

  \- No duplicated logic

  \- Backward compatibility preserved

  \- Escaping is present

  \- Sanitization is present

  \- SQL is prepared

  \- Nonces verified

  \- No unnecessary complexity

###### *Prompt Library*

Используется во время генерации кода 

###### *Rules*

* Describe project  rules

###### *Skills*

* Install

#### ***Advanced Settings***

* AI Assistant Enable  
* Angular \-\> Enable  
* Gateway WSL \-\> Enable

## **VS Code**

* Extensions  
* Remote WSL  
* Debugging

## **Quality Tools**

* https://deliciousbrains.com/php-static-code-analysis/  
* Installing for local project with Composer  
* PHP\_CodeSniffer  
* PHPStan  
* PHP CS Fixer  
* Rector  
* PHPUnit

## **Remote Development**

* WSL Connection  
* SSH  
* Docker  
* Path mappings

# **Part IV. Engineering Best Practices**

## **Composer**

{

	"name": "",

	"description": "",

	"type": "wordpress-plugin",

	"license": "GPL-2.0-or-later",

	"require": {

		"php": "\>=8.2"

	},

	"require-dev": {

		"dealerdirect/phpcodesniffer-composer-installer": "^1.0",

		"wp-coding-standards/wpcs": "^3.0",

		"phpcompatibility/phpcompatibility-wp": "^2.1",

		"phpstan/phpstan": "^2.1",

		"szepeviktor/phpstan-wordpress": "^2.0"

	},

	"autoload": {

		"psr-4": {

			"": "src/"

		}

	},

	"scripts": {

		"lint": "phpcs",

		"lint:fix": "phpcbf",

		"analyse": "phpstan analyse",

		"quality": \[

			"@lint",

			"@analyse"

		\]

	},

	"config": {

		"allow-plugins": {

			"dealerdirect/phpcodesniffer-composer-installer": true

		},

		"sort-packages": true

	}

}

# **Roadmap**

Each chapter will eventually follow the same structure:

* Overview  
* Why this tool or approach  
* Installation  
* Configuration  
* Verification  
* Best Practices  
* Alternatives  
* Troubleshooting  
* Common Mistakes  
* Reference Links

# **Version History**

v0.2

* Renamed the project to Windows Engineering & Development Handbook  
* Expanded scope from PhpStorm to the complete Windows PHP engineering environment  
* Added book structure and engineering principles  
* Prepared roadmap for future chapters